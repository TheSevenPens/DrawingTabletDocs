import sys
from pathlib import Path

from gitbooklib import (
    get_summary_pages,
    get_page_title,
    get_outgoing_internal_links,
    resolve_page_path,
)


def parse_arg(args, key):
    try:
        idx = args.index(key)
        if idx + 1 < len(args):
            return args[idx + 1]
    except ValueError:
        pass
    return None


def list_pages(root_dir, output_file):
    try:
        pages = get_summary_pages(root_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    page_titles = {}
    backlinks = {page: [] for page in pages}  # target -> list of (source, text)

    print(f"Found {len(pages)} pages in SUMMARY.md. Analyzing backlinks...")

    # Analyze each page
    for relative_path in pages:
        full_path = resolve_page_path(root_dir, relative_path)

        if full_path.exists():
            try:
                content = full_path.read_text(encoding='utf-8').splitlines()
                page_titles[relative_path] = get_page_title(content)

                for target_relative, text in get_outgoing_internal_links(content, relative_path, root_dir):
                    if target_relative in backlinks:
                        backlinks[target_relative].append((relative_path, text))

            except Exception:
                page_titles[relative_path] = "Error reading file"
        else:
            page_titles[relative_path] = "File not found"

    # Write output
    output_lines = []
    for page in pages:
        title = page_titles.get(page, "Unknown")
        output_lines.append(f"{page} - {title}")

        if backlinks[page]:
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
