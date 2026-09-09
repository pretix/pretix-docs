# Rabatte

pretix bietet verschiedene Verfahren, mit denen Sie Ihren Kund/*innen unter bestimmten Voraussetzungen Rabatte anbieten können.
Dieser Artikel erklärt die verschiedenen Arten von Rabatten für bestimmte Anwendungsfälle:

 - [Unterschiedliche Preisniveaus](discounts.md#different-price-levels)
 - [Gruppentarife](discounts.md#group-discounts-and-discounts-for-large-orders)
 - [Frühbucherpreise](discounts.md#early-bird-tickets)
 - [Rabattpakete](discounts.md#discount-packages)

## Voraussetzungen

Die meisten hier beschriebenen Verfahren greifen auf Veranstaltungsebene, Sie müssen also zuerst eine Veranstaltung anlegen.
Da dieser Artikel voraussetzt, dass Sie in Grundzügen mit dem Erstellen und Bearbeiten von Produkten vertraut sind, sollten Sie sich zuerst den Guide über [Produkte](index.md) ansehen.
Die Implementierung von [Rabattpaketen](discounts.md#discount-packages) setzt Kenntnisse über Check-in-Listen voraus.

## Anleitung

In pretix können Sie so viele verschiedene Produkte mit unterschiedlichen Preisniveaus anlegen, wie Sie benötigen.
Wie Sie dazu vorgehen, ist im Abschnitt [Unterschiedliche Preisniveaus](discounts.md#different-price-levels) erklärt.
Die anschließenden Abschnitte erläutern die anspruchsvolleren Verfahren, um abhängig von bestimmten Bedingungen Rabatte anzubieten, nämlich [Frühbucherpreise](discounts.md#early-bird-tickets), [Rabattpakete](discounts.md#discount-packages) und [Gruppentarife](discounts.md#group-discounts-and-discounts-for-large-orders).

### Unterschiedliche Preisniveaus

Am einfachsten können Sie einen Rabatt gewähren, indem Sie zwei oder mehr Zutrittsprodukte mit unterschiedlichen Preisniveaus erstellen.
Das bietet sich beispielsweise an, wenn Sie Tickets für Menschen mit Altersrente oder für Studierende rabattieren.
Dazu legen Sie zuerst das Standard-Zutrittsticket an und konfigurieren es wie gewünscht.

Anschließend klonen Sie das Ticket einmal für jedes weitere Preisniveau.
Passen Sie Name und Preis jedes geklonten Tickets an.
Geben Sie in das Feld "Beschreibung" einen erläuternden Text ein, etwa folgendermaßen:
"Dieses Ticket ist nur gültig, wenn Sie während des Check-ins einen Studierendenausweis vorlegen."
Wechseln Sie zum Reiter :btn:Check-in & Gültigkeit: und geben Sie einen "Check-in-Hinweis" mit Anweisungen für die Person ein, die das Ticket scannt, zum Beispiel:
"Studierendenausweis prüfen".

Fügen Sie alle Produkte einem allgemeinen Kontingent hinzu.
Legen Sie die Kapazität des Kontingents auf die Höchstzahl der Tickets fest, die Sie verkaufen möchten.

Wenn Sie die Anzahl der verfügbaren ermäßigten Tickets weiter begrenzen möchten, erstellen Sie ein weiteres Kontingent und legen Sie dessen Kapazität auf die Höchstzahl der Tickets fest, die Sie mit Rabatt verkaufen möchten.
Fügen Sie diesem Kontingent nur die ermäßigten Tickets hinzu.
pretix rechnet jedes mit Rabatt verkaufte Ticket auf beide Kontingente an, jedes verkaufte Standardticket nur auf das allgemeine Kontingent.

### Gruppentarife und Rabatte für Großbestellungen

pretix bietet Ihnen unabhängig vom gekauften Produkt verschiedene Verfahren, um Rabatte für Großbestellungen einzurichten.
Dies kann auch praktisch sein, um Gruppentarife anzubieten.
Sie können Ermäßigungen mit einer Mindestbestellmenge verknüpfen, eine Regel für Rabatte erstellen, die unter bestimmten Bedingungen beim Kauf automatisch angewendet wird, oder feste Gruppenpakete zu ermäßigten Preisen anbieten.
Die folgenden Unterabschnitte erläutern die jeweiligen Verfahren.

#### Mindestbestellmenge

Sie können die Funktion für Mindestbestellmengen nutzen, um Werbung für ermäßigte Gruppentickets zu machen.
Dazu erstellen Sie ein Ticket für eine Person zu einem reduzierten Preis.
Über die Option "Minimale Anzahl pro Bestellung" definieren Sie die Mindestgröße der Gruppe, ab der Sie den Rabatt gewähren möchten.

Ein Beispiel: Ihr Standard-Zutrittsticket kostet 20,00 €.
Klonen Sie dieses Ticket, nennen Sie es beispielsweise "Ermäßigtes Ticket für Gruppen ab fünf Personen" und legen Sie den Preis auf 15,00 € fest.
Speichern Sie das Ticket und bearbeiten Sie es.
Wechseln Sie zum Reiter :btn:Verfügbarkeit: und legen Sie die "Minimale Anzahl pro Bestellung" auf 5 fest.
So müssen Kund/*innen mindestens fünf der ermäßigten Tickets gleichzeitig kaufen.

#### Mengenrabatte

Mit der Funktion "Automatischer Rabatt" können Sie auf eine Bestellung automatisch einen Mengenrabatt gewähren, wenn die Bestellung eine bestimmte Bedingung erfüllt: Sie enthält entweder eine Mindestanzahl Produkte oder hat einen Brutto-Mindestwert.

Um dies einzurichten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-ticket: Produkte → Rabatte: und klicken den Button :btn-icon:fa3-plus: Neuen Rabatt erstellen:.
Füllen Sie für den Rabatt das Feld "Interner Name" aus.

Wenn der Rabatt nur für ausgewählte Produkte gelten soll, entfernen Sie den Haken aus dem Kontrollkästchen neben "Anwendbar für alle Produkte (inkl. neu erstellter Produkte)" und kreuzen Sie unter "Auf bestimmte Produkte anwenden" die betreffenden Tickets an.
Das ist nützlich, wenn der Rabatt beispielsweise nur für Zutrittstickets gelten soll.

Um einen Rabatt-Prozentsatz festzulegen, etwa "25 Prozent Rabatt beim Kauf von mindestens 5", legen Sie für "Minimale Anzahl passender Produkte" 5 und für "Prozentualer Rabatt auf passende Produkte" 25,00 fest.

Um einen Rabatt in der Art "6 zum Preis von 5" festzulegen, legen Sie für "Minimale Anzahl passender Produkte" 5 fest, für "Prozentualer Rabatt auf passende Produkte" 100,00 und für "Gewähre Rabatt nur für diese Anzahl passender Produkte" 1.

Wenn für den Rabatt der Bruttowert und nicht die Anzahl gekaufter Produkte maßgeblich sein soll, lassen Sie das Feld "Minimale Anzahl passender Produkte" leer und setzen Sie "Minimaler Brutto-Gesamtbetrag passender Produkte" auf den gewünschten Wert.

Klicken Sie zur Bestätigung den Button :btn:Speichern:.

#### Feste Gruppenpakete

Sie können Produktpakete nutzen, um Gruppentickets in festen Paketen zu verkaufen, beispielsweise für einen Achtertisch beim Galadinner.

Dazu erstellen Sie zuerst ein Standard-Zutrittsticket für eine einzelne Person und ein dazugehöriges Kontingent.
Dann erstellen Sie ein Produkt, das nicht zum Zutritt berechtigt und dessen Preis geringer ist als der volle Preis für acht Einzeltickets.
Rufen Sie den Reiter :btn:Enthaltene Produkte: für dieses Produkt auf und klicken Sie den Button :btn-icon:fa3-plus: Neues enthaltenes Produkt hinzufügen:.
Wählen Sie das Standard-Zutrittsticket als "Enthaltenes Produkt", legen Sie für "Menge" 8 fest und klicken Sie den Button :btn:Speichern.

Erstellen Sie ein Kontingent, das nur das Paket für acht Personen enthält.
Dieses Kontingent kann eine unbegrenzte Kapazität haben.

Diese Konfiguration bewirkt, dass pretix bei jedem Kauf eines dieser Produktpakete acht Einzeltickets anlegt.
So wird die korrekte Anzahl vom Kontingent für das Grundprodukt abgezogen und auf der Check-in-Liste werden acht neue Einträge für Teilnehmer/*innen angelegt.
Wenn Sie die persönlichen Daten der einzelnen Teilnehmer/*innen benötigen, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Allgemein:, wechseln Sie zum Reiter :btn:Kunden- und Teilnehmerdaten: und bearbeiten Sie die Einstellungen unter "Teilnehmerdaten (einmal pro personalisiertem Ticket)".

### Frühbuchertickets

Dieser Abschnitt erläutert, wie Sie Frühbuchertickets anbieten, die nur weit vor der Veranstaltung bis zu einem bestimmten Datum erhältlich sind, ab dem nur noch teurere Tickets angeboten werden.
Sie können ein Ticket anlegen und den Preis manuell heraufsetzen, je näher die Veranstaltung rückt.

pretix bietet aber auch zwei Verfahren, dies zu automatisieren:
Unterschiedliche Preisklassen können Sie je nach Datum anbieten oder abhängig von den noch verfügbaren Tickets.
In beiden Fällen erstellen Sie zuerst ein Zutrittsticket für jede Preisklasse.

#### Zeitabhängige Frühbuchertickets für Einzelveranstaltungen

Wenn Sie abhängig vom Zeitpunkt Frühbuchertickets für eine Einzelveranstaltung anbieten möchten, bearbeiten Sie eines der Produkte und wechseln Sie zum Reiter :btn:Verfügbarkeit:.
Definieren Sie dort anhand der Felder "Verfügbar ab" und "Verfügbar bis" den Zeitraum, in dem das Produkt gekauft werden kann.
Wiederholen Sie diesen Schritt für jedes Produkt.

Vergewissern Sie sich, dass das Feld "Verfügbar bis" für das erste Ticket denselben Zeitpunkt mit Datum und Uhrzeit angibt wie das Feld "Verfügbar ab" des folgenden Tickets.
Damit verhindern Sie Überlappungen, in denen phasenweise mehr als eine Preisgruppe verfügbar ist, und ebenso Lücken, in denen gar keine Tickets verfügbar sind.

#### Zeitabhängige Frühbuchertickets für Termine in einer Veranstaltungsreihe

Die oben beschriebene Vorgehensweise funktioniert nicht bei einer Veranstaltungsreihe, deren Termine über einen längeren Zeitraum verteilt sind.
Wenn Sie zeitabhängige Frühbuchertickets auf der Grundlage des Termins in einer Veranstaltungsreihe anbieten möchten, navigieren Sie zu :navpath:Ihre Veranstaltungsreihe → :fa3-calendar: Termine: und bearbeiten Sie einen der Termine.
Definieren Sie unter "Produkteinstellungen" anhand der Felder "Verfügbar ab" und "Verfügbar bis" den Zeitraum, in dem das Produkt für genau diesen Termin gekauft werden kann.

Wenn Sie für mehrere Termine dieselbe Verfügbarkeit festlegen möchten, navigieren Sie zu :navpath:Ihre Veranstaltungsreihe → :fa3-calendar: Termine:, markieren Sie das Kontrollkästchen neben den betreffenden Terminen und klicken Sie den Button :btn-icon:fa3-edit: Ausgewählte bearbeiten:.
Definieren Sie unter "Produktpreise" anhand der Felder "Verfügbar ab" und "Verfügbar bis" den Zeitraum, in dem das Produkt für die gewählten Termine gekauft werden kann.
Markieren Sie die Felder "ändern" neben "Verfügbar ab" und "Verfügbar bis", damit die Produkteinstellungen auch sicher überschrieben werden.

#### Frühbuchertickets anhand der Ticketmenge

Wenn Sie abhängig von der Anzahl der bereits verkauften Tickets für eine Einzelveranstaltung Frühbuchertickets anbieten möchten, erstellen Sie für jedes Preisniveau ein Kontingent.
Geben Sie für alle Preisklassen außer der letzten eine feste Anzahl in das Feld "Gesamtanzahl" ein und markieren Sie das Kontrollkästchen neben "Dieses Kontingent schließen, sobald es einmal ausverkauft war".
Das hat folgende Wirkung: Sobald eine Preisklasse ausverkauft ist, bietet der Shop **keine** frühere Preisklasse mehr an, selbst wenn Bestellungen storniert werden und wieder im Kontingent vorhanden sind.
Bei dieser Vorgehensweise müssen Sie für das letzte Kontingent **nicht** die Option "Dieses Kontingent schließen, sobald es einmal ausverkauft war" aktivieren.

Wenn Sie vorhaben, nur eine begrenzte Anzahl Tickets zu verkaufen, etwa weil der Veranstaltungsort nur begrenzten Platz bietet, legen Sie für die "Gesamtanzahl" des letzten Kontingents einen Wert fest.
Die Summe der "Gesamtanzahl"-Werte aller Kontingente darf nicht höher sein als die Gesamtzahl der Tickets, die Sie verkaufen möchten.

Fügen Sie dem ersten Kontingent nur das erste Produkt hinzu.
Fügen Sie das erste **und** das zweite Produkt dem zweiten Kontingent hinzu und legen Sie dessen Gesamtanzahl so fest, dass sie gleich der Summe des ersten Kontingents und der zu verkaufenden Anzahl der zweiten Tickets ist.
Gehen Sie in dieser Weise vor bis zum letzten Kontingent, das alle relevanten Produkte enthalten sollte.
Diese Kontingent-Konstruktion bewirkt, dass Sie auch dann die maximale Anzahl Tickets für Ihre Veranstaltung verkaufen können, wenn Ticket-Bestellungen aus früheren Kontingenten storniert werden.

Navigieren Sie zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Produkte: und bearbeiten Sie das zweite Produkt in der Sequenz.
Wechseln Sie zum Reiter :btn:Verfügbarkeit:.
Wählen Sie unter "Nicht anzeigen, wenn Kontingent verfügbar" das erste Kontingent.
Wiederholen Sie dieses Vorgehen für jedes weitere Produkt und wählen Sie jedes Mal das vorherige Kontingent.
Das bewirkt, dass jede Preisklasse im Shop nur angezeigt wird, wenn die vorherige Preisklasse ausverkauft ist, das Kontingent also ausgeschöpft ist.

Wenn Sie die Preise für frühere Ticket-Preisklassen verbergen möchten, navigieren Sie zu :navpath:Ihre Veranstaltung → :fa3-wrench: Einstellungen → Allgemein: und wechseln Sie zum Reiter :btn:Anzeige:.
Markieren Sie bei "Produktliste" das Kontrollkästchen bei "Verstecke alle ausverkauften Produkte".

!!! Hinweis
    In seltenen Fällen kann es vorkommen, dass die Preise in Ihrem Shop zwischen Preisklassen hin- und herspringen.
    Wenn ein/*e Kund/*in die letzten Produkte einer Preisklasse in den Warenkorb legt, aber noch nicht kauft, werden diese Tickets als "Reserviert" gekennzeichnet und die nächste Preisklasse wird angezeigt.
    Schließt der/*die Kund/*in den Kauf dann aber nicht ab, werden die zuvor reservierten Tickets wieder im Shop angezeigt und die Tickets der nächsten Preisklasse werden nicht mehr angezeigt.

    Dieses Verhalten ist einer Situation vorzuziehen, in der ein/*e Benutzer/*in mit bösen Absichten alle Tickets einer günstigeren Preisklasse reservieren kann, ohne sie zu kaufen.

Ein Beispiel: Angenommen, Sie möchten 400 Tickets in drei Preisklassen verkaufen.
Zuerst erstellen Sie drei Produkte mit unterschiedlichen Preisen:

 - "Extrem-Frühbucherticket"
 - "Frühbucherticket"
 - "Standardticket"

Dann erstellten Sie drei Kontingente:

 - "Extrem-Frühbucher" mit einer Gesamtanzahl von 100 und Wahl des Produkts "Extrem-Frühbucherticket".
 - "Frühbucher und billiger" mit einer Gesamtanzahl von 200 und Wahl der Produkte "Extrem-Frühbucherticket" und "Frühbucherticket".
 - "Alle Gäste" mit einer Gesamtanzahl von 400, Wahl aller drei Produkte und keine weitere gewählten Optionen.

Anschließend ändern Sie das Produkt "Standardticket" und wechseln zum Reiter :btn:Verfügbarkeit:.
Wählen Sie unter "Nicht anzeigen, wenn Kontingent verfügbar" Ihr Kontingent "Frühbucher und billiger".
Gehen Sie ebenso vor für das "Frühbucherticket" mit dem Kontingent "Extrem-Frühbucherticket".

### Rabattpakete

Dieser Abschnitt erläutert, wie Sie mehrere kombinierte Produkte zu einem geringeren Preis anbieten, als sie einzeln kosten würden.
Das ist nützlich, wenn Sie mehrere Produkte anbieten, Ihre Kund/*innen voraussichtlich unterschiedliche Kombinationen dieser Produkte kaufen werden und Sie für umfangreichere Kombinationen günstigere Preise anbieten möchten.
Das kann zum Beispiel in den folgenden Szenarios der Fall sein:

 - Eine Messe oder ein Festival läuft über drei aufeinanderfolgende Tage und die Karten für einen, zwei oder drei Tage haben unterschiedliche Preise.
 - Sie bieten unterschiedlich große Merch-Pakete an, wobei größere Pakete günstiger sind.
 - Verschiedene Angebote, etwa Präsenz-Workshops, Online-Inhalte und eine Netzwerkveranstaltung, sind günstiger, wenn sie in Kombination gekauft werden.

Sie können dies in pretix auf zwei Weisen umsetzen:
Eine Möglichkeit sind [Produktkombinationen](discounts.md#option-a-combination-products).
Sie haben den Vorteil, dass Ihre Produkte und Bestellmöglichkeiten einigermaßen überschaubar bleiben.
Diese Möglichkeit kommt allerdings nur in Frage, wenn es maximal drei oder vier Grundprodukte gibt.

Die andere Möglichkeit sind [Zusatzprodukte und Produktpakete](discounts.md#option-b-add-ons-and-bundles).
Diese Option ist zunächst deutlich komplexer, aber mit einer steigenden Anzahl von Grundprodukten wächst diese Komplexität nicht exponentiell, wie es bei der ersten Möglichkeit der Fall ist.

Generell ist die erste Möglichkeit besser geeignet, wenn Sie nur wenige Grundprodukte haben, und die zweite Möglichkeit ist ab einer Anzahl von vier oder fünf Grundprodukten sinnvoller.
Die folgenden Abschnitte erläutern beide Möglichkeiten.

Wenn Sie unabhängig von den gekauften Produkten einen Rabatt für größere Bestellungen gewähren möchten, lesen Sie stattdessen den Abschnitt über [Gruppentarife und Rabatte für Großbestellungen](discounts.md#group-discounts-and-discounts-for-large-orders).

#### Option A: Produktkombinationen

Eine Möglichkeit besteht darin, Grundprodukte und Kontingente zu erstellen und anschließend separate Produkte für alle möglichen Kombinationen der Grundprodukte anzulegen.
Dies hat den Vorteil, dass Ihre Produkte und Bestellmöglichkeiten einigermaßen überschaubar bleiben.
Sie können diese Möglichkeit ohne die Funktionen für Zusatzprodukte oder Produktpakete umsetzen.

Allerdings ist sie nur nutzbar, wenn die Gesamtzahl der möglichen Kombinationen recht klein ist.
Die Anzahl der Produkte, die Sie in Ihrem Shop anbieten müssen, ist `2ⁿ-1`, wobei `n` die Anzahl der Grundprodukte ist.
Mit jedem weiteren Grundprodukt steigt diese Anzahl exponentiell:
Wenn Sie drei Grundprodukte haben, müssen Sie auf diese Weise sieben Produkte im Shop anbieten.
Wenn Sie vier Grundprodukte haben, sind es schon fünfzehn Produkte.
Ab einem solchen Komplexitätsgrad sind vermutlich die unten beschriebenen [Produktpakete](discounts.md#option-b-add-ons-and-bundles) eine besser geeignete Möglichkeit.

Ein Beispiel: Sie veranstalten eine dreitägige Messe.
Legen Sie für jeden Messetag ein Grundticket an, drei Kombinationstickets für je zwei Tage und ein Kombinationsticket für alle drei Tage:

 - Ticket Tag 1
 - Ticket Tag 2
 - Ticket Tag 3
 - Ticket Tag 1 + Tag 2
 - Ticket Tag 1 + Tag 3
 - Ticket Tag 2 + Tag 3
 - Ticket für alle drei Tage

Erstellen Sie dann drei Kontingente, jedes mit der maximalen Kapazität des Veranstaltungsorts an jedem einzelnen Tag als Gesamtanzahl:

 - Kontingent Tag 1, verknüpft mit "Ticket Tag 1", "Ticket Tag 1 + Tag 2", "Ticket Tag 1 + Tag 3" und "Ticket für alle drei Tage"
 - Kontingent Tag 2, verknüpft mit "Ticket Tag 2", "Ticket Tag 1 + Tag 2", "Ticket Tag 2 + Tag 3" und "Ticket für alle drei Tage"
 - Kontingent Tag 3, verknüpft mit "Ticket Tag 3", "Ticket Tag 1 + Tag 3", "Ticket Tag 2 + Tag 3" und "Ticket für alle drei Tage"

So können alle Teilnehmer/*innen genau ein Ticket bestellen, mit dem sie an allen gewünschten Tagen Zutritt haben.
Zum Schluss navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-check-square-o: Check-in:.
Hier bearbeiten oder erstellen Sie eine Check-in-Liste mit den von Ihnen angelegten Tickets und wechseln zum Reiter :btn:Erweitert:.
Definieren Sie eigene Check-in-Regeln, sodass die Tickets aus dem ersten Kontingent am ersten Tag der Veranstaltung gültig sind, die Tickets aus dem zweiten Kontingent am zweiten Tag und die Tickets aus dem dritten Kontingent am dritten Tag.

Dazu verwenden Sie die Bedingung "Aktueller Tag der Woche" oder die Bedingung "Aktueller Zeitpunkt".
Die Check-in-Regel sollte ungefähr so aussehen wie auf dem unten gezeigten Screenshot.
Die Logik ist wie folgt:

Mindestens eine der folgenden Bedingungen (ODER)

 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 1", "Ticket Tag 1 + Tag 2", "Ticket Tag 1 + Tag 3" oder "Ticket für alle drei Tage"
    - Aktueller Tag der Woche = 1 (Montag)
 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 2", "Ticket Tag 1 + Tag 2", "Ticket Tag 2 + Tag 3" oder "Ticket für alle drei Tage"
    - Aktueller Tag der Woche = 2 (Dienstag)
 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 3", "Ticket Tag 1 + Tag 3", "Ticket Tag 2 + Tag 3" oder "Ticket für alle drei Tage"
    - Aktueller Tag der Woche = 3 (Mittwoch)

![Eigene Check-in-Regel mit drei Blöcken von UND-Bedingungen. Der erste verlangt, dass das Produkt eines der Produkte für Tag 1 ist UND dass der aktuelle Wochentag Montag ist. Der zweite und der dritte Block verlangen dasselbe für Tag 2 und Dienstag beziehungsweise für Tag 3 und Mittwoch. Die drei Blöcke von UND-Bedingungen sind Teil einer ODER-Bedingung.](../../assets/screens/products/check-in-rules-combination-products.png "Eigene Check-in-Regel")

#### Option B: Zusatzprodukte und Produktpakete

Eine andere Möglichkeit besteht darin, Grundprodukte und Kontingente zu erstellen und anschließend für alle möglichen Kombinationen Produkte mit obligatorischen Zusatzprodukten anzulegen.
Eine Ausnahme bildet die Produktkombination mit **allen** Grundprodukten.
Die komplette Produktkombination können Sie entweder einrichten wie oben im Abschnitt [Option A: Produktkombinationen](discounts.md#option-a-combination-products) beschrieben oder als Produktpaket.
Die Einrichtung als Produktpaket wird auch in diesem Abschnitt erläutert.

Diese Option hat den Vorteil, dass die Anzahl der benötigten Produkte nicht exponentiell zur Anzahl der Grundprodukte wächst.
Ihr wesentlicher Nachteil ist, dass Bestellungen komplexer werden, weil jede Bestellung eines Produkts mit obligatorischen Zusatzprodukten mindestens drei Produkte enthält.

Ein Beispiel: Sie veranstalten eine dreitägige Messe.
Erstellen Sie zuerst eine Kategorie für "Tagestickets".
Legen Sie dann für jeden Messetag ein Standard-Zutrittsticket an, ein nicht zum Zutritt berechtigendes Produkt für eine beliebige Kombination aus zwei Tagen und ein nicht zum Zutritt berechtigendes Produkt für alle drei Tage:

 - Ticket Tag 1
 - Ticket Tag 2
 - Ticket Tag 3
 - Ticket für zwei Tage
 - Ticket für alle drei Tage

Fügen Sie die Tickets für Tag 1, 2 und 3 der Kategorie "Tagestickets" hinzu.
Fügen Sie dieser Kategorie **keine** anderen Tickets hinzu.
Erstellen Sie nun ein Kontingent für jedes der Zutrittstickets.
Wenn Sie die Kontingente für die einzelnen Tagestickets erstellen, geben Sie als "Gesamtanzahl" den Wert ein, der der Kapazität Ihres Veranstaltungsorts an jedem Tag entspricht.
Die Kontingente für die Tickets für zwei und drei Tage können unbegrenzt sein.

Bearbeiten Sie das "Ticket für zwei Tage", wechseln Sie zum Reiter :btn:Zusatzprodukte: und klicken Sie den Button :btn-icon:fa3-plus: Weitere Kategorie hinzufügen:.
Wählen Sie die Kategorie "Tagestickets", legen Sie die minimale und die maximale Anzahl auf 2 fest und markieren Sie das Kontrollkästchen "Zusatzprodukte sind im Preis enthalten".
Klicken Sie den Button :btn:Speichern:.
Mit dieser Konfiguration wird ein/*e Kund/*in beim Kauf eines "Tickets für zwei Tage" aufgefordert, dem Warenkorb zwei Tickets aus der Kategorie "Tagesticket" als Zusatzprodukte hinzuzufügen.
Der/*die Kund/*in erhält zwei Tickets: eines für jeden gewählten Tag der Veranstaltung.

Es ist nicht sinnvoll, das "Ticket für alle drei Tage" ebenso einzurichten, weil der/*die Kund/*in dann alle drei Tagestickets von Hand wählen müsste.
Wenn Sie das "Ticket für alle drei Tage" als Produktpaket einrichten möchten, bearbeiten Sie es und wechseln Sie zum Reiter :btn:Enthaltene Produkte:.
Klicken Sie den Button :btn-icon:fa3-plus: Neues enthaltenes Produkt hinzufügen:.
Wählen Sie als "Enthaltenes Produkt" das "Ticket Tag 1".
Lassen Sie die "Menge" bei 1 und "Ausgewiesener Preisanteil" bei 0,00.
Wiederholen Sie dies für das "Ticket Tag 2" und das "Ticket Tag 3".

Diese Konfiguration bewirkt, dass beim Kauf eines "Tickets für alle drei Tage" die drei Tagestickets automatisch kostenlos dem Warenkorb hinzugefügt werden.
Der/*die Kund/*in erhält drei Tickets: eines für jeden Tag der Veranstaltung.

Zum Schluss navigieren Sie zu :navpath:Ihre Veranstaltung →  :fa3-check-square-o: Check-in:.
Hier bearbeiten oder erstellen Sie eine Check-in-Liste mit den von Ihnen angelegten Tickets und wechseln zum Reiter :btn:Erweitert:.
Definieren Sie eigene Check-in-Regeln, sodass das "Ticket Tag 1" nur am ersten Tag der Veranstaltung gültig ist, das "Ticket Tag 2" nur am zweiten Tag und das "Ticket Tag 3" nur am dritten Tag.
Falls Sie das "Ticket für alle drei Tage" als Produktkombination gestaltet haben, definieren Sie die Regel so, dass es auch an jedem Tag gültig ist.
Dazu verwenden Sie die Bedingung "Aktueller Tag der Woche" oder die Bedingung "Aktueller Zeitpunkt".
Die Logik ist wie folgt:

Mindestens eine der folgenden Bedingungen (ODER)

 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 1" oder "Ticket für alle drei Tage"
    - Aktueller Tag der Woche = 1 (Montag)
 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 2" oder "Ticket für alle drei Tage"
    - Aktueller Tag der Woche = 2 (Dienstag)
 - Alle der folgenden Bedingungen (UND)
    - Produkt ist eines von "Ticket Tag 3"
    - Aktueller Tag der Woche = 3 (Mittwoch)

!!! Hinweis
    Sie können das "Ticket für alle drei Tage" auch wie im Abschnitt [Option A: Produktkombinationen](discounts.md#option-a-combination-products) beschrieben einrichten.
    Führen Sie dieses Ticket in dem Fall bei jeder Bedingung auf, die mit "Produkt ist eines von" beginnt.
