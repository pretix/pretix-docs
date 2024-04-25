from __future__ import annotations

import posixpath
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match

def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):

    # Replace callback
    def replace(match: Match):
        return f'<span class="typo-btn">{match.group(1)}</span>'

    # Find and replace all external asset URLs in current page
    return re.sub(
        r":btn:([^:]+):",
        replace, markdown, flags = re.I
    )
