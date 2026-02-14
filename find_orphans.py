import os
import re
import urllib.parse
from pathlib import Path

def find_orphans(root_dir):
    root_path = Path(root_dir).resolve()
    all_files = set()
    referenced_files = set()
    
    # 1. Get all md files
    for root, dirs, files in os.walk(root_path):
        # Exclude .git and node_modules
        if '.git' in dirs:
            dirs.remove('.git')
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
            
        for file in files:
            if file.endswith('.md'):
                full_path = Path(root) / file
                try:
                    rel_path = full_path.relative_to(root_path)
                    all_files.add(str(rel_path).replace('\\', '/'))
                except ValueError:
                    pass

    # Regex patterns
    # [text](url) - standard link
    inline_link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    # [id]: url - reference link definition
    ref_link_def_pattern = re.compile(r'^\[.*?\]:\s*(.*?)$', re.MULTILINE)
    # <url> - angle bracket link
    angle_link_pattern = re.compile(r'<(.*?)>')
    
    # 2. Process files to find links
    for root, dirs, files in os.walk(root_path):
        if '.git' in dirs: dirs.remove('.git')
        if 'node_modules' in dirs: dirs.remove('node_modules')

        for file in files:
            if not file.endswith('.md'):
                continue
                
            current_file_path = Path(root) / file
            try:
                content = current_file_path.read_text(encoding='utf-8', errors='ignore')
            except Exception as e:
                print(f"Error reading {current_file_path}: {e}")
                continue
                
            links = []
            
            # Extract links
            matches = inline_link_pattern.findall(content)
            links.extend(matches)
            
            matches = ref_link_def_pattern.findall(content)
            links.extend(matches)
            
            matches = angle_link_pattern.findall(content)
            links.extend(matches)
            
            for link in links:
                # Clean link
                link = link.strip()
                if not link or link.startswith(('http:', 'https:', 'mailto:', 'ftp:')):
                    continue
                
                link = link.split('#')[0].split('?')[0]
                if not link:
                    continue

                # Resolve path
                target_path = None
                try:
                    if link.startswith('/'):
                        # Relative to root
                        abs_target = root_path / link.lstrip('/')
                    else:
                        # Relative to current file
                        abs_target = (current_file_path.parent / link).resolve()
                    
                    try:
                        rel_target = abs_target.relative_to(root_path)
                        target_path = str(rel_target).replace('\\', '/')
                    except ValueError:
                        # Path is outside root
                        continue
                        
                except Exception:
                    continue
                
                if target_path:
                    if target_path in all_files:
                         referenced_files.add(target_path)
                    else:
                        # Try percent decoding and check again
                        try:
                            decoded = urllib.parse.unquote(target_path)
                            if decoded in all_files:
                                referenced_files.add(decoded)
                        except:
                            pass

    # 3. Add entry points
    entry_points = ["README.md", "SUMMARY.md", "summary.md", "readme.md"]
    for ep in entry_points:
        if ep in all_files:
            referenced_files.add(ep)
            
    # 4. Find orphans
    orphans = []
    for f in all_files:
        if f not in referenced_files:
            # Also check if it ends with README.md as per original script logic
            if not f.lower().endswith("readme.md"):
                orphans.append(f)
                
    orphans.sort()
    
    print(f"Found {len(all_files)} markdown files.")
    print(f"Found {len(referenced_files)} referenced files.")
    print(f"Found {len(orphans)} orphan files (excluding README.md):")
    for o in orphans:
        print(o)

if __name__ == "__main__":
    find_orphans('.')
