# Inspired by mkdocs-material
# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>
# Adjusted
# Copyright (c) 2025 pretix GmbH

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

import json
import posixpath
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match


SHORTLINK_PREFIX = 'link/'
DEFAULT_LANGUAGE = 'en'

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

def on_page_content(
        markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):
    language = config.theme["language"]

    # Replace callback
    def replace(match: Match):
        if not hasattr(files, '_permalink_used_link_ids'):
            files._permalink_used_link_ids = set()
        if not hasattr(config, '_permalink_multilang'):
            config._permalink_multilang = dict()

        (headid, linkid,) = match.groups()

        # prevent duplicate link ids
        if linkid in files._permalink_used_link_ids:
            raise ValueError(f'Duplicate permalink id {linkid}')
        files._permalink_used_link_ids.add(linkid)

        # get current language via mkdocs-static-i18n I18nFiles object
        current_lang = files.plugin.current_language

        # build target url and store per-language
        target_url = config.site_url + page.url + '#' + headid
        if linkid not in config._permalink_multilang:
            config._permalink_multilang[linkid] = dict()
        config._permalink_multilang[linkid][current_lang] = target_url

        # generate redirect page from template
        files.append(File.generated(
            config,
            src_uri=SHORTLINK_PREFIX + linkid + '/index.html',
            content=generate_html_redirect(config._permalink_multilang[linkid])
        ))

        print('Generated short link: ' + config.site_url + SHORTLINK_PREFIX + linkid + '/  -->  ', config._permalink_multilang[linkid])
        return match.group(0)

    # Handle forwarding link targets
    return re.sub(
        r'<h[1-6] id="([^"]+)">.*<!-- permalink:(\w+) -->.*</h[1-6]>',
        replace, markdown, flags=re.I | re.M
    )


def generate_html_redirect(target_urls):
  return f"""
  <!doctype html>
  <html lang="en">
  <head>
      <meta charset="utf-8">
      <title>Redirecting...</title>
      <link rel="canonical" href="{target_urls.get(DEFAULT_LANGUAGE)}">
      <script>
      var target_urls = {json.dumps(target_urls)};
      function get_url() {{
        for (var key in target_urls)
          if (navigator.language.startsWith(key))
            return target_urls[key];
        return target_urls.en;
      }}
      location.href = get_url();
      </script>
      <meta http-equiv="refresh" content="0; url={target_urls.get(DEFAULT_LANGUAGE)}">
  </head>
  <body>
  <font face=sans-serif>You're being redirected to the pretix documentation. <a href="{target_urls.get(DEFAULT_LANGUAGE)}">Click here if the redirect doesn't work.</a>.</font>
  </body>
  </html>
  """
