import os
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

from markdown_it import MarkdownIt


@dataclass
class LinkInfo:
    url: str          # raw href as it appears in the source
    text: str         # link text
    source: str       # relative path of the page containing the link
    is_external: bool # True if the link points outside the docs
    domain: str       # netloc for external links (e.g. "example.com"), '' for internal


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
    EXCLUDED_DIRS = {'.git', 'node_modules', 'scripts'}

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self._md = MarkdownIt()

    def _iter_links(self, tokens):
        """Yield (href, text) tuples for every link in a markdown-it token stream."""
        for token in tokens:
            if not token.children:
                continue
            children = token.children
            for i, child in enumerate(children):
                if child.type == 'link_open':
                    href = (child.attrs or {}).get('href', '')
                    text = ''
                    if i + 1 < len(children) and children[i + 1].type == 'text':
                        text = children[i + 1].content
                    yield href, text

    def get_all_markdown_files(self):
        """Return a set of relative posix paths for all markdown files under root_dir.

        Directories in EXCLUDED_DIRS are skipped entirely.
        """
        root_path = Path(self.root_dir).resolve()
        files = set()
        for root, dirs, filenames in os.walk(root_path):
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS]
            for filename in filenames:
                if filename.endswith('.md'):
                    full_path = Path(root) / filename
                    try:
                        rel_path = full_path.relative_to(root_path)
                        files.add(str(rel_path).replace('\\', '/'))
                    except ValueError:
                        pass
        return files

    def extract_link(self, line):
        """Extract and clean the first internal markdown link from a line.

        Returns the cleaned relative path (no anchor/query), or None if the line
        has no link or the link is external.
        """
        tokens = self._md.parse(line)
        for href, _ in self._iter_links(tokens):
            if href.startswith(('http', 'ftp', 'mailto:')):
                return None
            return href.split('#')[0].split('?')[0]
        return None

    def get_page_title(self, content_lines):
        """Return the first H1 heading text from a list of lines, or 'Unknown Title'."""
        tokens = self._md.parse('\n'.join(content_lines))
        for i, token in enumerate(tokens):
            if token.type == 'heading_open' and token.tag == 'h1':
                if i + 1 < len(tokens) and tokens[i + 1].type == 'inline':
                    return tokens[i + 1].content.strip()
        return "Unknown Title"

    def get_outgoing_internal_links(self, content_lines, relative_path):
        """Yield (target_relative, link_text) for each internal link found in content_lines.

        Links are resolved relative to relative_path inside root_dir. Only links
        that stay within root_dir and point to markdown/directory targets are yielded.
        """
        current_dir = os.path.dirname(relative_path)
        root_resolved = Path(self.root_dir).resolve()

        tokens = self._md.parse('\n'.join(content_lines))
        for href, text in self._iter_links(tokens):
            if href.startswith(('http', 'ftp', 'mailto:', '#')):
                continue

            link = href.split('#')[0].split('?')[0]
            if not link:
                continue

            # Filter to likely markdown/directory links
            if not link.lower().endswith('.md') and not link.endswith('/'):
                if os.path.splitext(link)[1]:  # has other extension
                    continue

            target_abs = (Path(self.root_dir) / current_dir / link).resolve()

            try:
                if not str(target_abs).startswith(str(root_resolved)):
                    continue

                target_relative = target_abs.relative_to(root_resolved).as_posix()

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

    def get_all_links(self):
        """Yield a LinkInfo for every link found across all pages in SUMMARY.md."""
        for relative_path in self.get_summary_pages():
            full_path = self.resolve_page_path(relative_path)
            if not full_path.exists():
                continue

            try:
                content = full_path.read_text(encoding='utf-8').splitlines()
                tokens = self._md.parse('\n'.join(content))

                for href, text in self._iter_links(tokens):
                    if not href:
                        continue

                    is_external = href.startswith(('http://', 'https://', 'ftp://', 'mailto:'))

                    if is_external:
                        if href.startswith('mailto:'):
                            email = href[7:]
                            domain = email.split('@')[-1] if '@' in email else ''
                        else:
                            domain = urlparse(href).netloc
                    else:
                        domain = ''

                    yield LinkInfo(
                        url=href,
                        text=text,
                        source=relative_path,
                        is_external=is_external,
                        domain=domain,
                    )

            except Exception:
                continue
