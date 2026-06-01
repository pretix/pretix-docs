# Language

This article explains what kind of language, writing style, orthography, grammar, and terminology to use when contributing to the pretix documentation.
This article focuses on the English-language parts of the pretix documentation.

## Prerequisites

There are no strict prerequisites for using appropriate language while writing pretix documentation.
A solid grasp of the English language is helpful.

## How to

### Writing style

There is a central challenge you will encounter again and again while writing documentation for pretix.
That challenge is to understand a complex issue, to break that issue down into its semantic components, and to communicate those components as straightforwardly as possible.

Keep sentences short.
Separate complex sentences including subordinate clauses into two sentences wherever possible.
Do **not** include any sentences with more than one subordinate clause.

#### Passive voice

Use the active voice wherever possible.
When passing instructions to the reader, use the imperative mood.
The passive voice obfuscates who is taking an action.

```
The first code snippet should be added into the <head> part of your website.
```

In the above example, it is unclear who is supposed to add the code snippet.
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

The passive voice is still appropriate in a few special circumstances.
Use the passive voice in the following cases:

 1. when describing a general state of things

```
Customer accounts are handled on the organizer level.
```

 2. when the person taking an action is unknown

```
By default, pretixSCAN will only recognize a ticket as valid **once** if it has not been checked out in the meantime.
```

In this example, the author cannot know who checked out the ticket.
It could have been the reader, another team member, or a customer using a checkout kiosk.
The only relevant factor is whether the ticket is checked out or not.

### Terminology

The pretix documentation benefits from consistent and clear terminology.
There should be a one-to-one correspondence between words and concepts.

Always communicate a concept with the same word.
For instance, if you want to instruct the user to click a button in the pretix backend, use the word "click".
Do **not** use "click on", "tap", "hit", "use", "interact with", or any other terminology.

Always use a word for the same concept.
For instance, do not use the word "category" to refer to product categories, seat categories, and GetYourGuide categories.
Specify which type of category you are writing about, even if it should be clear from context.

There is a [terminology database](https://www.terminologue.org/pretix-docs/) for the pretix documentation.
Use this database to look up preferred terminology and to record new decisions regarding terminology.
If you want to make a new addition or correction to the terminology database, speak to the team.

### Orthography

There are three sources for proper orthography within the context of the pretix documentation:

 1. Our internal [terminology database](https://www.terminologue.org/pretix-docs/)
 2. [Merriam-Webster](https://www.merriam-webster.com/)
 3. [Wiktionary](https://en.wiktionary.org/)

Use the spellings marked as "preferred" in our terminology database.
Do not use the variants marked as "rejected".
If our terminology database does not have an entry on a word, consult Merriam-Webster.
Ignore spellings marked as "variant".
If neither our terminology database nor Merriam-Webster have an entry on a word, use Wiktionary.

If you or the team have not yet made a decision which spelling option to use, pick on variant and stick with it.
Consistent spelling is helpful for replacing the word with the proper spelling later.

### Punctuation

English and German have different punctuation rules.
This is an overview over commonly used special characters.

#### Numbers

Write the numbers from zero to ten as whole words.

```
one, two, three, ... ten
```

Write all larger numbers as numbers:

```
11, 20, 67, 947
```

For amounts of money, put the currency symbol at the beginning.
Do **not** separate it with a space.

```
€1,899.99
```

For percentages, place the percentage symbol at the end.
Do **not** use a space between the number and the symbol.

```
19%
```

#### Quotation marks

For quotation marks, use `"` (U+0022 QUOTATION MARK).
When copying text from Confluence, word editors, or other websites, check if your text still contains the correct quotation marks.
These other softwares will sometimes replace the quotation mark above with a different symbol such as `”`.
Do **not** use this symbol anywhere in our documentation.
It only occurs here as a deterrent example.

#### Hyphens and dashes

The pretix documentation uses a few different dash symbols.
The hyphen and minus are the same symbol: `-` (U+002D HYPHEN-MINUS).
Use the hyphen-minus for compound words as suggested by our sources on [orthography](#orthography).

The en-dash is a separate symbol: `–` ( U+2013 EN DASH).
Use the en-dash for relationships and connections:

```
Merriam–Webster
```

You may use the en-dash for ranges of values in tables and formulas:

```
| Animal | Amount |
|------------|-------|
| Feral hogs | 30–50 |
```

In the text, use the word "to" for ranges of values instead:

```
30–50 feral hogs
```

The em-dash is yet another separate symbol: `—` (U+2014 EM DASH).
Use the em-dash to set off a summary or a clarification of the previous sentence.
Do not add spaces before or after the em-dash.

```
pretix offers you many options for contacting your customers and attendees via email—both on the organizer level and on the event level.
```

#### Commas

English sentences usually start with the subject.
If the sentence contains an imperative, then they usually start with the imperative verb.
If the sentence starts with anything other than the subject or the imperative verb, then you need to separate the starting element from the rest of the sentence with a comma.

If your sentence starts with an **adverbial phrase**, separate that phrase from the main clause with a comma.

```
Under the "Other operations" heading, select one of the options next to "Recalculate taxes".
```

If your sentence starts with a **subordinate clause**, separate that clause from the main clause with a comma.

```
While your event is in test mode, pretix will always use Stripe's testing endpoint regardless of the setting here.
```

English punctuation rules differentiate between restrictive and non-restrictive **relative clauses**.
Restrictive relative clauses are essential to the meaning of the sentence.
Removing a restrictive relative clause would change the meaning of the main clause of the sentence.
Non-restrictive relative clauses provide additional information.
But removing a non-restrictive relative clause does not change the meaning of the main clause.

Separate non-restrictive relative clauses from the main clause with a comma.

```
The admission ticket price also automatically includes catering, which is still taxed at a rate of 19.00%.
```

Separating the non-restrictive relative clause from the main clause does not change the meaning.

```
The admission ticket price also automatically includes catering.
Catering is still taxed at a rate of 19.00%.
```

Do **not** separate restrictive relative clauses from the main clause with a comma.

```
They will also be able to view and edit any orders that have been placed with the same email address.
```

Separating the restrictive relative clause from the main clause changes the meaning.

```
*They will also be able to view and edit any orders.
*Orders have been placed with the same email address.
```
