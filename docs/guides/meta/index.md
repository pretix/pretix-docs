# Contributing to the docs

This section of the documentation explains how the documentation itself works, how we wrote it, and how to contribute to it.
If you want to contribute to the pretix documentation, then you should read this article and the following articles:

 - You can find information on how to set up your development environment under [Development environment](development-environment.md).

 - You can find information on how to contribute an article to the pretix docs under [Adding a guide](adding-a-guide.md).

 - You can find information on terminology, orthography, and punctuation under [Language](language.md).

 - You can find information on how to format your text using Markdown, MkDocs, and our customizations under [Formatting](formatting.md).

This article contains general information on how to contribute to the documentation and what to avoid in the process.

## Prerequisites

This article contains basic information on how to contribute to the docs.
There are no further prerequisites.

## How to

This article describes [best practices](#best-practices-what-to-do-when-writing-documentation-for-pretix) as well as [what not to do](#what-not-to-do-when-writing-documentation-for-pretix) when contributing to the docs.

### Best Practices: What to do when writing documentation for pretix

What follows is an incomplete list of best practices, that is, things you **should** do when contributing to this documentation.
The best practices are the following:

 - observe our [four maxims of documentation](#follow-our-four-maxims-of-documentation)
 - [read](#read-the-documentation) the documentation
 - [contact](#contact-the-team) the team
 - [try pretix yourself](#try-it-yourself)
 - break down [complex issues](#break-down-complex-issues)
 - assume [real-world use cases](#lead-with-the-assumed-use-case) and lead with them
 - [keep sentences short](#keep-sentences-short)
 - [keep paragraphs short](#keep-paragraphs-short)
 - use the [active voice](#use-the-active-voice) and imperative
 - only use the [passive voice](#only-use-passive-voice-when-appropriate) when appropriate
 - include [image descriptions](#add-image-descriptions), also known as alt text
 - add [cross-references](#add-cross-references)
 - link to [external documentation](#link-to-external-documentation)
 - use [Vale](#use-vale-to-improve-your-text) to improve your text

The following sections explain those best practices in detail.

#### Adhere to our Code of Conduct

Before you contribute to pretix itself or its documentation, read our [code of conduct](https://docs.pretix.eu/dev/development/contribution/codeofconduct.html).
Adhere to this code of conduct while making contributions.

#### Follow our four maxims of documentation

When writing documentation for pretix, try to stick to the [maxims of conversation](https://en.wikipedia.org/wiki/Cooperative_principle#Grice's_maxims) as postulated by linguist Paul Grice.
These maxims, when applied to the task of documenting pretix, entail the following:

 1. Maxim of quantity: be informative.

    Give complete instructions.
    Do **not** skip any necessary steps.
    For instance, if it is necessary to save the settings before they can take effect, then clicking the "Save" button is an essential step.
    Omit any information that is not needed for the task at hand.

 2. Maxim of quality: be truthful.

    Check and double-check that your instructions actually work when using pretix.
    Do **not** include any factually inaccurate information.
    Do **not** include any uncertain information.
    Missing information is still better than wrong information.

 3. Maxim of relation: be relevant.

    Explain how to use pretix.
    Explain how pretix works.
    Only explain processes external to pretix if they are necessary for a feature of pretix to work.

 4. Maximum of manner: be clear.

    Write as clearly, simply, and directly as possible.
    Keep sentences short.
    Avoid obscure and complex expressions.
    Provide the steps in the exact order that the user needs to follow.
    Provide navigation instructions in order from largest (most general) to smallest (most specific).

#### Read the documentation

The more familiar you are with the documentation, the better prepared you are for contributing to it.
In addition to the webpages themselves, also take a look at the source code.
Try to make your contribution look like the pages that are already there.

For an example of a comprehensive article that represents a good implementation of our guides template, take a look at the guide on [gift cards](../gift-cards.md).
If you are writing a guide, try to structure your guide like the one on gift cards.
You can also use the file `template-guides.md` in the root directory of this repository.

#### Contact the team

Talk to the docs team.
Create an issue on the GitHub page for [pretix-docs](https://github.com/pretix/pretix-docs/issues) or send an email to [pretix support](mailto:support@pretix.eu).

The docs team will answer any questions you might have regarding your contribution.
They will be able to tell you whether it is relevant; where it fits into the established structure of the documentation; whether there are any internal resources on the subject; and so on.

You are helping the docs team a great deal by contacting them before submitting a pull request.
Reviewing a PR, fixing the formatting and discussing how it fits into the concept of the documentation is more work than discussing a few open questions ahead of time.

#### Try it yourself

The best way to understand how to use a feature of pretix is trying to use that feature yourself.
If you want to document, for instance, how to use vouchers, log into your pretix account and use the vouchers feature yourself.
Note every step you have to take and every issue you encounter along the way.
This brings you close to a complete step-by-step guide for the feature.

#### Break down complex issues

There is a central challenge you will encounter again and again while writing documentation for pretix.
That challenge is to understand a complex issue, to break that issue down into its semantic components, and to communicate those components as straightforwardly as possible.

Consider the following example:

```
*You can filter events by meta data attributes.
*You can create those attributes in your order profile and set their values in both event and series date settings.
*For example, if you set up a meta data property called "Promoted" that you set to "Yes" on some events, you can pass a filter like this: [...]
```

This example also does offer a sufficiently detailed explanation of how to set up a metadata attribute.

```
#### Using the widget for a selection of events

If you are hosting multiple events, but only want to display some of them in the widget, then you should use **metadata attributes**.
This section explains how to create metadata attributes, assign them to events, and set a filter in the widget.

You can create metadata attributes by navigating to :navpath:Your organizer → :fa3-wrench: Settings → Event metadata: and clicking the :btn-icon:fa3-plus: Create a new property: button.
For example, you could set up a metadata property called "Promoted" with the values `True` and `False`, the default value being `False`.

In order to assign the metadata property to an event, navigate to :navpath:Your event → :fa3-wrench: Settings → General:.
On the :btn:Basics: tab, edit the relevant property under "Meta data".

For example, if you set up a metadata property called "Promoted" with values `True` and `False` that you set to `True` on some events, you can pass a filter like this: [...]
```

The above example expands upon the explanation on how to set up a metadata attribute.
If a sufficient explanation of that process already existed elsewhere, then cross-referencing it here would achieve the same effect.

Give the user complete and clear instructions.
If the documentation already includes such instructions elsewhere, tell the user where to find the instructions and provide them with a link.

#### Lead with the assumed use case

Make it easy for the reader to understand under which circumstances a given article or section is relevant to them.
If you are writing an article about a feature, tell the reader what they can use the feature for in the introduction.
For instance, if you are writing an [article about vouchers](../vouchers.md), explain the possible uses to the reader:
They can use vouchers to offer discounts, to limit availability, to reserve products, and to bypass a sold-out quota.

If you are writing a section about the way the reader can use a feature, explain the use case for which this is relevant.
Do **not** limit this explanation to the software and its functions.
Instead, include the real-world use case.

Consider the beginning of the example from the section about [breaking down complex issues](#break-down-complex-issues):

```
*You can filter events by meta data attributes.
*You can create those attributes in your order profile and set their values in both event and series date settings. [...]
```

This example does not lead with the assumed use case.
Thus, it does not make clear enough to the reader why they would want to filter events by metadata attributes.

```
#### Using the widget for a selection of events

If you are hosting multiple events, but only want to display some of them in the widget, then you should use **metadata attributes**.
This section explains how to create metadata attributes, assign them to events, and set a filter in the widget. [...]
```

The above example has fixed the issues of the previous one.
It includes an informative subheading and introductory sentence.
Hosting multiple events but only displaying a selection of them in the widget is a real-world use case.

#### Keep sentences short

Keep sentences short.
Separate complex sentences including subordinate clauses into two sentences wherever possible.
Do **not** include any sentences with more than one subordinate clause.

#### Keep paragraphs short

Do not write paragraphs longer than five to six lines.
Preview your article in a 1920 pixels wide browser window.
If one of the paragraphs in that article is longer than six lines, split it up.

If you are starting a new topic, start a new paragraph.

#### Use the active voice

Use the [active voice](https://en.wikipedia.org/wiki/Active_voice) wherever possible.
When passing instructions to the reader, use the [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood).
The [passive voice](https://en.wikipedia.org/wiki/Passive_voice) obfuscates who is taking an action.

```
The first code snippet should be added into the <head> part of your website.
```

It is unclear whether the above example is trying to instruct the user to add the code snippet, or if it describes the behavior of the software.
Thus, the reader has to use context to infer if they need to take action, or if the software takes care of it for them.
You can remedy this lack of clarity by using the imperative instead:

```
Add the code snippet to the <head> of your website.
```

The active voice also helps make the docs shorter and clearer.

```
*A list of all tax rules that you have created for the event is displayed on this page.
```

This sentence contains 18 words.
A relative clause is embedded in the middle of the sentence.
Compare this to the following:

```
This page displays a list of all tax rules that you have created for the event.
```

This sentence contains 16 words.
The relative clause is at the end of the sentence.
This makes it easier to parse.

#### Only use passive voice when appropriate

The passive voice is still appropriate in a few special circumstances.
Use the passive voice when describing a general state of things, and when the person taking an action is unknown.
The following example describes a general state of things:

```
Customer accounts are handled on the organizer level.
```

This is not an instruction.
Thus, the imperative would be inappropriate here.

In the next example, it is unclear who is taking an action:

```
By default, pretixSCAN will only recognize a ticket as valid **once** if it has not been checked out in the meantime.
```

In this example, the author cannot know who checked out the ticket.
It could have been the reader, another team member, or a customer using a checkout kiosk.
The only relevant factor is whether the ticket is checked out or not.
Thus, the passive voice is appropriate.

There is another phenomenon which looks like passive, but describes a state instead of a process.
For example:

```
Checking that box makes another box appear that is checked by default.
```

```
The scan engine is located on the top edge of the device.
```

Vale will misidentify these examples as passives.
That is inaccurate.
Since these cases do not represent a genuine use of the passive voice, they are okay to use in the context of the pretix documentation.

!!! Note
   If you speak German, you can determine these cases by attempting to translate them into German.
   If you translate the sentence with the word "sein" as opposed to the verb "werden", then it is not a genuine passive.
   For instance, you would translate the first example as:
   `ein Kontrollkästchen, das standardmäßig angehakt ist`

#### Add image descriptions

Whenever you add an image to the pretix documentation, add an image description along with it.
Do not include an image without an image description in your article.
You can find basic information on how to write a good image description at [Axess Lab](https://axesslab.com/alt-texts/).

#### Add cross-references

One aim of this documentation is to facilitate the search for relevant information for the reader.
The first time you mention a concept or feature in an article, link to the relevant article.
Make these links informative.
For example, after mentioning gift cards in an article, insert a cross-reference such as the following:

```
For more information, see the article on [gift cards](../gift-cards.md).
```

If you are contributing a new article, check the existing documentation for mentions of the subject of your article and insert references to your article.

#### Link to external documentation

Insert links to pretix blog posts, Wikipedia, third-party software documentation, legal texts, or high-quality how-to guides on other websites.
The readers of this documentation benefit from curated links to relevant information.
That way, they do not have to search for the missing information themselves.
This also reduces the risk of them encountering bad information.

Strip all unnecessary data (such as tracking) from a link before inserting it.
You can identify the start of the unnecessary data by the `#` or the `?` symbol in the URL.
Check any links to external websites frequently to confirm that they still point to the desired website.

#### Use Vale to improve your text

The linter Vale can help improve your writing.
Think of it as an automated review relying on grammar and style rules implemented with regular expressions.
Take a look at the [vale-pretix](https://github.com/mschrumpf/vale-pretix) repository and follow the instructions there to use Vale on your own writing.
The vale-pretix repo contains custom vocabulary and rules for the pretix documentation.
You can also contribute to the improvement of these rules by following the instructions in the repo readme.

### What not to do when writing documentation for pretix

What follows is an incomplete lists of things you might feel tempted to do when contributing, but which do not fit into the concept of the pretix documentation.
This section will explain why the following things are not a good idea:

 - do not use [artificial intelligence](#do-not-use-artificial-intelligence-ai)
 - do not contribute [machine-translated](#do-not-contribute-machine-translated-text) text without intensive editing
 - do not re-narrate the [user interface](#do-not-re-narrate-the-user-interface)
 - do not use [empty phrases](#do-not-use-empty-phrases)
 - do not overuse [notes and warnings](#do-not-overuse-notes-and-warnings)
 - do not document [third-party software](#do-not-attempt-to-replace-the-documentation-for-third-party-software)

The following sections explain these things to avoid in detail.

#### Do not use Artificial Intelligence (AI)

Do **not** use so-called artificial intelligence (AI), for instance Large Language Models (LLMs) such as ChatGPT.
LLMs can generate text that, on the surface, looks professional and accurate.
But LLMs **cannot** do research.
They **cannot** interact with pretix like a human user can.
The texts that LLMs produce **cannot** be guaranteed to be factually accurate.
They will often contain false information.

As the maxim of quality states, missing information is better than wrong information.
You can improve the pretix documentation by researching the information and putting it into words yourself.
You **cannot** improve it by prompting an LLM to do it.

#### Do not contribute machine-translated text

Machine translators such as DeepL or Google Translate can be of great help when translating the pretix documentation into another language.
However, you **cannot** rely on machine translation alone to provide a good translation.
Cross-reference the UI in the target language.
Change all texts, labels, buttons and other UI elements mentioned in the translated text to match the ones on the website.
Edit the terminology in the target language to be accurate, consistent, and distinct.
Correct grammar, spelling and punctuation in the target language so that they follow established standards.

### Do not re-narrate the user interface

There is no value in recounting the entire user interface.
Work on the assumption that the reader can see UI elements and read descriptions.
Your job is to provide the reader with a sequence of actions to take.
It is **not** to describe every element on the screen and explain what it does.

Such descriptions can be helpful in some circumstances.
One such case is if you are telling your reader to navigate to a page which they likely have not visited before:

```
This will land you on a page titled "Issued gift cards" displaying a search dialog, a button for manually issuing a gift card, and a list of gift card codes that have been issued already.
```

Such a description reassures the reader that they have taken the right actions to arrive on that page.
But a brief overview is enough to accomplish that.

Do not think in terms of UI elements.
Think in terms of use cases.
You do not need to tell the reader what they are seeing.
You need to tell the reader what to do.

#### Do not use empty phrases

Avoid unnecessary fluff such as:

 - "Make sure that"
 - "Please"
 - "Note that"
 - "It is, however, necessary to note that"
 - "important"
 - "critical"
 - "just"
 - "simply"

The linter [Vale](https://github.com/mschrumpf/vale-pretix) will help you avoid some of these expressions, but it will not catch all of them.

It is okay to use "just" for a temporal relation, for example:

```
In the "Domain name" field, enter the subdomain you just created.
```

#### Do not overuse notes and warnings

Before adding an admonition (a note or a warning), ask yourself if the information is necessary for following the instructions in the main text.
If it is, then do **not** hide the information in an admonition.
Include it in the main text instead.

Do **not** place two or more admonitions directly after one another if possible.

Do **not** use admonitions other than notes or warnings.
If you think that another type of admonition is necessary, talk to the docs team first.

#### Do not attempt to replace the documentation for third-party software

Some features of pretix can only be used in conjunction with third-party software.
Examples of this include plugins that interface with a third-party service, particularly payment providers, as well as data exports.
The maxim of quantity includes the statement that you should "[g]ive complete instructions" and that you should "not skip any necessary steps".
This would imply that you need to give complete instructions on what steps to take in the third-party software as well.
However, as the maxim of relation states:
"Only explain processes external to pretix if they are necessary for a feature of pretix to work."

Third-party software is a moving target.
The pretix team does not have any insight into its development.
This means that whenever a change takes place, it can take months or even years until the pretix team notices the change and is able to update the documentation accordingly.

Because of this, it makes more sense to describe the necessary steps in the third-party software **not** click-by-click, but in broad strokes.
Describe how to cross-authenticate pretix and the third-party software, what codes and URLs to copy back and forth, etc.
But for more in-depth use of the other software, try to find a corresponding page in their documentation and link to that.