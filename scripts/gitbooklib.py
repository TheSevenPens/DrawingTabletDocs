import os
import re
from pathlib import Path

# Regex for [text](link)
LINK_PATTERN = re.compile(r'\[(.*?)\]\((.*?)\)')


def extract_link(line, pattern=LINK_PATTERN):
    """Extract and clean an internal markdown link from a line.

    Returns the cleaned relative path (no anchor/query), or None if the line
    has no link or the link is external.
    """
    match = pattern.search(line)
    if match:
        # Group 2 is the link part in regex [text](link)
        raw_link = match.group(2)
        clean_link = raw_link.strip()

        if clean_link.startswith('<') and clean_link.endswith('>'):
            clean_link = clean_link[1:-1]

        if ' "' in clean_link:
            clean_link = clean_link.split(' "')[0]
        elif ' ' in clean_link:
            clean_link = clean_link.split(' ')[0]

        clean_link = clean_link.strip()

        if clean_link.startswith(('http', 'ftp', 'mailto:')):
            return None

        return clean_link.split('#')[0].split('?')[0]
    return None


def get_page_title(content_lines):
    """Return the first H1 heading text from a list of lines, or 'Unknown Title'."""
    for line in content_lines:
        if line.lstrip().startswith('# '):
            return line.lstrip()[2:].strip()
    return "Unknown Title"


def get_outgoing_internal_links(content_lines, relative_path, root_dir):
    """Yield (target_relative, link_text) for each internal link found in content_lines.

    Links are resolved relative to relative_path inside root_dir. Only links
    that stay within root_dir and point to markdown/directory targets are yielded.
    """
    current_dir = os.path.dirname(relative_path)
    root_resolved = Path(root_dir).resolve()

    for line in content_lines:
        for match in LINK_PATTERN.finditer(line):
            text = match.group(1)
            link = match.group(2)

            # Cleanup link
            if ' "' in link:
                link = link.split(' "')[0]
            elif ' ' in link:
                link = link.split(' ')[0]

            link = link.strip()

            if link.startswith(('http', 'mailto:', '#')):
                continue

            # Remove anchors/query
            link = link.split('#')[0].split('?')[0]

            # Filter to likely markdown/directory links
            if not link.lower().endswith('.md') and not link.endswith('/'):
                if os.path.splitext(link)[1]:  # has other extension
                    continue

            target_abs = (Path(root_dir) / current_dir / link).resolve()

            try:
                if not str(target_abs).startswith(str(root_resolved)):
                    continue

                target_relative = target_abs.relative_to(root_resolved).as_posix()

                # Normalize directory links
                if target_relative.endswith('/'):
                    target_relative = target_relative.rstrip('/')

                yield target_relative, text
            except ValueError:
                continue


def get_summary_pages(root_dir):
    """Return a list of relative page paths from SUMMARY.md, or raise on error."""
    summary_path = Path(root_dir) / 'SUMMARY.md'
    if not summary_path.exists():
        raise FileNotFoundError(f"SUMMARY.md not found at {summary_path}")

    pages = []
    with open(summary_path, 'r', encoding='utf-8') as f:
        for line in f:
            clean_link = extract_link(line)
            if clean_link:
                pages.append(clean_link)
    return pages


def resolve_page_path(root_dir, relative_path):
    """Resolve a page's relative path to a full filesystem path.

    Directory paths are resolved to their README.md.
    Returns a Path object (which may not exist).
    """
    full_path = Path(root_dir) / relative_path
    if full_path.is_dir():
        full_path = full_path / "README.md"
    return full_path
