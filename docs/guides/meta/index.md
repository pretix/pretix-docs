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
    Do not explain anything else. 

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
LLMs cannot do research. 
LLMs cannot interact with pretix like a human user can. 
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

Do not place two or more admonitions directly after one another. 

Do not use admonitions other than notes or warnings. 
If you think that that is necessary, talk to the docs team first. 

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