# Markdown 

In many places of your shop, like frontpage texts, product descriptions and email texts, you can use [Markdown](https://en.wikipedia.org/wiki/Markdown) to create links, bold text, and other formatted content. 
Markdown is a good middle-ground since it is way easier to learn than languages like HTML but allows all basic formatting options required for text in those places.

!!! Note
    Some fields that are used in one-line context only allow formatting that refers to individual words (such as bold or italic font or a link) but do not allow block-level formatting like lists or headlines.

## Formatting rules

### Simple text formatting

To set a text in italics, you can put it in asterisks or underscores. 
For example,

``` markdown
Please *really* pay your _ticket_.
```

will become:

> Please *really* pay your *ticket*.

If you set double asterisks or underscores, the text will be printed in bold. 
For example,

``` markdown
This is **important**.
```

will become:

> This is **important**.

You can also display, for example:

``` markdown
Input this `exactly like this`.
```

You will get:

> Input this `exactly like this`.

In order to prevent a character from being interpreted as markdown formatting, precede it with the backslash `\` escape character. 

``` markdown
This is \*\*important\*\*.
```

will become:

> This is \*\*important\*\*.

### Links

You can create a link by just pasting it in, e.g.

``` markdown
Check this on https://en.wikipedia.org
```

will become:

> Check this on <https://en.wikipedia.org>

If you want to prevent a word from being recognized as an URL and rendered accordingly, you can escape the dot with a backslash. 

``` markdown
Check this on en\.wikipedia\.org
```

This will yield:

> Check this on en\.wikipedia\.org


If you want to control the text of the link, you can put the text of the link in `[]` brackets and the link target in `()` parentheses, like this:

``` markdown
Check this on [Wikipedia](https://en.wikipedia.org).
```

This will yield:

> Check this on [Wikipedia](https://en.wikipedia.org)

All links created with pretix Markdown syntax will open in a new tab.

### Lists

You can create un-numbered lists by prepending the lines with asterisks.

``` markdown
* First item
* Second item with a text that is too long to
  fit in a line
* Third item
```

will become:

> -   First item
> -   Second item with a text that is too long to fit in a line
> -   Third item

You can also use numbers as list items

``` markdown
1.  Red
2.  Green
3.  Blue
```

to get

> 1.  Red
> 2.  Green
> 3.  Blue

### Headlines

To create a headline, prepend it with `#` for the main headline, `##` for a headline of the second level, and so on. 
For example:

``` markdown
# Headline 1
## Headline 2
### Headline 3
#### Headline 4
##### Headline 5
###### Headline 6
```

We do not recommend using headlines of the first level, as pretix will already set the name of your event as a level-1 headline of the page and HTML pages should have only one headline on the first level.

You can also use

``` markdown
*****
```

to create a horizontal line, like the following:

```{=html}
<hr>
```
## Using HTML

You can also directly embed HTML code, if you want, although we recommend using Markdown, as it enables e.g. people using text-based email clients to get a better plain text representation of your text. 
Note however, that for security reasons you can only use the following HTML elements:

    a, abbr, acronym, b, br, code, div, em, h1, h2,
    h3, h4, h5, h6, hr, i, li, ol, p, pre, s, span, strong,
    table, tbody, td, thead, tr, ul

Additionally, only the following attributes are allowed on them:

    <a href="…" title="…">
    <abbr title="…">
    <acronym title="…">
    <table width="…">
    <td width="…" align="…">
    <div class="…">
    <p class="…">
    <span class="…">

All other elements and attributes will be stripped during parsing.
