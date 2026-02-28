import sys
import os
import re
from pathlib import Path

from gitbooklib import GitBookDocs, LINK_PATTERN

def parse_arg(args, key):
    try:
        idx = args.index(key)
        if idx + 1 < len(args):
            return args[idx + 1]
    except ValueError:
        pass
    return None

def update_link_titles(root_dir, dry_run=False):
    docs = GitBookDocs(root_dir)
    root_dir_path = Path(root_dir).resolve()
    try:
        pages = docs.get_summary_pages()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    title_cache = {}

    def get_title(file_path):
        resolved_path = file_path.resolve()

        if resolved_path.is_dir():
            resolved_path = resolved_path / "README.md"

        if not resolved_path.exists():
            return None

        cache_key = str(resolved_path)
        if cache_key in title_cache:
            return title_cache[cache_key]

        try:
            content_lines = resolved_path.read_text(encoding='utf-8').splitlines()
            title = docs.get_page_title(content_lines)
            if title and title != "Unknown Title":
                title_cache[cache_key] = title
                return title
        except Exception as e:
            print(f"Error reading {resolved_path}: {e}")

        title_cache[cache_key] = None
        return None

    print(f"Found {len(pages)} pages in SUMMARY.md. Updating links...")

    changed_files = 0

    for relative_path in pages:
        if relative_path == 'SUMMARY.md' or relative_path.endswith('/SUMMARY.md'):
            continue

        full_path = docs.resolve_page_path(relative_path)
        
        if not full_path.exists():
            continue
            
        current_dir = full_path.parent
        
        try:
            content = full_path.read_text(encoding='utf-8')
            original_content = content

            custom_link_pattern = re.compile(r'(\\?)\[(.*?)\]\((.*?)\)(\s*\]?)')

            def replace_link(match):
                prefix = match.group(1)
                text = match.group(2)
                raw_link = match.group(3)
                suffix = match.group(4)
                
                # Check if it's an image link (e.g., prefix is '!')
                if match.start() > 0 and match.string[match.start() - 1] == '!':
                    return match.group(0)

                # Ignore links where the anchor itself is an image
                if text.strip().startswith('![') or '<img ' in text:
                    return match.group(0)

                # Cleanup link to resolve properly
                link = raw_link
                if ' "' in link:
                    link = link.split(' "')[0]
                elif ' ' in link:
                    link = link.split(' ')[0]

                link = link.strip()

                if link.startswith(('http', 'ftp', 'mailto:', '#', '<')):
                    return match.group(0)

                # Remove anchors/query to resolve file
                base_link = link.split('#')[0].split('?')[0]
                
                if not base_link:
                    return match.group(0)

                # Filter to likely markdown/directory links
                if not base_link.lower().endswith('.md') and not base_link.endswith('/'):
                    if os.path.splitext(base_link)[1]:  # has other extension
                        return match.group(0)

                # Resolve target file path
                try:
                    target_abs = (current_dir / base_link).resolve()
                except Exception:
                    return match.group(0)
                
                # Ensure we don't escape root_dir
                try:
                    target_abs.relative_to(root_dir_path)
                except ValueError:
                    return match.group(0)
                    
                title = get_title(target_abs)
                
                is_malformed = (prefix == '\\') or (']' in suffix)
                title_to_use = title if (title and title != "Unknown Title") else text
                
                if (title and title != text) or is_malformed:
                    # Update link to new title or fix malformed structure!
                    if ']' in suffix:
                        clean_suffix = ""
                    else:
                        clean_suffix = suffix
                        
                    return f"[{title_to_use}]({raw_link}){clean_suffix}"
                    
                return match.group(0)

            updated_content = custom_link_pattern.sub(replace_link, content)
            
            if updated_content != original_content:
                if not dry_run:
                    full_path.write_text(updated_content, encoding='utf-8')
                print(f"Updated links in {relative_path}")
                changed_files += 1

        except Exception as e:
            print(f"Error processing {relative_path}: {e}")
            
    if dry_run:
        print(f"Dry run complete. Would have updated {changed_files} files.")
    else:
        print(f"Update complete. Changed links in {changed_files} files.")

if __name__ == "__main__":
    root_dir = parse_arg(sys.argv, '--root')
    dry_run = '--dry-run' in sys.argv

    if not root_dir:
        current = Path.cwd()
        while True:
            if (current / "SUMMARY.md").exists():
                root_dir = str(current)
                break
            if current.parent == current:
                break
            current = current.parent

    if not root_dir:
        print("Error: Could not determine repository root. Please use --root.")
        sys.exit(1)

    update_link_titles(root_dir, dry_run=dry_run)
