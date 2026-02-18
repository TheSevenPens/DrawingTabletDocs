import os
import re
from pathlib import Path
import sys

def list_pages(root_dir, output_file=None):
    root_path = Path(root_dir).resolve()
    summary_path = root_path / 'SUMMARY.md'
    
    if not summary_path.exists():
        print(f"Error: SUMMARY.md not found at {summary_path}")
        return

    # Regex to capture the link part [text](link "title")
    # We capture the content inside ()
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    
    pages = []
    
    try:
        content = summary_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading SUMMARY.md: {e}")
        return

    for line in content.splitlines():
        match = link_pattern.search(line)
        if match:
            raw_link = match.group(1)
            # Clean up the link (remove title, spaces)
            # Link might be: path/to/file.md "Title"
            # Or <path/to/file.md>
            
            clean_link = raw_link.strip()
            
            if clean_link.startswith('<') and clean_link.endswith('>'):
                clean_link = clean_link[1:-1]
            
            # Split by space or quote to remove title
            if ' "' in clean_link:
                clean_link = clean_link.split(' "')[0]
            elif " '" in clean_link:
                clean_link = clean_link.split(" '")[0]
            elif ' ' in clean_link:
                clean_link = clean_link.split(' ')[0]
                
            clean_link = clean_link.strip()
            
            # We only care about md files in the repo, usually relative paths
            # Ignore external links
            if clean_link.startswith(('http:', 'https:', 'ftp:', 'mailto:')):
                continue
                
            # Remove query params or anchors
            clean_link = clean_link.split('#')[0].split('?')[0]
            
            if clean_link:
                pages.append(clean_link)

    # Output
    print(f"Found {len(pages)} pages in SUMMARY.md.")
    
    if output_file:
        output_path = Path(output_file)
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                for page in pages:
                    f.write(page + '\n')
            print(f"List written to {output_path}")
        except Exception as e:
            print(f"Error writing output to {output_path}: {e}")
    else:
        for page in pages:
            print(page)

if __name__ == "__main__":
    # Default to the parent directory of this script (repository root)
    root_dir = Path(__file__).resolve().parent.parent
    
    # Setup output
    output_dir = root_dir / 'scripts-output'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'pages_list.txt'
    
    list_pages(root_dir, output_file)
