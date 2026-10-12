# Umsatzsteuer

In den meisten Ländern müssen Sie Steuern auf alle Umsätze abführen, die Sie mit pretix machen.
pretix gibt Ihnen die benötigten Werkzeuge an die Hand, um die korrekte Steuer auf jeden Verkauf zu errechnen.

Sie konfigurieren die Umsatzsteuer auf Veranstaltungsebene.
Wenn Sie eine Veranstaltung erstellen, fordert pretix Sie auf, eine einfache Steuer-Regel anzulegen.
Für die meisten unkomplizierten Fälle sollte das bereits ausreichen.
Dieser Artikel erklärt, wie Sie zusätzliche Steuer-Regeln erstellen, wie Sie komplexe eigene Steuer-Regeln konfigurieren und wie Sie Steuer-Regeln Produkten zuweisen.

Dieser Artikel sagt Ihnen **nicht**, welche Steuern Sie im Einzelfall berechnen müssen.
Dies hängt von dem Steuersystem Ihres Landes ab, von der Art Ihres Unternehmens und etlichen weiteren Faktoren.
Die pretix-Dokumentation enthält **keine** Informationen darüber, welche Steuersätze für Ihre Situation gelten.
Holen Sie eine qualifizierte Steuerberatung ein, bevor Sie in Ihrem Shop Steuersätze festlegen.

{% include "warning-tax-rules.md" %}

## Voraussetzungen

Umsatzsteuer gilt auf Veranstaltungsebene, Sie müssen also zuerst eine Veranstaltung anlegen.

## Allgemeine Verwendung

In pretix können Sie für jeden Steuersatz, der für Ihre Situation relevant ist, eine Steuer-Regel einrichten.
Anschließend weisen Sie diese Steuer-Regel jedem einzelnen Produkt zu.

Steuer-Regeln konfigurieren Sie für jede Veranstaltung individuell.
Es gibt keine Standard-Steuer-Regeln.
Damit Sie einem Produkt eine Steuer-Regel zuweisen können, müssen Sie diese Steuer-Regel zuerst anlegen.
Das gilt auch für einen Steuersatz von 0 %.
Auch wenn Sie Produkte mit einem Steuersatz von 0 % verkaufen (beispielsweise [Wertgutscheine](../guides/gift-cards.md)), müssen Sie zuerst eine Steuer-Regel für 0 % erstellen.

Bei Steuer-Regeln für kostenlose Produkte ist der auf der Rechnung gedruckte Steuersatz der einzige sichtbare Unterschied.
Legen Sie die Steuer-Regel an, die auf der Rechnung erscheinen soll, und weisen Sie sie Ihren Produkten zu.
pretix erstellt keine Rechnungen für Bestellungen, die ausschließlich kostenlose Produkte enthalten.

### Steuer-Regeln erstellen

Um eine neue Steuer-Regel zu erstellen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Steuern:. 
Diese Seite enthält eine Liste mit allen Steuer-Regeln, die Sie für diese Veranstaltung erstellt haben.
Um eine neue Steuer-Regel zu erstellen, klicken Sie den Button :btn:Neue Steuer-Regel erstellen:.  

![Dialogfeld 'Steuer-Regel'. Der Reiter 'Allgemein' zeigt Optionen für den offiziellen und den internen Namen, den Steuersatz und die Angabe, ob die Steuer im Produktpreis enthalten sein soll.](../assets/screens/tax/edit-rule.png "Erweiterte Optionen für Steuer-Regeln" )

Sie gelangen zu einem Dialogfeld, in dem Sie eine neue Steuer-Regel erstellen.
Der "Offizielle Name", den Sie auf dem Reiter "Allgemein" festlegen, ist der Name, der Kund\*innen im Shop angezeigt wird.
Hinterlegen Sie für jede verwendete Sprache die passende Übersetzung.

Optional können Sie auch einen "Internen Namen" festlegen, der Ihnen und Ihren Team-Mitgliedern im pretix-Backend angezeigt wird.

Wählen Sie unter "Steuersatz" den Prozentwert des Steuersatzes.
Wenn Sie beispielsweise in Deutschland Produkte mit dem regulären Umsatzsteuersatz verkaufen, legen Sie "Steuersatz" auf 19,00 % fest.

Über das Kästchen bei "Der konfigurierte Produktpreis enthält den Steuerbetrag" legen Sie fest, ob der Produktpreis bei dieser Steuer-Regel als Nettopreis (ohne Umsatzsteuer) oder Bruttobetrag (mit Umsatzsteuer) behandelt wird.

