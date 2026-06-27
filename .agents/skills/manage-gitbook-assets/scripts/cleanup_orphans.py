import os
import re
from pathlib import Path
import urllib.parse
import shutil

REPO_ROOT = Path(r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs")
ASSETS_DIR = REPO_ROOT / ".gitbook" / "assets"
UNUSED_DIR = ASSETS_DIR / "unused"

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
    md_matches = re.finditer(r'!\[.*?\]\((.*?)\)', content)
    for match in md_matches:
        references.append(match.group(1))
        
    html_matches = re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for match in html_matches:
        references.append(match.group(1))
        
    return references

def main():
    md_files = get_markdown_files()
    
    referenced_basenames = set()
    
    print(f"Scanning {len(md_files)} markdown files...")
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            continue
            
        refs = extract_image_references(content)
        for url in refs:
            decoded_url = urllib.parse.unquote(url)
            basename = os.path.basename(decoded_url)
            basename = basename.split('#')[0].split('?')[0]
            referenced_basenames.add(basename.lower()) # use lower for case-insensitive matching

    print(f"Found {len(referenced_basenames)} unique referenced images.")
    
    UNUSED_DIR.mkdir(exist_ok=True)
    
    moved_count = 0
    
    for asset_file in ASSETS_DIR.iterdir():
        if not asset_file.is_file():
            continue
            
        lower_name = asset_file.name.lower()
        
        if lower_name not in referenced_basenames:
            # It's an orphan
            destination = UNUSED_DIR / asset_file.name
            try:
                shutil.move(str(asset_file), str(destination))
                moved_count += 1
                # print(f"Moved orphan: {asset_file.name}")
            except Exception as e:
                print(f"Error moving {asset_file.name}: {e}")
                
    print(f"Successfully moved {moved_count} orphaned images to {UNUSED_DIR}")

if __name__ == '__main__':
    main()
