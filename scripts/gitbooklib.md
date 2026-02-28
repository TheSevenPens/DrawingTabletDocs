# gitbooklib.py

Shared library used by the scripts in this folder. Provides common utilities for parsing GitBook markdown content, resolving page paths, and extracting links.

---

## Constants

### `LINK_PATTERN`

A compiled regex matching standard markdown links of the form `[text](link)`.

---

## `BackLink`

Dataclass representing a single inbound link to a page.

| Field | Type | Description |
|---|---|---|
| `source` | `str` | Relative path of the page containing the link |
| `text` | `str` | The link text used at the source |

---

## `PageInfo`

Dataclass representing a single page from `SUMMARY.md`.

| Field | Type | Description |
|---|---|---|
| `path` | `str` | Relative path to the page as it appears in `SUMMARY.md` |
| `title` | `str` | Text of the page's first H1 heading, `"File not found"`, or `"Error reading file"` |
| `backlinks` | `list[BackLink]` | All other pages that link to this one |

---

## `GitBookDocs`

Main class. Instantiate with a `root_dir` and call methods on the instance.

```python
docs = GitBookDocs(root_dir)
```

### `EXCLUDED_DIRS`

Class-level set of directory names skipped during filesystem scans: `.git`, `node_modules`, `scripts`.

---

### `get_all_markdown_files()`

Walks `root_dir` recursively and returns the relative posix paths of all markdown files found, skipping any directory in `EXCLUDED_DIRS`.

**Returns:** `set[str]` — relative posix paths of all `.md` files

---

### `extract_link(line, pattern=LINK_PATTERN)`

Extracts and cleans a single internal markdown link from a line of text.

- Strips angle bracket wrappers (`<link>`)
- Strips inline titles (` "Title"`)
- Strips anchors (`#section`) and query strings (`?param`)
- Returns `None` if no link is found or the link is external (`http`, `ftp`, `mailto:`)

**Returns:** `str | None` — cleaned relative path, or `None`

---

### `get_page_title(content_lines)`

Returns the text of the first H1 heading (`# Heading`) found in a list of lines.

**Returns:** `str` — heading text, or `"Unknown Title"` if no H1 is found

---

### `get_outgoing_internal_links(content_lines, relative_path)`

Yields all internal links found in a page's content, resolved to paths relative to `root_dir`.

- Skips external links (`http`, `mailto:`) and anchor-only links (`#`)
- Skips links with non-markdown extensions
- Resolves links relative to the page's own directory
- Skips links that resolve outside `root_dir`

**Yields:** `(target_relative: str, link_text: str)` tuples

---

### `get_summary_pages()`

Parses `SUMMARY.md` and returns a list of all linked page paths.

- Raises `FileNotFoundError` if `SUMMARY.md` does not exist

**Returns:** `list[str]` — relative page paths in the order they appear in `SUMMARY.md`

---

### `resolve_page_path(relative_path)`

Resolves a relative page path to a full filesystem path. Directory paths are resolved to their `README.md`.

**Returns:** `Path` — absolute path (may not exist on disk)

---

### `list_pages()`

Returns all pages from `SUMMARY.md` as `PageInfo` objects, with titles and backlinks populated.

**Returns:** `list[PageInfo]` — one entry per page, in `SUMMARY.md` order
