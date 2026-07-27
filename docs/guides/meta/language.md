# Language

This article explains what kind of language, writing style, orthography, grammar, and terminology to use when contributing to the pretix documentation.
This article focuses on the English-language parts of the pretix documentation.

## Prerequisites

A solid grasp of the English language is helpful.
You need access to our [terminology database](https://www.terminologue.org/pretix-docs/).
If you cannot access the database, request it from our team.
In order to do so, you can [send us an email](mailto:support@pretix.eu).

## How to

Using proper language is not a linear process.
Rather, it requires attention to many factors at the same time.
Thus, unlike most other guides, this article will not give you step-by-step instructions.
Instead, it will introduce and explain the factors that are relevant for proper language within the context of the pretix documentation:

 - [writing style](#writing-style)
 - [terminology](#terminology)
 - [orthography](#orthography)
 - [punctuation](#punctuation)

This article will cover these factors in detail.
Some of them are complex enough to include several subsections.

### Writing style

Write text that is easy to understand and unambiguous.
In order to do so, [keep sentences short](#keep-sentences-short), [keep paragraphs short](#keep-paragraphs-short), [use the active voice](#use-the-active-voice), and [only use the passive voice](#only-use-passive-voice-in-a-few-special-cases) in a few special cases.

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

#### Only use passive voice in a few special cases

The passive voice is still appropriate in a few special circumstances.
Use the passive voice:

 1. to describe a general state of things
 2. if the entity taking an action is unknown

There is another case that looks like passive voice on the surface level, but is actually a separate phenomenon.
This section covers both legitimate uses of the passive voice, and that phenomenon.

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

### Terminology

The pretix documentation benefits from consistent and clear terminology.
There should be a one-to-one correspondence between words and concepts.

Always communicate a concept with the same word.
For instance, if you want to instruct the user to click a button in the pretix backend, use the word "click".
Do **not** use "click on", "tap", "hit", "use", "interact with", or any other terminology.

Do **not** use the same term for more than one concept.
For instance, do **not** use the word "category" to refer to product categories, seat categories, and GetYourGuide categories.
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

In case of disagreement between the three sources, stick to the hierarchy.
Merriam–Webster takes precedence over Wiktionary.
Our internal terminology database takes precedence over Merriam–Webster and Wiktionary.
For instance, despite broadly using US-American orthography, we prefer the spelling "theatre" over "theater".

If you or the team have not yet made a decision which spelling option to use, pick one variant and stick with it.
Consistent spelling is helpful for replacing the word with the proper spelling later.

### Punctuation

This section gives an overview on how to use proper punctuation while contributing to the pretix documentation.

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
30 to 50 feral hogs
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

If the adverbial phrase is in the middle or at the end of the sentence, do **not** use a comma.

If your sentence starts with a **subordinate clause**, separate that clause from the main clause with a comma.

```
While your event is in test mode, pretix will always use Stripe's testing endpoint regardless of the setting here.
```

If the subordinate clause is in the middle or at the end of the sentence, do **not** use a comma.

!!! Note
    In English, subordinating conjunctions such as "because", "while", "that", or "if" do **not** require a comma.
    If your first language is German, then you may feel tempted to use a comma before such a word.
    Only use a comma before these words if other factors require it.

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

Always separate **main clauses** with full stops.
Do **not** separate them with a comma.

If you are listing two elements, do **not** use a comma before "and" or "or".
If you are listing more than two elements, use a comma before "and" or "or" (Oxford comma).