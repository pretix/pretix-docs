# Produkte

Ein Produkt ist alles, was über pretix verkauft wird: Tickets, Wertgutscheine, T-Shirts und so weiter.
Wir werden in unserem Shop eine Vielzahl von Produkten anbieten.
Es ist nicht möglich, Termine festzulegen, ohne vorher die Produkte vorzubereiten, die wir zu diesen Terminen verkaufen wollen.

In diesem Artikel behandeln wir den Prozess, wie man die folgenden Produkte erstellt und in unserem Shop verfügbar macht:

- ein einfaches [Zutrittsticket](products.md#creating-and-editing-products)
- ein [Ermäßigtes Ticket](products.md#discount-ticket) für Studierende
- ein Ticket für unsere [Führung](#guided-tour-tickets) (sowie eine ermäßigte Variante)

Zunächst werden wir [Kategorien anlegen](products.md#creating-and-editing-categories), in die wir unsere Produkte einordnen können.
Anschließend erstellen wir die Produkte selbst.
Zuletzt werden wir Kontingente mit unbegrenzter Anzahl für unsere Zutrittstickets einrichten.

## Kategorien erstellen und bearbeiten

![Seite mit dem Titel "Produktkategorien", die eine Liste von Kategorien zeigt, die nur aus dem Eintrag "Tickets" besteht, sowie ein Button mit der Aufschrift "Kategorie erstellen".](../../assets/screens/products/categories.png "\"Produktkategorien\"")

Kategorien helfen uns dabei, Produkte sowohl im Backend als auch in unserem Shop in sinnvolle Gruppen einzuteilen.
Außerdem unterscheiden sie zwischen Produkten, die Kunden einzeln erwerben können, und Zusatz- sowie Cross-Selling-Produkten.
Für unser Museum benötigen wir keine Zusatz- oder Cross-Selling-Produkte, aber wir werden in unserem Shop sowohl Tickets zum Vollpreis als auch ermäßigte Tickets verkaufen.
Das bedeutet, dass unser nächster Schritt darin besteht, eine Kategorie für diese ermäßigten Tickets anzulegen.

Dazu navigieren wir zu unserer persönlichen Übersicht, indem wir oben links auf der Website :btn-icon:i-pretix: pretix.eu: klicken.
Anschließend wählen wir unsere Veranstaltungsreihe in der Liste "Ihre nächsten Veranstaltungen" aus.
Dann öffnen wir in der Seitenleiste :btn-icon:fa3-ticket: Produkte: und klicken den Unterpunkt :btn:Kategorien:. 
Diese Seite zeigt die Liste aller Produktkategorien an.
Die Liste sollte derzeit nur eine einzige Kategorie namens "Tickets" vom Typ "Normale Kategorie" enthalten.

Wir klicken den Button :btn-icon:fa3-edit:: neben der Kategorie "Ticket" in der Liste.
Wir ändern die "Bezeichnung" in \`Vollpreis-Tickets\` und klicken den Button :btn:Speichern:.

Wir navigieren zurück zur Seite "Produktkategorien".
Dort klicken wir den Button :btn-icon:fa3-plus: Kategorie erstellen: und geben der Kategorie einen Namen wie beispielsweise "Ermäßigte Tickets". Unter "Art der Kategorie" wählen wir \`Normale Kategorie\` aus.
Da wir nicht vorhaben, für unser Museum Cross-Selling zu nutzen, sind die Cross-Selling-Kategorien für uns nicht relevant.
Das Gleiche gilt für Zusatzkategorien.

Ein Klick auf den Button :btn:Speichern: am Ende der Seite bringt uns zurück zur Seite mit den Produktkategorien.
Auf dieser Seite sind nun zwei Einträge aufgeführt: "Tickets" und unsere neu erstellte Kategorie mit dem Namen "Ermäßigte Tickets".

## Produkte erstellen und bearbeiten

![Seite mit dem Titel "Produkte", die eine Liste von Produkten zeigt, die aus zwei Einträgen besteht, sowie ein Button mit der Aufschrift "Neues Produkt erstellen".](../../assets/screens/products/products.png "\"Produkte\"")

Nachdem wir die erforderlichen Kategorien für unsere Produkte angelegt haben, können wir jetzt die vorhandenen Produkte entsprechend unseren Anforderungen bearbeiten oder neue Produkte erstellen.

Zunächst bearbeiten wir das "Standard-Ticket", damit wir es als Vorlage für alle anderen Tickets verwenden können.
Dazu navigieren wir zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Produkte:.
Auf der Website sollten zwei Tickets angezeigt werden, die pretix automatisch zusammen mit der Veranstaltung angelegt hat: "Standard-Ticket" und "Reduziertes Ticket".
Wir klicken "Standard-Ticket".
Dadurch gelangen wir zum Dialogfeld "Produkt bearbeiten".

Wir ändern die deutsche Produktbezeichnung zu `Regulärer Eintritt` und geben eine englische Übersetzung an.
Wir fügen die folgende Beschreibung hinzu: `Standard-Ticket, das Eintritt in das Museum gewährt.`
Als Nächstes klicken wir den Reiter :btn:Preis: und ändern den "Standardpreis" auf 10,00 €.
Außerdem wählen wir aus dem Dropdown-Menü "Umsatzsteuer" den entsprechenden Steuersatz von 19 % aus.

{% include "note-tax-rules.md" %}

Dann klicken wir den Button :btn:Speichern:.

### Ermäßigtes Ticket

![Seite mit dem Titel "Produkt hinzufügen", die Optionen wie Produktbezeichnung, Produkt-Informationen kopieren, Produkttyp und Personalisierung zeigt.](../../assets/screens/products/create.png "\"Produkt hinzufügen\"")

Jetzt erstellen wir das ermäßigte Ticket basierend auf dem Ticket "Regulärer Eintritt", das wir im vorherigen Schritt bearbeitet haben.
Diese Vorgehensweise hat zwei Vorteile: Erstens müssen wir nicht alle Schritte wiederholen, und zweitens riskieren wir nicht, einen Schritt zu vergessen.
Das ist besonders nützlich, wenn Ihre Produkteinstellungen komplexer als in diesem Tutorial sind.

"Reduziertes Ticket" benötigen wir nicht mehr. Wir navigieren zur Seite "Produkte".
Dort klicken wir neben dem reduzierten Ticket den roten Button :btn-icon:fa3-trash:: und bestätigen, dass wir es löschen möchten.

Zurück im Produkt-Überblick klicken wir den Button :btn-icon:fa3-copy:: neben dem Ticket "Regulärer Eintritt", um es zu duplizieren.
Wir nennen das neue Ticket "Ermäßigter Eintritt" und geben eine Übersetzung ein.
Außerdem ändern wir den "Standardpreis" auf 8,00 € und klicken auf den Button :btn:Speichern:.

!!! Note
Oben auf der Seite wird nun in einem gelben Feld folgende Warnung angezeigt: "Bitte beachten Sie, dass das Produkt nicht verkauft wird, bevor Sie es zu einem bestehenden oder neuen Kontingent hinzugefügt haben."
Diese Warnung erscheint immer, wenn Sie ein neues Produkt anlegen.
Da wir uns im nächsten Abschnitt dieses Artikels damit befassen, Produkte zu Kontingenten hinzuzufügen, können wir diese Warnung vorerst ignorieren. Dadurch verschwindet die Warnung.

Auf der nächsten Seite müssen wir das Feld "Beschreibung" anpassen.
Dort informieren wir unsere Kund\*innen über die Voraussetzungen, um das ermäßigte Ticket zu erhalten.
Unsere Beschreibung lautet: "Dieses Ticket ist nur gültig, wenn Sie beim Check-in einen Studentenausweis vorlegen."

Anschließend wechseln wir zum Reiter :btn:Preis:.
Wir ändern den "Standardpreis" auf 8,00 € und den ursprünglichen Preis auf den Preis des Tickets "Regulärer Eintritt", also 10,00 €.
Unser Shop zeigt den ursprünglichen Preis durchgestrichen.
Der neue Standardpreis wird in Fettdruck und grün angezeigt, um den Preisnachlass hervorzuheben.

Anschließend wechseln wir zum Reiter :btn:Check-in \& Gültigkeit: und aktivieren das Kontrollkästchen neben "Benötigt besondere Behandlung".
Im Feld "Check-in-Hinweis" müssen wir Anweisungen für die Person bereitstellen, die den Check-in bei unserer Veranstaltung durchführt. Unsere Anweisungen lauten: `Frage nach Studierendenausweis`.
Dann klicken wir den Button :btn:Speichern:.

### Führungs-Tickets

Wir werden ein weiteres Ticket für unsere Führung erstellen.
Dazu navigieren wir zur Seite "Produkte" und klicken auf den Button :btn-icon:fa3-plus: Neues Produkt erstellen:.
Wir nennen unser neues Ticket "Führung" und geben eine englische Übersetzung an.
Unter "Kategorie" wählen wir `Vollpreis-Tickets` aus.
Wir fügen eine Beschreibung wie die folgende hinzu:

"Ticket für eine Führung.
Führungen finden jeden Montag und Mittwoch um 10 Uhr statt.
Das Ticket für die Führung gewährt Ihnen auch Zutritt zum Museum."

Anschließend ändern wir den "Standardpreis" auf 15,00 € und wählen im Dropdown-Menü "Umsatzsteuer" den entsprechenden Steuersatz von 19 % aus.
Wir lassen die übrigen Optionen auf dieser Seite unverändert.
Anschließend klicken wir den Button :btn:Speichern und mit mehr Einstellungen fortfahren:.

Anschließend navigieren wir zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Produkte.
Dort klicken wir den Button :btn-icon:fa3-copy:: neben dem "Führung"-Ticket.
Wir nennen dieses Ticket "Führung (ermäßigt)" und fügen eine englische Übersetzung hinzu.
Außerdem wählen wir die Kategorie "Ermäßigte Tickets" aus und legen den Preis auf 10,00 € fest.
Dann klicken wir den Button :btn:Speichern und mit mehr Einstellungen fortfahren:.

Am Ende dieses Vorgangs sollten wir zwei Kategorien mit jeweils zwei Tickets haben: die Kategorie "Vollpreis-Tickets" mit den Einträgen "Regulärer Eintritt" und "Führung" sowie die Kategorie "Ermäßigte Tickets" mit den Einträgen "Ermäßigter Eintritt" und "Führung (ermäßigt)".

## Kontingente erstellen und bearbeiten

Ein Kontingent legt fest, wie viele Einheiten unseres Produkts wir über unseren Shop verkaufen können.
Jedes Produkt muss Teil mindestens eines Kontingents sein, bevor es im Shop verfügbar wird.
In diesem Abschnitt werden wir Kontingente anlegen und ihnen unsere Produkte zuordnen.

Wir navigieren zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Kontingente.
Auf dieser Seite wird die Liste aller Kontingente für die Veranstaltung angezeigt.
Derzeit enthält die Liste das Kontingent "Standard-Ticket", das das Ticket "Regulärer Eintritt" als Produkt enthält, sowie das Kontingent "Ermäßigtes Ticket", das kein Ticket enthält.
Die Liste zeigt außerdem die Gesamtanzahl und die Anzahl der noch verfügbaren Plätze für jedes Kontingent an.

### Kontingente für Tickets

![Seite mit dem Titel "Kontingente", die eine Liste der Kontingente anzeigt, darunter das Kontingent für reduzierte Tickets mit einer Anzahl von 50 und das Kontingent für Standard-Tickets mit einer Anzahl von 100.](../../assets/screens/products/quotas.png "\"Kontingente\"")

Zunächst bearbeiten wir ein Kontingent für unsere regulären und unsere ermäßigten Tickets.
Es ist sinnvoll, beide Ticketarten in einem einzigen Kontingent zusammenzufassen, da wir nicht im Voraus planen können, wie viele der verkauften Tickets ermäßigte Tickets sein werden.
Wir klicken den Button :btn-icon:fa3-edit:: neben dem Kontingent "Standard-Ticket" in der Liste.
Außerdem werden wir dieses Kontingent in `Regulärer und ermäßigter Eintritt` umbenennen, um Verwechslungen zu vermeiden.
Das Ticket "Regulärer Eintritt" sollte in der Produktliste bereits ausgewählt sein.

Außerdem wählen wir in der Liste das Ticket "Ermäßigter Eintritt" aus und löschen den Eintrag im Feld "Gesamtanzahl".
Das bedeutet, dass es keine Begrenzung dafür gibt, wie viele dieser Tickets wir verkaufen können.
Wir planen, diese Eintrittskarten für die gesamte Saison 2027 zu verkaufen, nicht nur für einen einzelnen Termin.
Daher ist es nicht sinnvoll, die Gesamtanzahl zu begrenzen.

Die anderen Einstellungen lassen wir unverändert und klicken den Button :btn:Speichern:.
Dadurch gelangen wir zu einem detaillierten Überblick über den Status des Kontingents "Standard-Ticket".

Da dieses Kontingent nun sowohl die Standard- als auch die ermäßigten Zutrittstickets umfasst, benötigen wir das Kontingent "Reduziertes Ticket" nicht mehr.
Wir navigieren zurück zur Seite "Kontingente" und klicken den Button :btn-icon:fa3-trash:: neben dem Kontingent "Reduziertes Ticket".

Unser Produkt "Führung" wird Teil eines Kontingents pro Termin sein.
Wir werden diese Kontingente später zusammen mit den Terminen festlegen.

## Abschluss

Wir haben alle Tickets und sonstigen Produkte, die wir in unserem Shop verkaufen möchten, angelegt, sie in Kategorien sortiert und zwei von ihnen zu Kontingenten zugeordnet.
Im nächsten Schritt legen wir Termine fest, an denen unsere Kunden diese Produkte kaufen können.