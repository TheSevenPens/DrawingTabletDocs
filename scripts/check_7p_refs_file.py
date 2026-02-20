import os, glob

base_dir = r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs"
files = glob.glob(os.path.join(base_dir, "**", "7p*.md"), recursive=True)

all_md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

with open(r"c:\Users\seven\Documents\GitHub\DrawingTabletDocs\log_7p.txt", "w", encoding="utf-8") as out:
    out.write(f"Found {len(files)} files starting with '7p'\n")
    for f in files:
        filename = os.path.basename(f)
        out.write(f"[{filename}]\n")
        found = False
        for md in all_md_files:
            try:
                with open(md, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if filename in content:
                        if os.path.abspath(md) != os.path.abspath(f):
                            out.write(f"  -> Referenced in: {os.path.relpath(md, base_dir).replace(os.sep, '/')}\n")
                            found = True
            except Exception as e:
                pass
        if not found:
            out.write(f"  -> NOT referenced in any other md file.\n")
