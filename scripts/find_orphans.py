import sys
from pathlib import Path

from gitbooklib import GitBookDocs


def find_orphans(root_dir):
    docs = GitBookDocs(root_dir)
    root_path = Path(root_dir).resolve()
    referenced_files = set()

    # 1. Collect all markdown files on disk (excluding scripts and other ignored dirs)
    all_files = docs.get_all_markdown_files()

    # 2. Walk each file and collect referenced targets
    for relative_path in all_files:
        full_path = root_path / relative_path
        try:
            content = full_path.read_text(encoding='utf-8', errors='ignore').splitlines()
        except Exception:
            continue

        for target_relative, _ in docs.get_outgoing_internal_links(content, relative_path):
            if target_relative in all_files:
                referenced_files.add(target_relative)

    # 3. Mark known entry points as referenced
    for ep in ("README.md", "SUMMARY.md", "summary.md", "readme.md"):
        if ep in all_files:
            referenced_files.add(ep)

    # 4. Return unreferenced files, excluding README.md files
    return sorted(
        f for f in all_files
        if f not in referenced_files and not f.lower().endswith("readme.md")
    )


if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent

    orphans = find_orphans(root_dir)

    output_lines = []
    output_lines.append(f"Found {len(orphans)} orphan files:")
    output_lines.extend(orphans)

    output_dir = root_dir / 'scripts-output'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'orphan_files.txt'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    for line in output_lines:
        print(line)

    print(f"Report written to {output_file}")
