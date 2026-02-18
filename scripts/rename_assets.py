import os
import re
import urllib.parse
from pathlib import Path
import shutil
import uuid

# Configuration
ASSET_DIR_NAME = '.gitbook/assets'
NEW_NAME_PREFIX = 'image-'
NEW_NAME_DIGITS = 6 # image-000001

def rename_assets(root_dir, dry_run=False):
    root_path = Path(root_dir).resolve()
    assets_dir = root_path / '.gitbook' / 'assets'
    
    if not assets_dir.exists():
        print(f"Error: Assets directory {assets_dir} not found.")
        return

    # 1. Scan and Sort Assets
    print("Scanning assets...")
    assets = [] # List of Path objects
    for root, _, files in os.walk(assets_dir):
        for file in files:
            assets.append((Path(root) / file).resolve())
    
    # Sort to ensure deterministic renaming (e.g. alphabetical)
    assets.sort(key=lambda p: str(p).lower())
    
    print(f"Found {len(assets)} assets.")

    # 2. Generate Mapping
    # Map absolute path -> new filename (e.g. image-000001.png)
    # We rename to a temp name first to avoid collisions, but logic requires knowing final name.
    # Actually, we can just track the final name.
    
    asset_map = {} # abs_path -> new_filename
    
    for i, asset_path in enumerate(assets):
        ext = asset_path.suffix
        new_filename = f"{NEW_NAME_PREFIX}{str(i+1).zfill(NEW_NAME_DIGITS)}{ext}"
        asset_map[str(asset_path).lower()] = new_filename # Use lower for case-insensitive matching usually on Windows

    print("Mapping generated.")

    # 3. Process Markdown Files
    print("Scanning markdown files...")
    md_files = []
    for root, dirs, files in os.walk(root_path):
        if '.git' in dirs: dirs.remove('.git')
        if 'node_modules' in dirs: dirs.remove('node_modules')
        
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
                
    print(f"Found {len(md_files)} markdown files. Updating links...")

    # Regex patterns (Same as check_links.py)
    # inline_link_pattern = re.compile(r'\[.*?\]\((.*?)\)') # Naive
    # Better to capture full link to handle replacement safely using span
    
    # We will read file, find all links, resolve them. If they map to an asset, we calculate range and replacement.
    # We construct a list of replacements (start, end, new_text) and apply them in reverse order.
    
    inline_link_pattern = re.compile(r'\[.*?\]\((<[^>]+>|.*?)\)') 
    ref_link_def_pattern = re.compile(r'^\[.*?\]:\s*(.*?)$', re.MULTILINE)
    angle_link_pattern = re.compile(r'(?<!\\)<(.*?)>')
    html_img_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']', re.IGNORECASE)
    html_href_pattern = re.compile(r'href=["\'](.*?)["\']', re.IGNORECASE) # For html anchors if any

    files_modified = 0
    links_updated = 0

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue

        replacements = [] # (start, end, new_string)

        def process_match(match, group_idx=1, is_angle=False):
            # match is regex match object
            # group_idx is the index of the URL group
            
            raw_url = match.group(group_idx)
            
            # Cleanup raw_url for parsing
            url_to_parse = raw_url
            
            # Handle <url> inside parens
            if url_to_parse.startswith('<') and url_to_parse.endswith('>'):
                 url_to_parse = url_to_parse[1:-1]
            
            # Removing title "Title"
            clean_url = url_to_parse
            title_part = ""
            
            if ' "' in clean_url:
                clean_url, title_part = clean_url.split(' "', 1)
                title_part = ' "' + title_part
            elif " '" in clean_url:
                clean_url, title_part = clean_url.split(" '", 1)
                title_part = " '" + title_part
            elif ' ' in clean_url and not is_angle: # Space only separator if not angle bracket protected
                 # If it was in angle brackets <path with spaces>, we already stripped <> above
                 # But wait, regex for inline link capturing group captures the surrounding <> if present.
                 # logic above: if url_to_parse starts/ends with <>, stripped.
                 # So if it was <a b>, clean_url is "a b". title split shouldn't happen on space in that case?
                 # Standard MD: [text](<url space> "title")
                 pass
                 
            # Fallback cleanup
            clean_url = clean_url.strip()
            
            # Ignore external/anchors
            if clean_url.startswith(('#', 'http:', 'https:', 'mailto:', 'ftp:', 'tel:')):
                return

            # Unquote
            try:
                path_str = urllib.parse.unquote(clean_url.split('?')[0].split('#')[0])
            except:
                return

            # Resolve
            abs_target = None
            try:
                 if path_str.startswith('/'):
                     abs_target = (root_path / path_str.lstrip('/')).resolve()
                 else:
                     abs_target = (md_file.parent / path_str).resolve()
            except:
                return

            # Check mapping
            # print(f"Checking {abs_target}")
            if str(abs_target).lower() in asset_map:
                new_filename = asset_map[str(abs_target).lower()]
                
                # Calculate new relative path
                # New asset location is assets_dir / new_filename
                new_abs_target = assets_dir / new_filename
                
                try:
                    new_rel_path = os.path.relpath(new_abs_target, md_file.parent)
                    new_rel_path = new_rel_path.replace('\\', '/') # Force forward slashes
                    
                    # URL Encode
                    new_url = urllib.parse.quote(new_rel_path)
                    
                    # Reconstruct full matched string part
                    # We need to replace match.group(group_idx).
                    
                    # Be careful with titles.
                    # if raw_url was `../../file.png "Title"`, we want `../../new.png "Title"`
                    
                    # If raw_url had angle brackets `<path>`?
                    # `check_links` regex: `(<[^>]+>|.*?)`
                    
                    prefix = ""
                    suffix = ""
                    
                    if raw_url.startswith('<') and raw_url.endswith('>'):
                        # Was <url "title"> ?? No, title usually outside <> in standard link? 
                        # [link](<url>)
                        # If replacing with something that has NO spaces, we technically don't need <>, but keeping/adding checks is safe.
                        # But quotes normally escape spaces.
                        # Let's simple use the new_url. If it has no spaces, fine.
                        # If original had <>, we can keep <> or drop if not needed.
                        # Simplest: Just use new_url. if titles existed, append them.
                        pass

                    # Rebuild text
                    final_replacement = new_url + title_part
                    
                    # If original was wrapped in <>, and new one doesn't need it? 
                    # If new one doesn't have spaces, it's fine.
                    # If original had <>, replace content inside.
                    
                    if raw_url.startswith('<') and raw_url.endswith('>'):
                         # e.g. <path>
                         # path part replaced. title part?
                         # Usually <path> doesn't have title inside. Title is after.
                         pass
                    
                    # Actually, we are replacing the GROUP.
                    # If regex is `( <...> | ... )`.
                    # If we just put `new_url`, it might break if title was there?
                    
                    # Revised strategy: Just replace the path part in the string.
                    # Find unquoted path in raw_url and replace it?
                    # Dangerous if path is a substring of title.
                    
                    # Let's rely on the parsed structure:
                    # We extracted `clean_url`. We have `new_url`.
                    # We have `title_part`.
                    
                    full_new_string = new_url + title_part
                    
                    # If url needs encoding? already done.
                    
                    replacements.append((match.start(group_idx), match.end(group_idx), full_new_string))
                    
                except ValueError:
                    pass

        # Find matches
        for m in inline_link_pattern.finditer(content): process_match(m, 1)
        for m in ref_link_def_pattern.finditer(content): process_match(m, 1)
        for m in angle_link_pattern.finditer(content): 
             # Check ignore tags
             candidate = m.group(1).strip()
             if not any(candidate.startswith(t) for t in ['br', 'img', 'div', '!']): 
                 process_match(m, 1, is_angle=True)
        for m in html_img_pattern.finditer(content): process_match(m, 1)
        # Href
        for m in html_href_pattern.finditer(content): process_match(m, 1)

        # Apply replacements in reverse
        if replacements:
            # Sort reverse
            replacements.sort(key=lambda x: x[0], reverse=True)
            
            # Filter overlaps? Regex finditer shouldn't produce overlapping matches for same pattern.
            # But different patterns might?
            # E.g. inline_link might match inside angle_link?
            # Unlikely given structure.
            # But safe to check.
            
            new_content = list(content)
            
            last_pos = len(content)
            
            unique_replacements = []
            for start, end, text in replacements:
                if end <= last_pos:
                     unique_replacements.append((start, end, text))
                     last_pos = start
            
            # Wait, sorting reverse by start means we process end of file first.
            # Check overlap: current `end` must be <= previous `start` (which is `last_pos` in reverse iteration)
            
            for start, end, text in unique_replacements:
                new_content[start:end] = list(text)
                links_updated += 1
            
            str_content = "".join(new_content)
            
            if not dry_run:
                md_file.write_text(str_content, encoding='utf-8')
            files_modified += 1

    print(f"Updated {links_updated} links in {files_modified} files.")

    # 4. Rename Files
    print("Renaming files...")
    if not dry_run:
        # Strategy: Rename to temp names first to avoid collisions
        temp_map = {} # old_abs -> temp_abs
        
        for old_abs_str, new_filename in asset_map.items():
            old_path = Path(old_abs_str)
            if not old_path.exists(): 
                print(f"Warning: File {old_path} disappeared?")
                continue
                
            temp_name = f"tmp_{uuid.uuid4()}_{new_filename}"
            temp_path = assets_dir / temp_name
            
            try:
                os.rename(old_path, temp_path)
                temp_map[str(temp_path)] = assets_dir / new_filename
            except Exception as e:
                print(f"Error renaming to temp {old_path}: {e}")

        # Rename temp to final
        for temp_path_str, final_path in temp_map.items():
            try:
                os.rename(temp_path_str, final_path)
            except Exception as e:
                 print(f"Error final rename {final_path}: {e}")

    print("Renaming complete.")
    
if __name__ == "__main__":
    import sys
    dry_run = '--dry-run' in sys.argv
    # Default to the parent directory of this script (repository root)
    root_dir = Path(__file__).resolve().parent.parent
    rename_assets(root_dir, dry_run=dry_run)
