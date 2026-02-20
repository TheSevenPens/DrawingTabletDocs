import os
import glob
import re

base_dir = r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs"
md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

# Pattern: match \[ text ]( url ) optional-spaces ]
pattern = re.compile(r'\\\[(.*?)\]\((.*?)\)\s*\]')

total_files_modified = 0
total_replacements = 0

for md_file in md_files:
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, count = pattern.subn(r'[\1](\2)', content)
        
        if count > 0:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {count} links in: {os.path.relpath(md_file, base_dir)}")
            total_files_modified += 1
            total_replacements += count
            
    except Exception as e:
        print(f"Error processing {md_file}: {e}")

print(f"\nDone! Fixed {total_replacements} links across {total_files_modified} files.")
