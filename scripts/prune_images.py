import os
import re
import urllib.parse
from pathlib import Path
import argparse
import sys

# Force UTF-8 output
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass # Python < 3.7


def prune_images(root_dir, delete=False, output_file=None):
    # Redirect print to file if output_file is specified
    original_stdout = sys.stdout
    if output_file:
        f = open(output_file, 'w', encoding='utf-8')
        sys.stdout = f

    try:
        root_path = Path(root_dir).resolve()
        assets_dir = root_path / '.gitbook' / 'assets'
    
        if not assets_dir.exists():
            print(f"Assets directory not found: {assets_dir}")
            return

        # 1. Get all asset files
        asset_files = set()
        print(f"Scanning assets in {assets_dir}...")
        for root, _, files in os.walk(assets_dir):
            for file in files:
                # We treat all files in assets as potential targets
                full_path = Path(root) / file
                asset_files.add(str(full_path.resolve()).lower()) # Store as lower case absolute string for comparison

        print(f"Found {len(asset_files)} asset files.")

        # 2. Find all markdown files
        md_files = []
        for root, dirs, files in os.walk(root_path):
            if '.git' in dirs: dirs.remove('.git')
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.gitbook' in dirs: dirs.remove('.gitbook') # Don't scan inside .gitbook itself for references (unless docs are there?)
            
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)

        print(f"Scanning {len(md_files)} markdown files for references...")

        # Regex patterns
        # [text](url) - standard link
        inline_link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
        # [id]: url - reference link definition
        ref_link_def_pattern = re.compile(r'^\[.*?\]:\s*(.*?)$', re.MULTILINE)
        # <url> - angle bracket link
        angle_link_pattern = re.compile(r'<(.*?)>')
        # HTML img tag src="..."
        html_img_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']', re.IGNORECASE)

        referenced_assets = set()

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
            except Exception as e:
                print(f"Error reading {md_file}: {e}")
                continue

            links = []
            links.extend(inline_link_pattern.findall(content))
            links.extend(ref_link_def_pattern.findall(content))
            links.extend(angle_link_pattern.findall(content))
            links.extend(html_img_pattern.findall(content))

            for link in links:
                link = link.strip()
                if not link or link.startswith(('http:', 'https:', 'mailto:', 'ftp:')):
                    continue
                
                link = link.split('#')[0].split('?')[0]
                # Handle encoded spaces %20
                link = urllib.parse.unquote(link)
                
                # Resolve path
                target_path = None
                try:
                    if link.startswith('/'):
                        # Relative to root
                        abs_target = (root_path / link.lstrip('/')).resolve()
                    else:
                        # Relative to current file
                        abs_target = (md_file.parent / link).resolve()
                    
                    abs_target_str = str(abs_target).lower()
                    if abs_target_str in asset_files:
                        referenced_assets.add(abs_target_str)
                        
                except Exception:
                    continue

        # 3. Identify Orphans
        orphans = []
        for asset in asset_files:
            if asset not in referenced_assets:
                orphans.append(asset)

        orphans.sort()

        print(f"\nSummary:")
        print(f"Total assets: {len(asset_files)}")
        print(f"Referenced assets: {len(referenced_assets)}")
        print(f"Orphan assets: {len(orphans)}")

        if orphans:
            print("\nOrphan files:")
            for orphan in orphans:
                 # Print relative path for readability
                try:
                    print(Path(orphan).relative_to(root_path))
                except:
                    print(orphan)

            if delete:
                print("\nDeleting orphans...")
                for orphan in orphans:
                    try:
                        os.remove(orphan)
                        print(f"Deleted: {orphan}")
                    except Exception as e:
                        print(f"Failed to delete {orphan}: {e}")
            else:
                print("\nDry run completed. Use --delete to remove files.")
            
    finally:
        if output_file:
            sys.stdout = original_stdout
            f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find and prune orphan images.')
    parser.add_argument('--root', help='Root directory of the repository', default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument('--delete', action='store_true', help='Delete found orphan files')
    parser.add_argument('--output', help='Output file for the report')
    
    args = parser.parse_args()
    
    root_dir = Path(args.root)
    output_file = args.output
    
    if not output_file:
        output_dir = root_dir / 'scripts-output'
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / 'unused_assets.txt'
        
    prune_images(str(root_dir), args.delete, str(output_file))
