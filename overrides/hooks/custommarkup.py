from __future__ import annotations

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from re import Match

def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):

    # Replace callback
    def replace_btn(match: Match):
        return f'<span class="typo-btn">{match.group(1)}</span>'

    def replace_btn_mdi(match: Match):
        return f'<span class="typo-btn">:{match.group(1)}: {match.group(2)}</span>'

    markdown = re.sub(
        r":btn:([^:]+):",
        replace_btn, markdown, flags = re.I
    )
    markdown = re.sub(
        r":btn-icon:([^:]+):([^:]*):",
        replace_btn_mdi, markdown, flags = re.I
    )

    return markdown