Standardmäßig ist diese Option aktiv, sodass pretix mit dieser Steuer-Regel alle Produktpreise als Bruttopreise behandelt, also inklusive Umsatzsteuer.
Damit setzt sich für ein Produkt der Listenpreis von 10,00 € bei einem Steuersatz von 19,00 % aus einem Nettopreis von 8,40 € und 1,60 € Umsatzsteuer zusammen, die addiert den Bruttopreis von 10,00 € ergeben.

Wenn Sie das Häkchen aus dem Kontrollkästchen entfernen, behandelt pretix mit dieser Steuer-Regel alle Produktpreise als Nettopreise und schlägt die Umsatzsteuer auf den Listenpreis auf.
Für ein Produkt mit einem Listenpreis von 10,00 € wird bei einem Steuersatz von 19,00 % Umsatzsteuer in Höhe von 1,90 € dazu addiert, sodass der Bruttopreis 11,90 € beträgt.
Diese Einstellung gilt für alle Produkte, die diese Steuer-Regel verwenden.
Sie gilt **nicht** für alle Produkte in Ihrem Shop.

Klicken Sie den Button :btn:Speichern:, um Ihre Einstellungen zu bestätigen.

Die Einstellung "Der konfigurierte Produktpreis enthält den Steuerbetrag" wirkt sich darauf aus, wie Sie in pretix Produktpreise konfigurieren.
Sie wirkt sich nicht darauf aus, wie die Preise Ihren Kund\*innen im Shop angezeigt werden.
Wenn Sie im Shop Preise ohne enthaltene Umsatzsteuer anzeigen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Steuern:.
Ändern Sie die Einstellung "Preisanzeige für Kunden" zu "Preise exklusive Steuern" und klicken Sie den Button :btn:Speichern:.
Diese Einstellung gilt unabhängig von der jeweiligen Steuer-Regel für alle Produkte.

### Eigene Steuer-Regeln

![Dialogfeld 'Steuer-Regel'. Der Reiter 'Erweitert' zeigt als Optionen die Steuerpflicht des Leistungsempfängers bei EU-Geschäften, das Land des Händlers und den Abschnitt zum Definieren neuer eigener Regeln.](../assets/screens/tax/advanced.png "Erweiterte Optionen für Steuer-Regeln" )

!!! Hinweis
    Die Verwendung eigener Steuer-Regeln und die Option zur Steuerpflicht des Leistungsempfängers bei EU-Geschäften ("Reverse Charge") schließen sich gegenseitig aus.
    Wenn Sie mindestens eine eigene Steuer-Regel definiert haben, wird die Reverse-Charge-Option zur Steuerpflicht des Leistungsempfängers **nicht** angewendet, selbst wenn das Kontrollkästchen bei "Nutze EU-Regeln zur Steuerpflicht des Leistungsempfängers (reverse charge)" markiert ist.

In pretix können Sie "eigene Regeln" definieren, wenn bei Ihnen besondere Anforderungen an die Bedingungen gelten, unter denen Umsatzsteuer auf Ihren Verkaufspreis aufgeschlagen wird oder nicht.
Diese "eigenen Regeln" sind den Steuer-Regeln untergeordnet und sind optional.

Wenn Sie eigene Regeln für Unternehmen einrichten möchten, die eine Umsatzsteuer-Identifikationsnummer (USt-ID) haben, müssen Sie Ihre Kund\*innen auffordern, die USt-ID anzugeben.
Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Rechnungswesen:. 
Wechseln Sie zum Reiter :btn:Adresseingabe: und stellen Sie sicher, dass die Kontrollkästchen neben "Rechnungsadresse erfragen" und "Nach USt-ID fragen" markiert sind.
Klicken Sie zur Bestätigung den Button :btn:Speichern:.

Um eine eigene Steuer-Regel zu erstellen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Steuern:.  
Klicken Sie die Steuer-Regel, für die Sie eigene Regeln festlegen möchten, wechseln Sie zum Reiter :btn:Erweitert: und klicken Sie den Button :btn-icon:fa3-plus: Neue Regel hinzufügen:.

Wählen Sie unter "Bedingung" im ersten Dropdown-Menü das Land bzw. die Region, wo die eigene Regel gelten soll, oder wählen Sie "Beliebiges Land".
Wählen Sie im zweiten Dropdown-Menü die Art des\*der Kund\*in (Privatperson, Unternehmen oder Unternehmen mit gültiger USt-ID-Nr.) oder wählen Sie "Beliebiger Kunde".

