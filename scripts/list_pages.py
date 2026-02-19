import os
import re
import sys
from pathlib import Path

def parse_arg(args, key):
    try:
        idx = args.index(key)
        if idx + 1 < len(args):
            return args[idx + 1]
    except ValueError:
        pass
    return None

def extract_link(line, pattern):
    match = pattern.search(line)
    if match:
        # Group 2 is the link part in regex [text](link)
        raw_link = match.group(2)
        clean_link = raw_link.strip()
        
        if clean_link.startswith('<') and clean_link.endswith('>'):
            clean_link = clean_link[1:-1]
            
        if ' "' in clean_link:
            clean_link = clean_link.split(' "')[0]
        elif ' ' in clean_link:
            clean_link = clean_link.split(' ')[0]
            
        clean_link = clean_link.strip()
        
        if clean_link.startswith(('http', 'ftp', 'mailto:')):
            return None
            
        return clean_link.split('#')[0].split('?')[0]
    return None

def list_pages(root_dir, output_file):
    summary_path = Path(root_dir) / 'SUMMARY.md'
    if not summary_path.exists():
        print(f"Error: SUMMARY.md not found at {summary_path}")
        return

    pages = []
    page_titles = {}
    backlinks = {} # Dict[str, List[Tuple[str, str]]] mapping target -> list of (source, text)

    # Regex for [text](link)
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

    # 1. Get Master List from SUMMARY.md
    try:
        with open(summary_path, 'r', encoding='utf-8') as f:
            for line in f:
                clean_link = extract_link(line, link_pattern)
                if clean_link:
                    pages.append(clean_link)
                    if clean_link not in backlinks:
                        backlinks[clean_link] = []
    except Exception as e:
        print(f"Error reading SUMMARY.md: {e}")
        return

    print(f"Found {len(pages)} pages in SUMMARY.md. Analyzing backlinks...")

    # 2. Analyze each page
    for page_path in pages:
        relative_path = page_path
        
        # Handle directory links
        full_path = Path(root_dir) / relative_path
        if full_path.is_dir():
            full_path = full_path / "README.md"
        
        if full_path.exists():
            try:
                content = full_path.read_text(encoding='utf-8').splitlines()
                
                # Get Title
                title = "Unknown Title"
                for line in content:
                    if line.lstrip().startswith('# '):
                        title = line.lstrip()[2:].strip()
                        break
                page_titles[relative_path] = title

                # Find outgoing links
                for line in content:
                    for match in link_pattern.finditer(line):
                        text = match.group(1)
                        link = match.group(2)
                        
                        # Cleanup link
                        if ' "' in link:
                            link = link.split(' "')[0]
                        elif ' ' in link:
                            link = link.split(' ')[0]
                        
                        link = link.strip()
                        
                        if link.startswith(('http', 'mailto:', '#')):
                            continue
                            
                        # Remove anchors/query
                        link = link.split('#')[0].split('?')[0]
                        
                        # Filter to likely markdown/directory links
                        # Logic: if not .md and not ending in /, check extension.
                        if not link.lower().endswith('.md') and not link.endswith('/'):
                            if os.path.splitext(link)[1]: # has other extension
                                continue

                        # Resolve path relative to current file
                        current_dir = os.path.dirname(relative_path)
                        # We need to resolve relative to root, then calculate relative path from root
                        # abs path of target
                        target_abs = (Path(root_dir) / current_dir / link).resolve()
                        
                        try:
                            # Verify target is within root
                            if not str(target_abs).startswith(str(Path(root_dir).resolve())):
                                continue
                                
                            target_relative = target_abs.relative_to(Path(root_dir).resolve()).as_posix()
                            
                            # Normalize directory links
                            if target_relative.endswith('/'):
                                target_relative = target_relative.rstrip('/')
                                
                            if target_relative in backlinks:
                                backlinks[target_relative].append((relative_path, text))
                        except ValueError:
                            # Path resolution failed (e.g. outside of root?)
                            continue

            except Exception as e:
                # print(f"Error processing {relative_path}: {e}")
                page_titles[relative_path] = "Error reading file"
        else:
            page_titles[relative_path] = "File not found"

    # 3. Write Output
    output_lines = []
    for page in pages:
        title = page_titles.get(page, "Unknown")
        output_lines.append(f"{page} - {title}")
        
        if page in backlinks and backlinks[page]:
            output_lines.append("  Used by:")
            for source, text in backlinks[page]:
                output_lines.append(f"    - {source} ({text})")

    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            print(f"List written to {output_path}")
        except Exception as e:
            print(f"Error writing output: {e}")
    else:
        for line in output_lines:
            print(line)

if __name__ == "__main__":
    root_dir = parse_arg(sys.argv, '--root')
    output_file = parse_arg(sys.argv, '--output')
    
    if not root_dir:
        # Try to find SUMMARY.md
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
        
    if not output_file:
        output_file = str(Path(root_dir) / 'scripts-output' / 'pages_list.txt')
        
    list_pages(root_dir, output_file)
