# Writing a guide

This article explains how to add a guide to the pretix documentation.

## Prerequisites

Writing a guide requires a working [development environment](development-environment.md).
A general overview of the proper [formatting](formatting.md), [language](language.md) and [best practices](index.md) is helpful.

## General usage

This section describes how to make a basic contribution to the pretix documentation.
This involves the following steps:

 - creating a new branch
 - finding the appropriate directory
 - copying the template
 - writing the guide

This section guides you through those steps in detail.

### Creating a new branch

Before you make any edits to the pretix documentation, you need to create a new branch.
In order to do so, open a terminal on your computer.
Run the following command to check out the main branch:

```
git checkout main
```

To create a new branch named `badge-layout-editor`, run the following command:

```
git checkout -b badge-layout-editor
```

!!! Note
    The above instructions apply if you want to base your new branch on the main branch of the pretix-docs repository.
    This is appropriate for all but a few exceptions.
    Check out the branch from which you want to create a new branch.

### Finding the appropriate directory

All guides are in the directory `docs/guides`.
Try to find the appropriate subdirectory for your new guide.
For instance, if your guide describes a plugin that integrates with an external service, place it in `docs/guides/integrations`
If your guide does not fit into any of the subdirectories, place it in `docs/guides`.

Create a new file with the `.md` file extension.
Name it in lower case.
Use a hyphen-minus `-` to separate words.
For instance, if you are writing a guide on the badge layout editor, name the file `badge-layout-editor.md`.

### Copying the template

Copy the contents of the guide template into your new file.
You can find the template in the root directory of this repository at `template-guides.md`.

Replace the first line of the file in sentence with the title of your article.
Use the markdown title formatting and sentence-style capitalization, for instance:

```
# Badge layout editor
```