Wählen Sie unter "Berechnung", wie pretix unter den angegebenen Bedingungen (also je nach Land und Kund\*in) die Umsatzsteuer berechnet.
Wenn Sie für die angegebenen Bedingungen einen bestimmten Steuersatz berechnen möchten, wählen Sie "MwSt. berechnen" und geben Sie in das Eingabefeld darunter den Steuersatz ein.
Wenn für die definierte Bedingung die Steuerschuld des Leistungsempfängers gelten soll, wählen Sie "Reverse Charge" und lassen Sie das Feld darunter leer.

Über die anderen Optionen können Sie festlegen, dass **keine** Steuer berechnet wird, dass eine manuelle Freigabe erforderlich ist oder dass für die definierte Bedingung keine Verkäufe zulässig sind.
In diesen Fällen können Sie das Eingabefeld darunter leer lassen.

Unter "Grund" können Sie die rechtliche Begründung für die eingerichtete Steuer-Regel hinterlegen.
Wenn das Dropdown-Menü Ihren genauen Grund **nicht** enthält, wählen Sie eine allgemeinere Option.
In den Feldern "Text auf Rechnung" können Sie eine Erklärung für die berechnete Umsatzsteuer hinterlegen, die auf die Rechnungen an Ihre Kund\*innen gedruckt wird.

Wenn ein\*e Kund\*in eine Bestellung aufgibt, prüft pretix die eigenen Steuer-Regeln von oben nach unten.
Die erste Regel, die auf die Bestellung zutrifft, bestimmt dann, ob und wie pretix Umsatzsteuer berechnet.
Mit den Pfeil-Buttons :btn-icon:fa3-arrow-up:: und :btn-icon:fa3-arrow-down:: können Sie die Regeln je nach Priorität nach oben oder unten verschieben.

![Dialogfeld 'Steuer-Regel'. Auf dem Reiter 'Erweitert' sind vier eigene Regeln zu sehen, die im folgenden Absatz beschrieben werden.](../assets/screens/tax/custom-rules.png "Beispiel für eigene Regeln" )

Ein Beispiel: Ein Unternehmen in Deutschland organisiert eine Veranstaltung, bei der die Reverse-Charge-Regel der EU möglich ist.
Das Unternehmen legt zuerst die Regel für "Deutschland" an, die für "beliebige Kund\*innen" die Regel "MWSt. berechnen" anwendet.
Der Steuersatz beträgt 19,00 % und die Begründung ist "Standard-Steuerkodierung".
Anschließend legt das Unternehmen eine Regel für die "Europäische Union" an, die für "Unternehmen mit gültiger USt-ID-Nr." die "Reverse Charge"-Bestimmung anwendet, wobei das Feld für den Steuersatz leer ist und als Begründung "Steuerschuld des Leistungsempfängers (Reverse Charge)" gewählt ist.

Das Unternehmen legt außerdem eine Regel für "Österreich" an, die für "beliebige Kund\*innen" die Regel "MWSt. berechnen" anwendet und den österreichischen Umsatzsteuersatz verwendet.
Dieselbe Regel könnte es nun für alle EU-Mitgliedsstaaten anlegen, von Belgien bis Zypern, jeweils mit dem dortigen Umsatzsteuersatz.
Und schließlich kann das Unternehmen eine Regel für ein "Beliebiges Land" anlegen, die für "beliebige Kund\*innen" die Regel "MWSt. berechnen" anwendet.

In diesem Fall erfüllt ein in Österreich ansässiges Unternehmen mit gültiger USt-ID die Kriterien der zweiten und der dritten Regel.
Da pretix eigene Regeln aber immer von oben nach unten prüft und nur die erste zutreffende Regel anwendet, wendet die Software in diesem Beispiel nur die zweite Regel in der Liste auf die Transaktion an (Europäische Union → "Unternehmen mit gültiger USt-ID-Nr." → "Steuerschuld des Leistungsempfängers (Reverse Charge)").

Die Reihenfolge, in der das Beispielunternehmen die Regeln angeordnet hat, sorgt also dafür, dass keinem Unternehmen aus einem anderen EU-Mitgliedsstaat als Deutschland Umsatzsteuer auf die Transaktion berechnet wird, vorausgesetzt, das Unternehmen gibt bei der Bestellung eine gültige Umsatzsteuer-Identifikationsnummer an.

