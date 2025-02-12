# pretix-docs

Next-generation user documentation for the pretix ecosystem.

## How to build

Using a recent Python environment, install dependencies with:

    pip install -r requirements.txt

Then, you can build the project with:

    mkdocs serve

And view the local preview at https://127.0.0.1:8000/

## How to work on the project

On the technical side, this is based on [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
so view those pages for in-depth details. A number of plugins are installed that add significant functionality, such as
[i18n](https://github.com/ultrabug/mkdocs-static-i18n), [awesome pages](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) and
[macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/).

### Custom markup

- ``:placeholder:ABC:`` Typographically show that something is to be replaced by the user
- ``:btn:Click me:`` Typographically indicate a clickable UI element
- ``:btn-icon:fa3-eye:Click me:`` Typographically indicate a clickable UI element with an icon and text
- ``:btn-icon:fa3-eye::`` Typographically indicate a clickable UI element with only an icon
- ``:navpath:A:B:C:D:`` Typographically indicate a navigation path where the first element starts on a dynamic spot like "Your Event"
- ``:rootnavpath:A:B:C:D`` Typographically indicate a navigation path where the first element is the pretix logo that refers to the backend start page
- ``<!-- md:community -->`` Feature only on pretix Community
- ``<!-- md:hosted -->`` Feature only on pretix Hosted
- ``<!-- md:enterprise -->`` Feature requires pretix Enterprise
- ``<!-- md:plugin XY -->`` Feature requires plugin XY
- ``<!-- md:experimental -->`` Feature is experimental
