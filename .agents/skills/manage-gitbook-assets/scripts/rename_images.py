import os
import re
from pathlib import Path
import shutil
import urllib.parse

REPO_ROOT = Path(r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs")
ASSETS_DIR = REPO_ROOT / ".gitbook" / "assets"

def is_generic_image(filename):
    # Only jpg and png based on user request
    if not filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        return False
    
    basename = os.path.basename(filename)
    lower_basename = basename.lower()
    
    # Generic patterns
    if lower_basename.startswith('image-'):
        return True
    if lower_basename.startswith('image '):
        return True
    if lower_basename.startswith('image('):
        return True
    if lower_basename.startswith('img_'):
        return True
    if lower_basename.startswith('screenshot_'):
        return True
    if lower_basename.startswith('win_'):
        return True
    if lower_basename.startswith('slide_'):
        return True
    if lower_basename.startswith('gemini_'):
        return True
    if re.match(r'^\d{8}', lower_basename): # dates like 20260226
        return True
    
    return False

def get_markdown_files():
    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Exclude directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts-output']
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    return md_files

def extract_image_references(content):
    references = []
    # Markdown image syntax: ![alt](url)
    md_matches = re.finditer(r'!\[.*?\]\((.*?)\)', content)
    for match in md_matches:
        url = match.group(1)
        references.append((match.start(1), match.end(1), url))
        
    # HTML img syntax: <img src="url" ...> or <img ... src="url" ...>
    # Simple regex for src attribute
    html_matches = re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for match in html_matches:
        url = match.group(1)
        references.append((match.start(1), match.end(1), url))
        
    return references

def main():
    md_files = get_markdown_files()
    
    # Map image filename -> list of (Path_to_md, url_in_md)
    image_refs = {}
    
    print(f"Scanning {len(md_files)} markdown files...")
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
            
        refs = extract_image_references(content)
        for start, end, url in refs:
            # Decode URL in case of %20
            decoded_url = urllib.parse.unquote(url)
            basename = os.path.basename(decoded_url)
            
            # Remove any #hash or ?query from basename
            basename = basename.split('#')[0].split('?')[0]
            
            if not is_generic_image(basename):
                continue
                
            if basename not in image_refs:
                image_refs[basename] = []
            image_refs[basename].append({'md_file': md_file, 'url': url})

    print(f"Found {len(image_refs)} unique generic images referenced in markdown files.")
    
    # Find images with exactly ONE referring document
    renames = {} # old_basename -> new_basename
    
    for basename, refs in image_refs.items():
        # Get unique referencing markdown files (in case one file references the same image multiple times)
        unique_md_files = list(set([str(r['md_file']) for r in refs]))
        
        if len(unique_md_files) == 1:
            md_path = Path(unique_md_files[0])
            doc_basename = md_path.stem
            
            ext = os.path.splitext(basename)[1]
            
            # Compute new name. If multiple images are referenced by this doc, we add an index.
            # We will handle index assignment later by iterating through all images mapped to this doc.
            if md_path not in renames:
                renames[md_path] = []
            renames[md_path].append(basename)

    total_renamed = 0
    
    # To keep track of new names to avoid collisions
    all_new_names = set()
    
    # Execute renames
    for md_path, basenames in renames.items():
        doc_basename = md_path.stem
        
        for idx, old_basename in enumerate(basenames):
            ext = os.path.splitext(old_basename)[1].lower()
            
            # E.g. tablet-evaluation-1.jpg
            new_basename = f"{doc_basename}-{idx+1}{ext}"
            
            # Ensure new name doesn't collide
            counter = idx + 1
            while new_basename in all_new_names or (ASSETS_DIR / new_basename).exists():
                counter += 1
                new_basename = f"{doc_basename}-{counter}{ext}"
            
            all_new_names.add(new_basename)
            
            old_asset_path = ASSETS_DIR / old_basename
            new_asset_path = ASSETS_DIR / new_basename
            
            if old_asset_path.exists():
                # Rename the actual file
                old_asset_path.rename(new_asset_path)
                print(f"Renamed file: {old_basename} -> {new_basename}")
                
                # Update the markdown file
                try:
                    content = md_path.read_text(encoding='utf-8')
                    # Replace URL, careful with escaping.
                    # We can use simple replace because the URL in markdown is what we stored.
                    # However, we have a list of all references in this file.
                    refs_in_this_file = [r for r in image_refs[old_basename] if str(r['md_file']) == str(md_path)]
                    
                    for r in refs_in_this_file:
                        old_url = r['url']
                        # The new URL should just replace the basename.
                        old_url_decoded = urllib.parse.unquote(old_url)
                        old_basename_in_url = os.path.basename(old_url_decoded).split('#')[0].split('?')[0]
                        
                        # We need to construct the new URL properly
                        # E.g. ../.gitbook/assets/image-000123.jpg -> ../.gitbook/assets/tablet-evaluation-1.jpg
                        # A simple string replace on the URL string might be enough.
                        # Using regex to replace just the filename at the end of the URL
                        # URL looks like: ../.gitbook/assets/image%20(1).png
                        
                        # Just parse and replace
                        parts = old_url.rsplit('/', 1)
                        if len(parts) == 2:
                            new_url = parts[0] + '/' + urllib.parse.quote(new_basename)
                        else:
                            new_url = urllib.parse.quote(new_basename)
                            
                        # Now replace old_url with new_url in content
                        # Since multiple identical references might exist, standard replace is fine
                        content = content.replace(old_url, new_url)
                        
                    md_path.write_text(content, encoding='utf-8')
                    total_renamed += 1
                except Exception as e:
                    print(f"Failed to update markdown file {md_path}: {e}")
            else:
                print(f"Warning: Image {old_basename} referenced by {md_path} not found in {ASSETS_DIR}")

    print(f"Successfully processed {total_renamed} images.")

if __name__ == '__main__':
    main()