!!! Hinweis
    Das obige Beispiel dient nur zur Veranschaulichung, wie sich die Software einsetzen lässt.
    Es ist keine Rechtsberatung.

### Steuerpflicht des Leistungsempfängers bei EU-Geschäften ("reverse charge")

!!! Warnung
    Die Reverse-Charge-Regeln gelten **nicht** für die meisten mit pretix verwalteten Veranstaltungen.
    Wir **empfehlen daher dringend**, diese Funktion **nur zu aktivieren**, wenn es dafür einen konkreten Grund gibt.
    Laut Artikel 52 der [Richtlinie über das gemeinsame Mehrwertsteuersystem](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32006L0112&from=DE) (Seite 17) gilt als Ort der Veranstaltung der Ort, an dem die Dienstleistung tatsächlich bewirkt wird.
    Deshalb gilt immer die Steuergesetzgebung des Landes, in dem die Veranstaltung stattfindet, unabhängig vom Wohnort der Kund\*innen.

!!! Hinweis
    Die Reverse-Charge-Funktion ist abgekündigt, läuft also aus.
    Ein zukünftiges Update von pretix wird sie nicht mehr enthalten.
    Vermeiden Sie nach Möglichkeit die Verwendung der Reverse-Charge-Funktion und definieren Sie stattdessen eigene Steuer-Regeln.
    Auf diese Weise können Sie die Steuer-Regeln ganz genau auf Ihre jeweiligen Anforderungen abstimmen und sicherstellen, dass Sie alle relevanten Gesetze einhalten.

!!! Hinweis
    Die Verwendung eigener Steuer-Regeln und die Option zur Steuerpflicht des Leistungsempfängers bei EU-Geschäften ("Reverse Charge") schließen sich gegenseitig aus.
    Wenn Sie mindestens eine eigene Steuer-Regel definiert haben, wird die Reverse-Charge-Option zur EU-Steuerpflicht nicht angewendet, selbst wenn das Kontrollkästchen bei "Nutze EU-Regeln zur Steuerpflicht des Leistungsempfängers (reverse charge)" markiert ist.

Die Reverse-Charge-Regel ist Teil der Umsatzsteuer-Gesetzgebung der Europäischen Union und legt fest, wie Steuern berechnet werden, wenn Verkäufer\*in und Käufer\*in einer Ware in unterschiedlichen EU-Ländern ansässig sind.
Wenn der\*die Käufer\*in im eigenen Land als umsatzsteuerpflichtiges Unternehmen registriert ist, dürfen Sie als Verkäufer\*in nur den Nettopreis ohne Umsatzsteuer berechnen und müssen darauf hinweisen, dass der\*die Käufer\*in dafür verantwortlich ist, die erforderliche Umsatzsteuer abzuführen.

Wenn Sie die Reverse-Charge-Regel nutzen möchten, müssen Sie die USt-ID Ihrer Kund\*innen erfragen.
Navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Rechnungswesen:. 
Wechseln Sie zum Reiter :btn:Adresseingabe: und stellen Sie sicher, dass die Kontrollkästchen neben "Rechnungsadresse erfragen" und "Nach USt-ID fragen" markiert sind.
Klicken Sie zur Bestätigung den Button :btn:Speichern:.

Wenn Sie die Reverse-Charge-Funktion aktivieren möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Steuern:.
Wählen Sie die Steuer-Regel, bei der Sie die Reverse-Charge-Funktion aktivieren möchten, und wechseln Sie zum Reiter :btn:Erweitert:.
Markieren Sie das Kontrollkästchen neben "Nutze EU-Regeln zur Steuerpflicht des Leistungsempfängers (reverse charge)" und wählen Sie Ihr Land aus dem Dropdown-Menü "Land des Händlers".

Wenn Sie die Reverse-Charge-Funktion aktivieren und das Land des Händlers angeben, führt pretix folgende Schritte aus, wenn ein\*e Kund\*in eine Bestellung aufgibt:

 1. Der Shop zeigt je nach der (auf dem Reiter :btn:Allgemein:) eingestellten Steuer-Regel die Netto- oder Bruttopreise an.
 2. Der\*die Kund\*in legt ein Produkt in den Warenkorb.
    Der Shop zeigt den Bruttopreis inklusive Umsatzsteuer an.
 3. Im Schritt "Ihre Informationen" kann der\*die Kund\*in die "Rechnungsinformationen" angeben.
    Wenn die Rechnungsadresse in einem Land außerhalb der EU liegt, rechnet pretix den Umsatzsteueranteil aus dem Preis heraus.
    Wenn die Rechnungsadresse eine Geschäftsadresse in einem anderem EU-Land als dem des Händlers ist **und** eine gültige USt-ID angegeben wurde, rechnet pretix den Umsatzsteueranteil aus dem Preis heraus und fügt der Rechnung einen Hinweis auf das Reverse-Charge-Verfahren hinzu. 

