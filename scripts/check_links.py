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

def check_links(root_dir, output_file=None):
    # Redirect print to file if output_file is specified
    original_stdout = sys.stdout
    if output_file:
        f = open(output_file, 'w', encoding='utf-8')
        sys.stdout = f

    try:
        root_path = Path(root_dir).resolve()
        
        # 1. Index all files
        all_files = set()
        print(f"Indexing files in {root_dir}...")
        for root, dirs, files in os.walk(root_path):
            if '.git' in dirs: dirs.remove('.git')
            if 'node_modules' in dirs: dirs.remove('node_modules')
            
            for file in files:
                full_path = Path(root) / file
                # Store absolute path lowercased
                all_files.add(str(full_path.resolve()).lower())

        print(f"Indexed {len(all_files)} files.")

        # 2. Scan markdown files for links
        md_files = []
        for root, dirs, files in os.walk(root_path):
            if '.git' in dirs: dirs.remove('.git')
            if 'node_modules' in dirs: dirs.remove('node_modules')
            
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)

        print(f"Scanning {len(md_files)} markdown files for broken links...")

        # Regex patterns
        # Fix for nested parens in angle brackets: try to match <...> first, then fall back to non-paren characters
        inline_link_pattern = re.compile(r'\[.*?\]\((<[^>]+>|.*?)\)') 
        ref_link_def_pattern = re.compile(r'^\[.*?\]:\s*(.*?)$', re.MULTILINE)
        angle_link_pattern = re.compile(r'(?<!\\)<(.*?)>') # Negative lookbehind for escaped <
        html_img_pattern = re.compile(r'<img\s+[^>]*src=["\'](.*?)["\']', re.IGNORECASE)
        html_href_pattern = re.compile(r'href=["\'](.*?)["\']', re.IGNORECASE)

        broken_links = [] # List of tuples: (source_file, link_text, resolved_path_attempt)

        # Common HTML tags to ignore/exclude from angle bracket matches
        html_tags = {
            'br', 'hr', 'div', '/div', 'span', '/span', 'img', '/img',
            'table', '/table', 'thead', '/thead', 'tbody', '/tbody',
            'tr', '/tr', 'td', '/td', 'th', '/th', 'p', '/p',
            'h1', '/h1', 'h2', '/h2', 'h3', '/h3', 'h4', '/h4', 'h5', '/h5', 'h6', '/h6',
            'b', '/b', 'i', '/i', 'strong', '/strong', 'em', '/em', 'code', '/code', 'pre', '/pre',
            'ul', '/ul', 'ol', '/ol', 'li', '/li', 'blockquote', '/blockquote', 'a', '/a',
            'mark', '/mark', 'figure', '/figure', 'figcaption', '/figcaption',
            'title', '/title', 'sup', '/sup', 'sub', '/sub', 'kbd', '/kbd',
            'script', '/script', 'style', '/style'
        }

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
            except Exception as e:
                print(f"Error reading {md_file}: {e}")
                continue

            links = []
            
            # Handle inline links [text](url "title")
            for match in inline_link_pattern.findall(content):
                url = match.strip()
                if not url:
                    continue
                
                # Check for <url> format which allows spaces
                if url.startswith('<') and '>' in url:
                     # Extract content between first < and next >
                     # This handles cases like [text](<path with spaces>)
                     url = url[1:url.find('>')]
                else:
                    # Standard behavior: split by space or quote
                    if ' "' in url:
                        url = url.split(' "')[0]
                    elif " '" in url:
                        url = url.split(" '")[0]
                    elif ' ' in url: # Fallback for no quotes
                        url = url.split(' ')[0]
                
                links.append(url)

            # Handle reference links
            for match in ref_link_def_pattern.findall(content):
                url = match.strip()
                if not url: continue
                
                if url.startswith('<') and '>' in url:
                     url = url[1:url.find('>')]
                else:
                    if ' "' in url:
                        url = url.split(' "')[0]
                    elif " '" in url:
                        url = url.split(" '")[0]
                    elif ' ' in url:
                        url = url.split(' ')[0]
                links.append(url)

            # Handle angle brackets <url> - carefully
            for match in angle_link_pattern.findall(content):
                candidate = match.strip()
                # If it looks like an HTML tag, skip it
                first_word = candidate.split(' ')[0].lower()
                if first_word in html_tags or first_word.startswith(('!--', 'mark', 'style')):
                    continue
                # If it contains attributes like width=, it's likely HTML
                if '=' in candidate and not '?' in candidate: # ? for query params is ok
                    continue
                links.append(candidate)

            links.extend(html_img_pattern.findall(content))
            links.extend(html_href_pattern.findall(content))

            for link in links:
                original_link = link
                link = link.strip()
                
                # Skip partial matches or empty
                if not link:
                    continue
                
                # Skip anchors only
                if link.startswith('#'):
                    continue

                if link.lower().startswith("mailto:"):
                   continue
                
                # Skip external links
                if link.lower().startswith(('http:', 'https:', 'ftp:', 'tel:', 'onenote:')):
                    continue
                
                # Remove query params and anchors
                link_path = link.split('#')[0].split('?')[0]
                if not link_path:
                    continue

                # Unquote path (handle %20 etc)
                link_path = urllib.parse.unquote(link_path)
                
                # Resolve path
                abs_target = None
                try:
                    if link_path.startswith('/'):
                        # Relative to root
                        abs_target = (root_path / link_path.lstrip('/')).resolve()
                    else:
                        # Relative to current file
                        abs_target = (md_file.parent / link_path).resolve()
                    
                    # Check if exists
                    if str(abs_target).lower() not in all_files:
                        # Double check if it's a directory (rendering README.md implicit?)
                        if abs_target.is_dir():
                             # Check if README.md exists inside
                             if str((abs_target / 'README.md').resolve()).lower() in all_files:
                                 continue
                             if str((abs_target / 'readme.md').resolve()).lower() in all_files:
                                 continue
                        
                        relative_source = md_file.relative_to(root_path)
                        broken_links.append((str(relative_source), original_link, str(abs_target)))

                except Exception as e:
                     # Could be path formatting error
                     try:
                        relative_source = md_file.relative_to(root_path)
                     except:
                        relative_source = md_file
                     broken_links.append((str(relative_source), original_link, f"Error resolving: {e}"))

        print(f"\nFound {len(broken_links)} broken links.")
        
        if broken_links:
            print("\nBroken Links:")
            # Group by file
            current_file = ""
            for source, link, target in sorted(broken_links, key=lambda x: x[0]):
                if source != current_file:
                    print(f"\nFile: {source}")
                    current_file = source
                print(f"  Link: {link}")
                # print(f"    Resolved: {target}")

    finally:
        if output_file:
            sys.stdout = original_stdout
            f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check for broken links in markdown files.')
    parser.add_argument('--root', help='Root directory of the repository', default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument('--output', help='Output file for the report')
    
    args = parser.parse_args()
    
    root_dir = Path(args.root)
    output_file = args.output
    
    if not output_file:
        output_dir = root_dir / 'scripts-output'
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / 'broken_links.txt'
        
    check_links(str(root_dir), str(output_file))
