# Inspired by mkdocs-material
# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>
# Adjusted
# Copyright (c) 2024 rami.io GmbH

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import annotations

import posixpath
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match


# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# @todo
def on_page_markdown(
        markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):
    # Replace callback
    def replace(match: Match):
        type, args = match.groups()
        args = args.strip()
        if type == "version":
            return _badge_for_version(args, page, files)
        elif type == "plugin":
            return _badge_for_plugin(args, page, files)
        elif type == "enterprise":
            return _badge_for_enterprise(page, files)
        elif type == "hosted":
            return _badge_for_hosted(page, files)
        elif type == "community":
            return _badge_for_community(page, files)
        elif type == "experimental":
            return _badge_for_experimental(page, files)
        else:
            raise RuntimeError(f"Unknown shortcode: {type}")

    # Find and replace all external asset URLs in current page
    return re.sub(
        r"<!-- md:(\w+)(.*?) -->",
        replace, markdown, flags=re.I | re.M
    )


def _badge(icon: str, text: str = "", type: str = "", title: str = ""):
    classes = f"mdx-badge mdx-badge--{type}" if type else "mdx-badge"
    return "".join([
        f"<span class=\"{classes}\" title=\"{title}\">",
        *([f"<span class=\"mdx-badge__icon\">{icon}</span>"] if icon else []),
        *([f"<span class=\"mdx-badge__text\">{text}</span>"] if text else []),
        f"</span>",
    ])


def _badge_for_version(text: str, page: Page, files: Files):
    icon = "material-tag-outline"
    return _badge(
        icon=f":{icon}:",
        text=text,
        type="version",
        title=f"This section applies starting with pretix version {text}",
    )


def _badge_for_experimental(page: Page, files: Files):
    icon = "material-flask-outline"
    return _badge(
        icon=f":{icon}:",
        text="Experimental",
        type="experimental",
        title="This section refers to experimental features that may be changed or removed in the future",
    )


def _badge_for_plugin(text, page: Page, files: Files):
    icon = "material-puzzle"
    return _badge(
        icon=f":{icon}:",
        text="Plugin: " + text,
        type="plugin",
        title="This section requires you to use the plugin " + text,
    )


def _badge_for_enterprise(page: Page, files: Files):
    icon = "material-star"
    return _badge(
        icon=f":{icon}:",
        text="pretix Enterprise",
        type="enterprise",
        title="This section applies if you are using the commercial on-premise edition of pretix.",
    )


def _badge_for_hosted(page: Page, files: Files):
    icon = "material-cloud"
    return _badge(
        icon=f":{icon}:",
        text="pretix Hosted",
        type="hosted",
        title="This section applies if you are using our cloud offering pretix Hosted.",
    )


def _badge_for_community(page: Page, files: Files):
    icon = "material-heart-outline"
    return _badge(
        icon=f":{icon}:",
        text="pretix Community",
        type="community",
        title="This section applies if you are using the open-source edition of pretix.",
    )