Wenn der\*die Kund\*in auf den Button "Fortfahren" klickt, gleicht pretix die angegebene Umsatzsteuer-Identifikationsnummer mit dem Onlinedienst der EU zur USt-ID-Prüfung ab.
Falls der Dienst gerade nicht verfügbar ist, muss der\*die Kund\*in die Umsatzsteuer zahlen und kann sie sich später vom eigenen Staat erstatten lassen.

Falls Ihr EU-Land und das des\*der Kund\*in eine andere Währung verwendet, werden auf der Rechnung der Gesamtbetrag sowie der enthaltene Umsatzsteuerbetrag sowohl in der Währung des Veranstaltungslandes angegeben als auch in der Währung im Land des\*der Kund\*in.

Bei bestehenden Bestellungen führt eine Änderung der Rechnungsadresse **nicht** zu einer automatischen Änderung der Besteuerung.
Wenn Sie diese Änderung manuell auslösen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-shopping-cart: Bestellungen: → Alle Bestellungen: und klicken Sie eine der betreffenden Bestellungen.
Klicken Sie den Button :btn:Prüfen: neben der USt-ID.
Klicken Sie anschließend den Button :btn-icon:fa3-edit: Produkte bearbeiten:.
Wählen Sie unter "Andere Aktionen" eine der Optionen bei "Steuern neu berechnen".
Bestätigen Sie Ihre Wahl mit dem Button :btn:Änderungen durchführen:.

!!! Hinweis
    Wenn Sie den Steuerstatus mehrmals hin und her ändern, können Rundungsfehler entstehen, die um bis zu einen Cent vom vorgesehenen Preis abweichen.
    Aufgrund der flexiblen Art der Preiskalkulation lässt sich das nicht vermeiden.

### Steuer-Regeln zuweisen

![Dialogfeld Produkt hinzufügen. Die letzte Option ist das Dropdown-Menü 'Umsatzsteuer'. Ausgewählt ist 'Keine Besteuerung'. Unten auf der Seite ist ein Button mit dem Text 'Speichern und mit mehr Einstellungen fortfahren'.](../assets/screens/tax/create-product.png "Dialogfeld zum Erstellen von Produkten" )

Wenn Sie ein **neues Produkt** erstellen und diesem eine Steuer-Regel zuweisen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Produkte:. 
Klicken Sie den Button :btn-icon:fa3-plus: Neues Produkt erstellen:. 
Klicken Sie unter "Preis" das Dropdown-Menü "Umsatzsteuer" und wählen Sie die Steuer-Regel, die für das Produkt gelten soll.
Diese Liste zeigt den internen Namen und den Steuersatz, die Sie auf der Seite mit Einstellungen für die Steuer-Regel festgelegt haben.
Wenn Sie alle Optionen nach Bedarf gewählt haben, klicken Sie den Button :btn:Speichern und mit mehr Einstellungen fortfahren:.

<br>

![Dialogfeld 'Produkt bearbeiten'. Der Reiter 'Preis' wird angezeigt. Die zweite Option ist das Dropdown-Menü 'Umsatzsteuer'. Ausgewählt ist 'VAT (inkl. 19% MwSt.)'. Unten auf der Seite ist ein Button mit dem Text 'Speichern'.](../assets/screens/tax/edit-product.png "Dialogfeld zum Bearbeiten von Produkten" )

Wenn Sie einem **bestehenden Produkt** eine Steuer-Regel zuweisen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Produkte:.  
Klicken Sie den Button :btn-icon:fa3-edit:: "Bearbeiten" neben dem betreffenden Produkt und wechseln Sie zum Reiter :btn:Preis:.
Wählen Sie im Dropdown-Menü "Umsatzsteuer" die Steuer-Regel, die für das Produkt gelten soll.
Diese Liste zeigt den internen Namen, den Sie auf der Seite mit Einstellungen für die Steuer-Regel festgelegt haben, und den Steuersatz.
Wenn Sie alle Optionen nach Bedarf gewählt haben, klicken Sie den Button :btn:Speichern:.

