import os, glob

base_dir = r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs"
files = glob.glob(os.path.join(base_dir, "**", "7p*.md"), recursive=True)

all_md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

print(f"Found {len(files)} files starting with '7p'")

for f in files:
    filename = os.path.basename(f)
    print(f"[{filename}]")
    found = False
    for md in all_md_files:
        try:
            with open(md, 'r', encoding='utf-8') as file:
                content = file.read()
                if filename in content:
                    # check if it's referenced in a different file
                    if os.path.abspath(md) != os.path.abspath(f):
                        print(f"  -> Referenced in: {os.path.relpath(md, base_dir)}")
                        found = True
        except Exception as e:
            pass
    if not found:
        print(f"  -> NOT referenced in any other md file.")
