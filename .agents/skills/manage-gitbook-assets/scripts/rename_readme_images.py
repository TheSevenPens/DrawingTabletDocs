import os
import re
import sys
from pathlib import Path
import shutil
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assetrefs

REPO_ROOT = Path(r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs")
ASSETS_DIR = REPO_ROOT / ".gitbook" / "assets"

def is_generic_or_readme_image(filename):
    if not filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        return False
    
    basename = os.path.basename(filename)
    lower_basename = basename.lower()
    
    # Generic patterns + README prefix
    if lower_basename.startswith('readme-'):
        return True
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
    # Delegates to assetrefs so all three scripts parse references the same
    # way. The old regex here truncated `![](<name (1).png>)` at the first
    # closing paren; see assetrefs.py for details.
    return assetrefs.extract_references(content)

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
            # Skip externally hosted images; only local assets can be renamed.
            if url.startswith(('http://', 'https://', 'data:')):
                continue
            decoded_url = urllib.parse.unquote(url)
            basename = os.path.basename(decoded_url)
            
            basename = basename.split('#')[0].split('?')[0]
            
            if not is_generic_or_readme_image(basename):
                continue
                
            if basename not in image_refs:
                image_refs[basename] = []
            image_refs[basename].append({'md_file': md_file, 'url': url})

    print(f"Found {len(image_refs)} unique generic/README images referenced in markdown files.")
    
    renames = {} # md_path -> list of old_basenames
    
    for basename, refs in image_refs.items():
        unique_md_files = list(set([str(r['md_file']) for r in refs]))
        
        if len(unique_md_files) == 1:
            md_path = Path(unique_md_files[0])
            
            # We ONLY process images uniquely referenced by README.md files
            if md_path.name.lower() != 'readme.md':
                continue
                
            if md_path not in renames:
                renames[md_path] = []
            renames[md_path].append(basename)

    total_renamed = 0
    all_new_names = set()
    
    # Execute renames
    for md_path, basenames in renames.items():
        # Get parent directory name
        if md_path.parent == REPO_ROOT:
            parent_name = 'DrawingTabletDocs'
        else:
            parent_name = md_path.parent.name
            
        for idx, old_basename in enumerate(basenames):
            ext = os.path.splitext(old_basename)[1].lower()
            
            # E.g. pens-1.jpg
            new_basename = f"{parent_name}-{idx+1}{ext}"
            
            counter = idx + 1
            while new_basename in all_new_names or (ASSETS_DIR / new_basename).exists():
                counter += 1
                new_basename = f"{parent_name}-{counter}{ext}"
            
            all_new_names.add(new_basename)
            
            old_asset_path = ASSETS_DIR / old_basename
            new_asset_path = ASSETS_DIR / new_basename
            
            if old_asset_path.exists():
                old_asset_path.rename(new_asset_path)
                print(f"Renamed file: {old_basename} -> {new_basename}")
                
                try:
                    content = md_path.read_text(encoding='utf-8')
                    refs_in_this_file = [r for r in image_refs[old_basename] if str(r['md_file']) == str(md_path)]
                    
                    for r in refs_in_this_file:
                        old_url = r['url']
                        parts = old_url.rsplit('/', 1)
                        if len(parts) == 2:
                            new_url = parts[0] + '/' + urllib.parse.quote(new_basename)
                        else:
                            new_url = urllib.parse.quote(new_basename)
                            
                        content = content.replace(old_url, new_url)
                        
                    md_path.write_text(content, encoding='utf-8')
                    total_renamed += 1
                except Exception as e:
                    print(f"Failed to update markdown file {md_path}: {e}")
            else:
                print(f"Warning: Image {old_basename} referenced by {md_path} not found in {ASSETS_DIR}")

    print(f"Successfully processed {total_renamed} README images.")

if __name__ == '__main__':
    main()
