import sys
from pathlib import Path

from gitbooklib import GitBookDocs


def parse_arg(args, key):
    try:
        idx = args.index(key)
        if idx + 1 < len(args):
            return args[idx + 1]
    except ValueError:
        pass
    return None


if __name__ == "__main__":
    root_dir = parse_arg(sys.argv, '--root')
    output_file = parse_arg(sys.argv, '--output')

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

    if not output_file:
        output_file = str(Path(root_dir) / 'scripts-output' / 'pages_list.txt')

    pages = GitBookDocs(root_dir).list_pages()

    print(f"Found {len(pages)} pages in SUMMARY.md.")

    output_lines = []
    for page in pages:
        output_lines.append(f"Path:  {page.path}")
        output_lines.append(f"Title: {page.title}")
        if page.backlinks:
            output_lines.append("  Used by:")
            for backlink in page.backlinks:
                output_lines.append(f"    - {backlink.source} ({backlink.text})")
        output_lines.append("")

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
