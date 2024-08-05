from __future__ import annotations

import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from re import Match


def i18n(language, strings):
    if language in strings:
        return strings[language]
    if "en" in strings:
        return strings[language]
    return list(strings.values())[0]


def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):
    language = config.theme["language"]

    # Replace callback
    def replace_btn(match: Match):
        return f'<span class="typo-btn">{match.group(1)}</span>'

    def replace_btn_mdi(match: Match):
        return f'<span class="typo-btn">:{match.group(1)}: {match.group(2)}</span>'

    def replace_navpath(match: Match):
        parts = match.group(1).split("→")
        sr_text = i18n(language, {
            "de": "dann",
            "en": "then"
        })
        sr_prefix = i18n(language, {
            "de": "Navigationspfad",
            "en": "navigation path"
        })
        title = 'title="' + i18n(language, {
            "de": "Starten Sie, indem Sie zu diesem Element navigieren",
            "en": "Start by navigating to this element, then go from here"
        }) + '"'
        return f'<span class="sr-only">{sr_prefix}</span>' + (f' :fontawesome-solid-arrow-right: <span class="sr-only">{sr_text}</span> '.join(
            f'<span class="{"typo-navlayer" if i == 0 else "typo-btn"}" {title if i == 0 else ""}>{p.strip()}</span>' for i, p in enumerate(parts)
        ))

    def replace_rootnavpath(match: Match):
        parts = match.group(1).split("→")
        sr_text = i18n(language, {
            "de": "dann",
            "en": "then"
        })
        sr_prefix = i18n(language, {
            "de": "Navigationspfad startend auf dem Dashboard",
            "en": "navigation path starting at the dashboard"
        })
        logo_hover = i18n(language, {
            "de": "Beginnen Sie auf der Backend-Startseite (Klick aufs Logo links oben)",
            "en": "Start at our backend home page (click on the logo in the top left)"
        })
        return f'<span class="sr-only">{sr_prefix}</span>' + (f' :fontawesome-solid-arrow-right: <span class="sr-only">{sr_text}</span> '.join([
            f'<span title="{logo_hover}">:i-pretix:</span>'
        ] + [
            f'<span class="typo-btn">{p.strip()}</span>' for i, p in enumerate(parts)
        ]))

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
        r":navpath:(([^:]|:[a-z0-9-]+:)*):",
        replace_navpath, markdown, flags = re.I
    )
    markdown = re.sub(
        r":rootnavpath:(([^:]|:[a-z0-9-]+:)*):",
        replace_rootnavpath, markdown, flags = re.I
    )

    return markdown
