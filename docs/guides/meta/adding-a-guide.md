# Adding a guide

This article explains how to add a guide to the pretix documentation.
Most of the steps described here also apply to other types of contributions.
If you want to make a contribution other than a guide or a translation, contact the team first.
It is also a good idea to contact the team if you want to contribute a guide.

## Prerequisites

Writing a guide requires a working [development environment](development-environment.md).
A general overview of the proper [formatting](formatting.md), [language](language.md) and [best practices](index.md) is helpful.

## How to

This section describes how to make a basic contribution to the pretix documentation.
This involves the following steps:

 - [creating a new branch](#creating-a-new-branch)
 - [finding the appropriate directory](#finding-the-appropriate-directory)
 - [using the template](#using-the-template)
 - [writing the guide](#writing-the-guide)
 - [creating a pull request](#creating-a-pull-request-for-review)

This section guides you through those steps in detail.

### Creating a new branch

Before you make any edits to the pretix documentation, you need to create a new branch.
There is more than one way to do this.

If you want to use the Git CLI to create a new branch, open a terminal on your computer.
Check out the branch from which you want to create a new branch.
In all but a few exceptions, that is going to be the main branch.

Run the following command to check out the main branch:

```
git checkout main
```

In order to create a new branch named `badge-layout-editor` and check it out, run the following command:

```
git checkout -b badge-layout-editor
```

Alternatively, use your IDE or your preferred Git client to create a new branch.

### Finding the appropriate directory

All guides are in the directory `docs/guides`.
Try to find the appropriate subdirectory for your new guide.
For instance, if your guide describes a plugin that integrates with an external service, place it in `docs/guides/integrations`.
If your guide does not fit into any of the subdirectories, place it in `docs/guides`.

Create a new file with the `.md` file extension.
Name it in lower case.
Use a hyphen-minus `-` to separate words.
For instance, if you are writing a guide on the badge layout editor, name the file `badge-layout-editor.md`.

### Using the template

Copy the contents of the guide template into your new file.
You can find the template in the root directory of this repository at `template-guides.md`.

Replace the first line of the file in sentence with the title of your article.
Use the markdown title formatting and sentence-style capitalization, for instance:

```
# Badge layout editor
```

The template contains questions and instructions as placeholder text under each headline.
Answer those questions in the respective section in your text.

If you do not have any content for the sections "Troubleshooting", "Further information", and "See also", remove those sections.
Do **not** remove the sections "Prerequisites" or "How to".
Do **not** remove the title section either.

If the "How to" section becomes very long, separate it into "General usage" and "Advanced usage".
For an example of this article structure, see [pretixSCAN (Android)](../pretixscan/android.md).

If you are describing the setup of a feature and then its applications, separate the "How to" section into "General usage" and "Applications".
For an example of this article structure, see [Vouchers](../vouchers.md).

### Writing the guide

Research the subject that you want to cover and write your guide.
For guidance on how to collect and record the relevant information, refer to the article on [best practices](index.md).
For instructions on how to format your text, see [formatting](formatting.md).
For information on terminology, orthography, and punctuation, see [language](language.md).

### Creating a pull request for review

Once you have finished writing the guide, submit a pull request.
There is more than once way to do this.
In order to submit a pull request using the GitHub web interface, open your browser.
Log into your GitHub account.
Navigate to the `pretix-docs` repository.
Open the [Pull requests](https://github.com/pretix/pretix-docs/pulls) tab.

Create a new pull request.
Select the branch you created under [Creating a new branch](#creating-a-new-branch).
In the example above, the name of that branch is `branch-layout-editor`.
Provide an informative title and description.

You do not have to submit a draft pull request.
You can submit a pull request right away.
Once you have done so, the pretix documentation team will notice your contribution, review it, and eventually merge it into the main branch.