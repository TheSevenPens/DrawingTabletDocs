import os
import re
from dataclasses import dataclass, field
from pathlib import Path

# Regex for [text](link)
LINK_PATTERN = re.compile(r'\[(.*?)\]\((.*?)\)')


@dataclass
class BackLink:
    source: str  # relative path of the page containing the link
    text: str    # the link text used


@dataclass
class PageInfo:
    path: str
    title: str
    backlinks: list = field(default_factory=list)  # list of BackLink


class GitBookDocs:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def extract_link(self, line, pattern=LINK_PATTERN):
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

    def get_page_title(self, content_lines):
        """Return the first H1 heading text from a list of lines, or 'Unknown Title'."""
        for line in content_lines:
            if line.lstrip().startswith('# '):
                return line.lstrip()[2:].strip()
        return "Unknown Title"

    def get_outgoing_internal_links(self, content_lines, relative_path):
        """Yield (target_relative, link_text) for each internal link found in content_lines.

        Links are resolved relative to relative_path inside root_dir. Only links
        that stay within root_dir and point to markdown/directory targets are yielded.
        """
        current_dir = os.path.dirname(relative_path)
        root_resolved = Path(self.root_dir).resolve()

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

                target_abs = (Path(self.root_dir) / current_dir / link).resolve()

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

    def get_summary_pages(self):
        """Return a list of relative page paths from SUMMARY.md, or raise on error."""
        summary_path = Path(self.root_dir) / 'SUMMARY.md'
        if not summary_path.exists():
            raise FileNotFoundError(f"SUMMARY.md not found at {summary_path}")

        pages = []
        with open(summary_path, 'r', encoding='utf-8') as f:
            for line in f:
                clean_link = self.extract_link(line)
                if clean_link:
                    pages.append(clean_link)
        return pages

    def resolve_page_path(self, relative_path):
        """Resolve a page's relative path to a full filesystem path.

        Directory paths are resolved to their README.md.
        Returns a Path object (which may not exist).
        """
        full_path = Path(self.root_dir) / relative_path
        if full_path.is_dir():
            full_path = full_path / "README.md"
        return full_path

    def list_pages(self):
        """Return a list of PageInfo for all pages in SUMMARY.md order.

        Each PageInfo contains the page path, title, and backlinks from other pages.
        """
        paths = self.get_summary_pages()

        page_info = {path: PageInfo(path=path, title='', backlinks=[]) for path in paths}

        for relative_path in paths:
            full_path = self.resolve_page_path(relative_path)

            if full_path.exists():
                try:
                    content = full_path.read_text(encoding='utf-8').splitlines()
                    page_info[relative_path].title = self.get_page_title(content)

                    for target_relative, text in self.get_outgoing_internal_links(content, relative_path):
                        if target_relative in page_info:
                            page_info[target_relative].backlinks.append(BackLink(source=relative_path, text=text))

                except Exception:
                    page_info[relative_path].title = "Error reading file"
            else:
                page_info[relative_path].title = "File not found"

        return [page_info[path] for path in paths]
