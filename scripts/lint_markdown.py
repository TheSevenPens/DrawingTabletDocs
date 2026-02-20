import os
import glob
import re
import sys

def lint_markdown(base_dir):
    md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)
    
    # Define our linting rules
    
    # We will use regex but also some manual checking for parens
    link_pattern = re.compile(r'(\\?)\[(.*?)\]\((.*?)\)(\)*)(\s*\]?)')
    # prefix [ text ] ( url ) suffix_parens suffix_brackets
    
    issues_found = 0
    
    # Write output to stdout, but we use utf-8 encoding for sys.stdout if we can,
    # or just write out to a file if provided.
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for i, line in enumerate(lines):
                line_issues = []
                
                # Check for double opening bracket before a link `[[text](url)`
                double_open_matches = re.finditer(r'\[\[(.*?)\]\((.*?)\)', line)
                for m in double_open_matches:
                    line_issues.append(('double_opening_bracket', m.group(0)))
                
                for match in link_pattern.finditer(line):
                    prefix = match.group(1)
                    url = match.group(3)
                    suffix_parens = match.group(4)
                    suffix_brackets = match.group(5)
                    
                    # 1. Escaped bracket
                    if prefix == '\\':
                        line_issues.append(('escaped_bracket', match.group(0)))
                        
                    # 2. Extra closing bracket
                    if ']' in suffix_brackets:
                        line_issues.append(('extra_closing_bracket', match.group(0)))
                        
                    # 3. Double closing paren 
                    # If there's an extra paren at the end, let's see if the URL actually has an unclosed open paren
                    if suffix_parens:
                        # count parens in url
                        open_parens = url.count('(')
                        close_parens = url.count(')')
                        extra_parens = len(suffix_parens)
                        if open_parens != (close_parens + extra_parens):
                            # It's truly malformed
                            line_issues.append(('double_closing_paren', match.group(0)))
                            
                if line_issues:
                    rel_path = os.path.relpath(md_file, base_dir)
                    print(f"{rel_path}:{i+1}")
                    for rule_name, match in line_issues:
                        print(f"  [{rule_name}] -> {match}")
                    issues_found += len(line_issues)
                        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            
    print(f"\nLinting complete. Found {issues_found} potential issues.")
    return issues_found

if __name__ == "__main__":
    base_dir = r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs"
    # You can also use sys.argv to pass a directory if preferred
    if len(sys.argv) > 1:
        base_dir = os.path.abspath(sys.argv[1])
        
    print(f"Linting markdown files in: {base_dir}\n")
    issues = lint_markdown(base_dir)
    sys.exit(1 if issues > 0 else 0)
