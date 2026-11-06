---
title: Markdown
---
# Markdown

Sie können an mehreren Stellen in Ihrem Shop – beispielsweise in Texten auf der Startseite, in Produktbeschreibungen und in E-Mail-Texten – [Markdown](https://de.wikipedia.org/wiki/Markdown) verwenden, um Links, fettgedruckten Text und andere formatierte Inhalte zu erstellen.
Markdown bietet einen guten Kompromiss, da es deutlich leichter zu erlernen ist als Auszeichnungssprachen wie HTML, aber trotzdem alle grundlegenden Formatierungsmöglichkeiten bietet, die für Text in diesen Bereichen erforderlich sind.

!!! Note
    Einige Felder, die nur für einzeilige Texte vorgesehen sind, unterstützen nur wortbezogene Formatierungen (wie Fett- oder Kursivschrift oder einen Link).
    Blockformatierungen wie Listen oder Überschriften sind dort jedoch nicht möglich.

## Formatierungsregeln

### Einfache Textformatierung

Um einen Text kursiv zu formatieren, können Sie ihn in Sternchen oder Unterstriche setzen.
Zum Beispiel:

``` markdown
Bitte bezahlen Sie Ihr _Ticket_ *unbedingt*.
```

Daraus wird:

> Bitte bezahlen Sie Ihr *Ticket* *unbedingt*.

Wenn Sie doppelte Sternchen oder Unterstriche setzen, wird der Text fett gedruckt.
Zum Beispiel:

``` markdown
Das ist **wichtig**.
```

Daraus wird:

> Das ist **wichtig**.

Sie können beispielsweise auch Folgendes anzeigen lassen:

``` markdown
Geben Sie das `genau so` ein.
```

Dann bekommen Sie:

> Geben Sie das `genau so` ein.

Um zu verhindern, dass ein Zeichen als Markdown-Formatierung interpretiert wird, muss ihm das Escape-Zeichen "Backslash" `\` vorangestellt werden.

``` markdown
Das ist \*\*wichtig\*\*.
```

Daraus wird:

> Das ist \*\*wichtig\*\*.

### Links

Sie können einen Link erstellen, indem Sie ihn einfach einfügen, z. B.

``` markdown
Schauen Sie sich das hier an: https://de.wikipedia.org
```

Daraus wird:

> Schauen Sie sich das hier an: https://de.wikipedia.org

Wenn Sie verhindern möchten, dass ein Wort als URL erkannt und entsprechend dargestellt wird, können Sie den Punkt mit einem Backslash maskieren.

``` markdown
Schauen Sie sich das hier an: de\.wikipedia\.org
```

Daraus wird:

> Schauen Sie sich das hier an: de\.wikipedia\.org


Wenn Sie den Text des Links festlegen möchten, können Sie diesen in eckige Klammern `[]` und das Linkziel in runde Klammern `()` setzen.
Das sieht dann wie folgt aus:

``` markdown
Schauen Sie sich das hier auf [Wikipedia](https://de.wikipedia.org) an.
```

Daraus wird:

> Schauen Sie sich das hier auf [Wikipedia](https://de.wikipedia.org) an

Alle Links, die mit der pretix-Markdown-Syntax erstellt wurden, werden in einem neuen Tab geöffnet.

### Listen

Sie können unnummerierte Listen erstellen, indem Sie den Zeilen Sternchen voranstellen.

``` markdown
 * Erster Eintrag
 * Zweiter Eintrag mit einem Text, der zu lang ist, um in eine Zeile zu passen
 * Dritter Eintrag
```

Daraus wird:

>- Erster Eintrag
>- Zweiter Eintrag mit einem Test, der zu lang ist, um in eine Zeile zu passen
>- Dritter Eintrag

Sie können auch Zahlen als Listenelemente verwenden

``` markdown
 1. Erster Listeneintrag
 2. Zweiter Listeneintrag
 3. Dritter Listeneintrag
```

um folgendes zu erhalten:

> 1. Erster Listeneintrag
> 2. Zweiter Listeneintrag
> 3. Dritter Listeneintrag

### Überschriften

Um eine Überschrift zu erzeugen, fügen Sie am Anfang ein `#` für die Hauptüberschrift, ein `##` für eine Überschrift der zweiten Ebene usw. ein.
Zum Beispiel:

``` markdown
# Überschrift 1
## Überschrift 2
### Überschrift 3
#### Überschrift 4
##### Überschrift 5
###### Überschrift 6
```

Wir raten davon ab, Überschriften der ersten Ebene zu verwenden, da pretix den Namen Ihrer Veranstaltung bereits als Überschrift der ersten Ebene auf der Seite festlegt.
HTML-Seiten sollten nur eine Überschrift der ersten Ebene enthalten.

Sie können entweder Markdown verwenden:

``` markdown
*****
```
Oder HTML:

```{=html}
<hr>
```

Um eine horizontale Linie wie die folgende zu erstellen:

*****

## HTML verwenden

Sie können bei Bedarf auch HTML-Code direkt einbetten.
Wir empfehlen jedoch die Verwendung von Markdown, da dies beispielsweise Nutzern von textbasierten E-Mail-Clients eine bessere Darstellung Ihres Textes in Plain Text ermöglicht.
Aus Sicherheitsgründen können Sie nur die folgenden HTML-Elemente verwenden:

    a, abbr, acronym, b, br, code, div, em, h1, h2,
    h3, h4, h5, h6, hr, i, li, ol, p, pre, s, span, strong,
    table, tbody, td, thead, tr, ul

Zudem sind für diese Elemente ausschließlich die folgenden Attribute zulässig:

    <a href="…" title="…">
    <abbr title="…">
    <acronym title="…">
    <table width="…">
    <td width="…" align="…">
    <div class="…">
    <p class="…">
    <span class="…">

Alle anderen Elemente und Attribute werden beim Parsen entfernt.
