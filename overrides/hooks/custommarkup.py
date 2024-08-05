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

    def replace_navpath(match: Match):
        parts = match.group(1).split("→")
        return ' :fontawesome-solid-arrow-right: <span class="sr-only">→</span> '.join(
            f'<span class="{"typo-navlayer" if i == 0 else "typo-btn"}">{p.strip()}</span>' for i, p in enumerate(parts)
        )
        return f'<span class="typo-navlayer">{match.group(1)}</span>'

    def replace_placeholder(match: Match):
        return f'<span class="typo-placeholder">{match.group(1)}</span>'

    markdown = re.sub(
        r":placeholder:([^:]*):",
        replace_placeholder, markdown, flags = re.I
    )
    markdown = re.sub(
        r":btn:([^:]+):",
        replace_btn, markdown, flags = re.I
    )
    markdown = re.sub(
        r":btn-icon:([^:]+):([^:]*):",
        replace_btn_mdi, markdown, flags = re.I
    )
    markdown = re.sub(
        r":navpath:([^:]*):",
        replace_navpath, markdown, flags = re.I
    )

    return markdown
