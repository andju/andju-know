"""
Custom macros for MkDocs-Macros.

Defines Jinja macros used within Markdown pages to build automatic,
folder-based tables of contents. Loaded by mkdocs-macros-plugin as
configured via the `module_name` option in mkdocs.yml.
"""

import re

from mkdocs.utils import normalize_url


def define_env(env):
    """
    Register custom macros with the mkdocs-macros-plugin environment.

    Args:
        env: The mkdocs-macros-plugin environment object, exposing the
            `@env.macro` decorator (among others) used to register
            functions as callable macros in Markdown pages.
    """

    def resolve_title(item):
        """
        Get a page's title, even if MkDocs hasn't rendered it yet.

        Args:
            item: A MkDocs Page object.

        Returns:
            The page's title as a string, falling back to a title-cased
            version of the filename if no heading is found.
        """
        if item.title:
            return item.title
        try:
            with open(item.file.abs_src_path, encoding="utf-8") as f:
                for line in f:
                    match = re.match(r"^#\s+(.+)", line)
                    if match:
                        return match.group(1).strip()
        except OSError:
            pass
        return item.file.name.replace("-", " ").replace("_", " ").title()

    def resolve_url(item, page):
        """
        Convert a page's root-relative URL to one relative to `page`.

        `item.url` is relative to the site root (e.g. 'a/b/c/'). Embedding
        that directly as a link on another page bypasses MkDocs' own
        link-resolution, causing the browser to resolve it relative to the
        *current* page instead of the site root — duplicating path
        segments. `normalize_url` performs the same relative-path
        conversion MkDocs uses internally for its own generated links.

        Args:
            item: A MkDocs Page object being linked to.
            page: The current MkDocs page object the link appears on.

        Returns:
            A URL string correctly relative to the current page.
        """
        return normalize_url(item.url, page=page)

    def first_page(item):
        """
        Resolve a navigation item to its first linkable page.

        Args:
            item: A MkDocs navigation object (Page, Section, or Link).

        Returns:
            The first Page object found by descending into nested
            sections, or None if a section has no children.
        """
        while item.is_section:
            if not item.children:
                return None
            item = item.children[0]
        return item

    @env.macro
    def toc(page, navigation):
        """
        Build a markdown list of links for the current index page.

        Args:
            page: The current MkDocs page object (the `page` variable).
            navigation: The site's navigation object (the `navigation`
                variable).

        Returns:
            A markdown-formatted bullet list of links as a string.
        """
        items = page.parent.children if page.parent else navigation.items
        lines = []
        for item in items:
            if item.is_page and item != page:
                url = resolve_url(item, page)
                lines.append(f"- [{resolve_title(item)}]({url})")
            elif item.is_section:
                target = first_page(item)
                url = resolve_url(target, page) if target else "#"
                lines.append(f"- [{resolve_title(item)}]({url})")
        return "\n".join(lines)
