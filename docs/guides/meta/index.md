# Meta documentation 

This section of the documentation explains how the documentation itself works, how it was written, and how to contribute to it. 
This is directed at both coworkers, and at external contributors. 
It also serves as a reminder for the people writing the docs themselves how we do certain things, and why we decided to do them that way. 

## How to write documentation for pretix 

When writing documentation for pretix, do your best to stick to the [maxims of conversation](https://en.wikipedia.org/wiki/Cooperative_principle#Grice's_maxims) as postulated by linguist Paul Grice. 
These maxims, when applied to the task of documenting pretix, entail the following: 

 1. Maxim of quantity: be informative. 

    Give complete instructions. 
    Do not skip any necessary steps. 
    For instance, if it is necessary to save the settings before they can take effect, then clicking the "Save" button is an essential step. 
    Omit any information that is not needed for the task at hand. 

 2. Maxim of quality: be truthful. 

    Check and double-check that your instructions actually work when using pretix. 
    Do not include any factually inaccurate information. 
    Do not include any uncertain information. 
    Missing information is still better than wrong information. 

 3. Maxim of relation: be relevant. 
    
    Explain how to use pretix. 
    Explain how pretix works. 
    Only explain processes external to pretix if they are necessary for a feature of pretix to work. 

 4. Maximum of manner: be clear. 

    Write clear, simple, and straightforward as possible. 
    Keep sentences short. 
    Avoid obscure and complex expressions. 
    Provide the steps in the exact order that the user needs to follow. 
    Provide navigation instructions in order from largest (most general) to smallest (most specific). 

## What NOT to do when writing documentation for pretix 

What follows is an incomplete lists of things you might be tempted to do when contributing, but which do not fit into the concept of the pretix documentation. 
This section will help you understand why these things are not a good idea. 

### Do not use Artificial Intelligence (AI)

Do not use so-called artificial intelligence (AI), for instance Large Language Models (LLMs) such as ChatGPT. 
LLMs can generate text that, on the surface, looks professional and accurate. 
But LLMs cannot do research. 
They cannot interact with pretix like a human user can. 
The texts that LLMs produce cannot be guaranteed to be factually accurate. 
They will often contain false information. 

As it is stated under the maxim of quality, missing information is better than wrong information. 
You can improve the pretix documentation by researching the information and putting it into words yourself. 
You cannot improve it by prompting an LLM to do it. 

### Do not contribute machine-translated text

Machine translators such as DeepL or Google Translate can be of great help when translating the pretix documentation into another language. 
However, you cannot rely on machine translation alone to provide a good translation. 
Cross-reference the UI in the target language. 
Change all texts, labels, buttons and other UI elements mentioned in the translated text to match the ones on the website. 
Edit the terminology in the target language to be accurate, consistent, and distinct. 
Correct grammar, spelling and punctuation in the target language so that they follow established standards. 

### Do not use empty phrases

Avoid unnecessary fluff such as: 

 - "Make sure that" 
 - "Please" 
 - "Note that" 
 - "It is, however, necessary to note that" 
 - "important" 
 - "critical" 

### Do not overuse notes and warnings 

Before adding an admonition (a note or a warning), ask yourself if the information is necessary for following the instructions in the main text. 
If it is, then it does not belong in an admonition. 

Do not place two or more admonitions directly after one another if possible. 

Do not use admonitions other than notes or warnings. 
If you think that that is necessary, talk to the docs team first. 

### Do not attempt to replace the documentation for third-party software 

Some features of pretix can only be used in conjunction with third-party software. 
Examples of this include plugins that interface with a third-party service, particularly payment providers, as well as data exports. 
Under the maxim of quantity, it is stated that you should "[g]ive complete instructions" and that you should "not skip any necessary steps". 
This would imply that you need to give complete instructions on what steps to take in the third-party software as well. 
However, as it is stated under the maxim of relation:
"Only explain processes external to pretix if they are necessary for a feature of pretix to work."

Third-party software is a moving target. 
The pretix team does not have any insight into its development. 
This means that whenever a change takes place, it can take months or even years until that change is noticed and can be reflected by an update to the documentation. 

As a result of this, it makes more sense to describe the necessary steps in the third-party software not click-by-click, but in broad strokes. 
Describe how to cross-authenticate pretix and the third-party software, what codes and URLs to copy back and forth, etc. 
But for more in-depth use of the other software, try to find a corresponding page in their documentation and link to that. 

## Best Practices: What to do when writing documentation for pretix

What follows is an incomplete list of Best Practices, i.e., things you **should** do when contributing to this documentation. 

### Read the documentation

The more familiar you are with the documentation, the better prepared you are for contributing to it. 
In addition to the webpages themselves, also take a look at the source code. 
Try to make your contribution look like the pages that are already there. 

### Contact the team

Talk to the docs team. 
Create an issue on the GitHub page for [pretix-docs](https://github.com/pretix/pretix-docs/issues) or send an email to [pretix support](mailto:support@pretix.eu). 
The support team will forward your mail to the docs team. 

The docs team will answer any questions you might have regarding your contribution. 
They will be able to tell you whether it is relevant; where it fits into the established structure of the documentation; whether there are any internal resources on the subject; and so on. 

You are helping the docs team a great deal by contacting them before submitting a pull request. 
Reviewing a PR, fixing the formatting and discussing how it fits into the concept of the documentation is more work than discussing a few open questions ahead of time. 

### Follow the instructions on writing for MkDocs 

Consult the article on [writing for MkDocs](mkdocs.md). 
This documentation is fairly formalized. 
Each type of information has its own specific formatting. 
The linked article explains how to use Markdown and MkDocs to format each type of information. 

### Try it yourself 

The best way to understand how to use a feature of pretix is trying to use that feature yourself. 
If you want to document, say, how to use the seating plan editor, log into your pretix account and use the feature editor yourself. 
Note every step you have to take and every issue you encounter along the way. 
This brings you fairly close to a complete step-by-step guide for the feature. 

### Add cross-references 

One aim of this documentation is to facilitate the search for relevant information for the reader. 
The first time you mention a concept or feature in an article, link to the relevant article. 
Make these links informative. 
For example, after mentioning gift cards in an article, insert a cross-reference such as the following: 

``` 
For more information, see the article on [gift cards](../gift-cards.md). 
``` 

If you are contributing a new article, check the existing documentation for mentions of the subject of your article and insert references to your article. 

### Link to external documentation 

Insert links to pretix blog posts, Wikipedia, third-party software documentation, legal texts, or high-quality how-to guides on other websites. 
The readers of this documentation benefit from curated links to relevant information. 
That way, they do not have to search for the missing information themselves and there is a reduced risk of them encountering bad information. 

Strip any and all unnecessary data (such as tracking) from a link before inserting it. 
Any links to external websites will have to be checked frequently to make sure that they still point to the desired website. 