#### Gemischte Steuersätze (Preis enthält Umsatzsteuer)

{% include "warning-tax-rules.md" %}

Dieser Abschnitt erläutert, wie Sie für ein einzelnes Produkt gemischte Steuersätze einrichten.
Das können Sie in pretix tun, indem Sie ein Produkt mit dem vollen Preis und einem Steuersatz erstellen und dann ein Produktpaket mit diesem Produkt sowie Produkten mit unterschiedlichen Steuersätzen erstellen.

!!! Hinweis
    Dieser Abschnitt geht davon aus, dass Ihr Shop Preise inklusive Umsatzsteuer anzeigt.
    Markieren Sie bei allen eigenen Steuer-Regeln das Kontrollkästchen "Der konfigurierte Produktpreis enthält den Steuerbetrag".
    Wenn Sie bei allen eigenen Steuer-Regeln die Markierung aus diesem Kontrollkästchen entfernt haben, lesen Sie den Abschnitt [Gemischte Steuersätze (Preis wird ohne Umsatzsteuer angezeigt)](taxes.md#gemischte-steuersatze-preis-wird-ohne-umsatzsteuer-angezeigt)).

Erstellen Sie ein neues Produkt.
Geben Sie ihm einen aussagekräftigen Namen und weisen Sie ihm einen der in Frage kommenden Steuersätze zu.
Welchen Steuersatz Sie wählen, ist unerheblich.
Weisen Sie diesem Produkt den Gesamtpreis zu, der sich aus der Kombination der unterschiedlich besteuerten Produkte ergibt.
Dieser Preis ist der volle Preis des Produktpakets.
Weder die Preise der anderen Produkte im Produktpaket noch die Einstellung "Ausgewiesener Preisanteil" wirken sich auf den Gesamtpreis der Kombination aus.

Erstellen Sie ein weiteres neues Produkt.
Weisen Sie ihm einen anderen Steuersatz zu.
Welchen Preis Sie diesem Produkt geben, ist unerheblich.
Wechseln Sie zum Reiter :btn:Verfügbarkeit:, markieren Sie das Kontrollkästchen neben "Dieses Produkt nicht einzeln verkaufen, sondern nur als Teil eines festen Produktpakets" und klicken Sie den Button :btn:Speichern:.
Wenn Sie in einem Produktpaket mehr als zwei unterschiedliche Steuersätze verwenden möchten, wiederholen Sie diesen Schritt für jeden weiteren Steuersatz.

Bearbeiten Sie das Ticket mit dem vollen Preis, wechseln Sie zum Reiter:btn:Enthaltene Produkte: und klicken Sie den Button :btn-icon:fa3-plus: Neues enthaltenes Produkt hinzufügen:. 
Wählen Sie unter "Enthaltenes Produkt" eines der anderen Produkte, die Sie erstellt haben, und legen Sie einen Wert für "Ausgewiesener Preisanteil" fest.
"Ausgewiesener Preisanteil" legt fest, welcher Anteil des vollen Preises für das Produktpaket mit dem Steuersatz besteuert wird, der diesem Produkt zugewiesen ist.
pretix geht davon aus, dass der Wert von "Ausgewiesener Preisanteil" bei Produkten in Produktpaketen bereits die Umsatzsteuer enthält.

Wiederholen Sie diesen Schritt für jedes Produkt mit unterschiedlichem Steuersatz, das Teil des Produktpakets sein soll.
Klicken Sie dann den Button :btn:Speichern:.

Ein Beispiel: Sie organisieren eine Weiterbildungsveranstaltung für eine Wohltätigkeitsorganisation in Deutschland und dürfen für diese Veranstaltung den Umsatzsteuersatz von 7,00 % berechnen.
Im Preis für das Zutrittsticket ist allerdings auch das Catering enthalten, für das weiterhin der reguläre Steuersatz von 19,00 % anfällt.
Steuerlich sieht das dann so aus:

 - Preis für das Ticket zur Veranstaltung: Brutto-Gesamtpreis 450 € (inklusive 150 € für Verpflegung)
    - enthält 19,63 € USt zu 7,00 %
    - enthält 23,95 € USt zu 19,00 %

Um diese Situation mit dem oben beschriebenen Verfahren abzubilden, erstellen Sie die folgenden beiden Produkte:

 - "Veranstaltungsticket" mit einem Preis von 450 € und einem Steuersatz von 7,00 %
 - "Catering" mit einem Preis von 150 €, einem Steuersatz von 19,00 % und der markierten Option "Dieses Produkt nicht einzeln verkaufen, sondern nur als Teil eines festen Produktpakets"

Wählen Sie dann das "Veranstaltungsticket" und wechseln Sie zum Reiter :btn:Enthaltene Produkte:.
Fügen Sie das Produkt "Catering" hinzu und geben Sie als "Ausgewiesener Preisanteil" 150 € ein.

Wenn ein\*e Kund\*in das Veranstaltungsticket kauft, ist das Catering als Teil des Produktpakets automatisch dabei.
Der Produktpreis von 450 € wird in zwei Teile aufgeteilt:
300 € werden mit 7,00 % besteuert und 150 € werden mit 19,00 % besteuert.

#### Gemischte Steuersätze (Preis wird ohne Umsatzsteuer angezeigt)

Dieser Abschnitt erklärt, wie Sie gemischte Steuersätze implementieren, wenn Ihr pretix-Shop Steuer-Regeln verwendet, die die Umsatzsteuer auf den angezeigten Produktpreis aufschlagen.
Gehen Sie dazu  – mit Ausnahme der Preise – vor wie unter [Gemischte Steuersätze (Preis enthält Umsatzsteuer)](taxes.md#gemischte-steuersatze-preis-enthalt-umsatzsteuer) beschrieben.
Wenn bei allen eigenen Steuer-Regeln das Kontrollkästchen "Der konfigurierte Produktpreis enthält den Steuerbetrag" nicht markiert ist, ist die Konfiguration der Preise für gemischte Steuersätze komplexer.

pretix geht davon aus, dass der Wert von "Ausgewiesener Preisanteil" bei Produkten in Produktpaketen bereits die Umsatzsteuer enthält.
Für Produkte in Produktpaketen müssen Sie den Preis inklusive Umsatzsteuer daher selbst berechnen.

Multiplizieren Sie den vorgesehenen Preis ohne Umsatzsteuer mit dem jeweiligen Steuersatz.
Addieren Sie das Ergebnis zum vorgesehenen Preis ohne Umsatzsteuer.
Bearbeiten Sie das Produkt, in dem die anderen Produkte enthalten sind.
Wechseln Sie zum Reiter :btn:Enthaltene Produkte:.
Geben Sie den errechneten Betrag (Nettopreis + Umsatzsteuer) in das Feld "Ausgewiesener Preisanteil" ein.

Wiederholen Sie diese Schritte für jedes Produkt, das im Produktpaket enthalten sein soll.
Addieren Sie alle Beträge, die Sie in die Felder "Ausgewiesener Preisanteil" eingegeben haben, zum Nettopreis des Basistickets.
Wechseln Sie anschließend zum Reiter :btn:Preis: und geben Sie das Ergebnis in das Feld "Standardpreis" ein.

### Den Algorithmus zur Berechnung der Umsatzsteuer wählen

In pretix gibt es drei verschiedene Algorithmen, um die Umsatzsteuer zu berechnen.
Welchen Sie wählen, hängt von mehreren Faktoren ab:

 - Arbeiten Sie mit E-Rechnungen gemäß EN 16931?
 - Verkaufen Sie hauptsächlich an Unternehmens- oder Privatkund\*innen?
 - Welche Rundungsmethode verwendet Ihre Steuersoftware?

Um den Algorithmus zur Rundung der Steuerbeträge zu wählen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Steuern:. 
Unter "Steuereinstellungen" finden Sie die Einstellung "Rundung der Steuern".

![Seite 'Steuern' mit dem Bereich 'Steuereinstellungen'. Für 'Rundung der Steuern' gibt es drei Optionen: 'Berechne Steuern für jede Position einzeln', 'Berechne Steuern auf Basis der Nettosumme' und 'Berechne Steuern auf Basis der Nettosumme mit konstanten Bruttopreisen'. Für die Option 'Preisanzeige für Kunden' gibt es die Optionen 'Preis inklusive Steuern' und 'Preise exklusive Steuern'. ](../assets/screens/tax/tax-settings.png "Steuereinstellungen" )

Standardmäßig ist **"Berechne Steuern für jede Position einzeln"** gewählt.
Verwenden Sie diese Option, wenn pretix die Umsatzsteuer für jede Position einzeln berechnen soll.
pretix verkauft jedes Produkt mit genau dem von Ihnen konfigurierten Netto- und Bruttopreis.
Der Netto-Gesamtbetrag einer Bestellung mit mehreren Positionen hat keine Auswirkung auf die Berechnung der Umsatzsteuer.
Wir empfehlen, diese Option zu verwenden, sofern Sie keine Software für E-Rechnungen nutzen.

Die zweite Option ist **"Berechne Steuern auf Basis der Nettosumme"**.
Verwenden Sie diese Option, wenn pretix die Umsatzsteuer anhand des Netto-Gesamtbetrags einer Bestellung berechnen soll.
pretix addiert dann die Nettopreise aller Positionen auf der Bestellung und verwendet das Ergebnis als Grundlage für die Berechnung des Umsatzsteuerbetrags.

Dieser Algorithmus ist unsere Implementierung von [EN 16931](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108971/Obtaining+a+copy+of+the+European+standard+on+eInvoicing).
Wir empfehlen, diese Option zu verwenden, wenn Sie Software für E-Rechnungen nutzen und Ihre Kundschaft überwiegend aus Unternehmen besteht.
Der Nachteil dieser Methode ist, dass Kund\*innen in Ihrem Shop damit möglicherweise durch Änderungen beim Brutto-Gesamtpreis für ihre Bestellung überrascht werden.

Die dritte Option ist **"Berechne Steuern auf Basis der Nettosumme mit konstanten Bruttopreisen"**.
Verwenden Sie diese Option, wenn pretix bei der Berechnung der Umsatzsteuer minimale Änderungen an den Nettopreisen einzelner Positionen vornehmen darf, um den vorgesehenen Brutto-Gesamtbetrag zu erhalten.

Auch dieser Algorithmus ist mit EN 16931 kompatibel.
Wir empfehlen, diese Option zu verwenden, wenn Sie Software für E-Rechnungen nutzen und Ihre Kundschaft überwiegend aus Privatpersonen besteht.
Der Vorteil ist, dass Kund\*innen in Ihrem Shop keine unerwarteten Änderungen beim Brutto-Gesamtpreis ihrer Bestellung sehen.

Der Nachteil dieser Methode ist, dass dadurch winzige Abweichungen in den Nettopreisen für einzelne Bestellpositionen entstehen können.
Dadurch kann es passieren, dass Sie ein und dasselbe Produkt zu unterschiedlichen Nettopreisen verkaufen.
Bruttopreise und Steuersätze bleiben immer dieselben.

Wenn Sie eine externe Steuersoftware verwenden, sollten Sie die Methode wählen, die der Methode entspricht, die auch Ihre Steuersoftware verwendet.
Damit beugen Sie bei Rundungen Abweichungen zwischen pretix und der externen Software vor.

Weitere Informationen über Algorithmen zur Steuerberechnung finden Sie in unserer Dokumentation für Entwickler\*innen zum Thema [Runden bei der Umsatzsteuer](https://docs.pretix.eu/dev/development/algorithms/pricing.html#rounding-of-taxes).

## Fehlerbehebung

### Die passende Steuer-Regel wird nicht im Dropdown-Menü angezeigt

Wenn Sie einem Produkt einen Steuersatz zuweisen möchten, das Dropdown-Menü "Umsatzsteuer" aber **nicht** den benötigten Steuersatz enthält, müssen Sie diesen Steuersatz zuerst anlegen.
Gehen Sie vor, wie im Abschnitt [Steuer-Regeln erstellen](taxes.md#steuer-regeln-erstellen) beschrieben, und legen Sie eine Steuer-Regel mit dem benötigten Steuersatz und einem aussagekräftigen Namen an.
Bearbeiten Sie anschließend das Produkt.
Der Steuersatz wird nun im Dropdown-Menü "Umsatzsteuer" aufgeführt und Sie können ihn dem Produkt zuweisen.

### Ein Unternehmen aus dem Ausland tätigt eine Bestellung und gibt die USt-ID nicht an

Wenn Ihr\*e Kund\*in ein ausländisches Unternehmen ist und bei der Bestellung die USt-ID nicht angibt, können Sie die betreffende Bestellung manuell bearbeiten.
Klicken Sie auf der Seite "Bestellung" die Option :btn-icon:fa3-edit: Details bearbeiten:.
Wählen Sie unter "Rechnungsinformationen" die Option "Firmenkunde oder Institution".
Auf der Seite wird nun das Feld "USt-ID-Nr." angezeigt, in das Sie die USt-ID des Unternehmens eingeben können.