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
        output_file = str(Path(root_dir) / 'scripts-output' / 'links_list.txt')

    links = list(GitBookDocs(root_dir).get_all_links())

    print(f"Found {len(links)} links across {len({l.source for l in links})} pages.")

    # Group by source page
    by_source = {}
    for link in links:
        by_source.setdefault(link.source, []).append(link)

    output_lines = []
    for source, page_links in by_source.items():
        output_lines.append(f"Source: {source}")
        for link in page_links:
            if link.is_external:
                output_lines.append(f"  [external] [{link.text}] -> {link.url} ({link.domain})")
            else:
                output_lines.append(f"  [internal] [{link.text}] -> {link.url}")
        output_lines.append("")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
        print(f"List written to {output_path}")
    except Exception as e:
        print(f"Error writing output: {e}")
