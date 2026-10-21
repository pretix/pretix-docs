# Produkte

Ein Produkt ist alles, was über pretix verkauft wird: Tickets, Wertgutscheine, Konferenz-T-Shirts und so weiter. Wir werden in unserem Shop eine Vielzahl von Produkten anbieten. In diesem Artikel behandeln wir den Prozess, wie man die folgenden Produkte erstellt und in unserem Shop verfügbar macht:

- ein einfaches [Zutrittsticket](products.md#creating-and-editing-products)
- ein [Ermäßigtes Ticket](products.md#discount-ticket) für Studierende und Mitglieder
- ein kostenloses [Vortragenden-Ticket](products.md#speaker-ticket), das nur über einen Gutschein verfügbar ist
- [Sticker](products.md#product-with-variants) in drei Varianten mit unterschiedlichen Preisen

Zunächst werden wir [Kategorien anlegen](products.md#creating-and-editing-categories), in die wir unsere Produkte einordnen können. Anschließend erstellen wir die Produkte selbst. Zuletzt legen wir Kontingente fest, um die Verfügbarkeit für jedes Produkt festlegen und verfolgen zu können.

## Kategorien erstellen und bearbeiten

![Seite mit dem Titel "Produktkategorien", die eine Liste von Kategorien zeigt, die nur aus den Eintrag "Tickets" besteht, sowie ein Button mit der Aufschrift "Kategorie erstellen".](../../assets/screens/products/categories.png "\"Produktkategorien\"")

Kategorien helfen uns dabei, Produkte sowohl im Backend als auch in unserem Shop in sinnvolle Gruppen einzuteilen. Außerdem unterscheiden sie eigenständige Produkte von Zusatzprodukten. Neben Zutrittstickets werden wir in unserem Shop auch Extras wie Sticker verkaufen. Das bedeutet, dass unser nächster Schritt darin besteht, eine Kategorie für diese Extras anzulegen.

Dazu navigieren wir zu unserer persönlichen Übersicht, indem wir oben links auf der Website auf :btn-icon:i-pretix: pretix.eu: klicken. Anschließend wählen wir unsere Veranstaltung in der Liste "Ihre nächsten Veranstaltungen" aus. Dann öffnen wir in der Seitenleiste :btn-icon:fa3-ticket: Produkte: und klicken auf den Unterpunkt :btn:Kategorien:. Diese Seite zeigt die Liste aller Produktkategorien an. Die Liste sollte derzeit nur eine einzige Kategorie namens "Tickets" vom Typ "Normale Kategorie" enthalten.

Wir klicken auf den Button :btn-icon:fa3-plus: Kategorie erstellen: und geben der Kategorie einen Namen wie beispielsweise "Extras". Unter "Art der Kategorie" wählen wir "Zusatzprodukt-Kategorie" aus. Da wir nicht vorhaben, für diese Veranstaltung Cross-Selling zu nutzen, sind die Cross-Selling-Kategorien für uns nicht relevant. Ein Klick auf den Button :btn:Speichern: am Ende der Seite bringt uns zurück zur Seite mit den Produktkategorien. Auf dieser Seite sind nun zwei Einträge aufgeführt: "Tickets" und unsere neu erstellte Kategorie mit dem Namen "Extras".

## Produkte erstellen und bearbeiten

![Seite mit dem Titel "Produkte", die eine Liste von Produkten zeigt, die aus zwei Einträgen besteht, sowie ein Button mit der Aufschrift "Neues Produkt erstellen".](../../assets/screens/products/products.png "\"Produkte\"")

Nachdem wir die erforderlichen Kategorien für unsere Produkte angelegt haben, können wir jetzt die vorhandenen Produkte entsprechend unseren Anforderungen bearbeiten oder neue Produkte erstellen.

Zunächst bearbeiten wir das "Standard-Ticket", damit wir es als Vorlage für alle anderen Tickets verwenden können. Dazu navigieren wir zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Produkte:. Auf der Website sollten zwei Tickets angezeigt werden, die Pretix automatisch zusammen mit der Veranstaltung angelegt hat: "Standard-Ticket" und "Reduziertes Ticket". Wir klicken auf "Standard-Ticket". Dadurch gelangen wir zum Dialogfeld "Produkt bearbeiten".

Wir ändern die englische Produktbezeichnung zu `Standard Ticket` und geben eine deutsche Übersetzung an. Wir fügen folgende Beschreibung hinzu: `Regular ticket granting access to the entire conference.` Als Nächstes klicken wir auf den Reiter :btn:Preis: und ändern den "Standardpreis" auf 250,00 €. Außerdem wählen wir aus dem Dropdown-Menü "Umsatzsteuer" den entsprechenden Steuersatz von 19 % aus.

{% include "note-tax-rules.md" %}

Dann klicken wir auf den Button :btn:Speichern:.

### Ermäßigtes Ticket

![Seite mit dem Titel "Produkt hinzufügen", die Optionen wie Produktbezeichnung, Produkt-Informationen kopieren, Produkttyp und Personalisierung zeigt.](../../assets/screens/products/create.png "\"Produkt hinzufügen\"")

Jetzt erstellen wir das ermäßigte Ticket basierend auf dem "Standard-Ticket", das wir im vorherigen Schritt bearbeitet haben. Diese Vorgehensweise hat zwei Vorteile: Erstens müssen wir nicht alle Schritte wiederholen, und zweitens riskieren wir nicht, einen Schritt zu vergessen. Das ist besonders nützlich, wenn Ihre Produkteinstellungen komplexer als in diesem Tutorial sind.

Das "Reduziertes Ticket" benötigen wir nicht mehr. Wir navigieren zur Seite "Produkte". Dort klicken wir neben dem reduzierten Ticket auf den roten Button :btn-icon:fa3-trash:: und bestätigen, dass wir es löschen möchten.

Zurück im Produkt-Überblick klicken wir auf den Button :btn-icon:fa3-copy:: neben dem Standard-Ticket, um es zu duplizieren. Wir nennen das neue Ticket "Ermäßigtes Ticket" und geben eine Übersetzung ein. Außerdem ändern wir den "Standardpreis" auf 120,00 € und klicken auf den Button :btn:Speichern:.

!!! Note Oben auf der Seite wird nun in einem gelben Feld folgende Warnung angezeigt: "Bitte beachten Sie, dass das Produkt nicht verkauft wird, bevor Sie es zu einem bestehenden oder neuen Kontingent hinzugefügt haben." Diese Warnung erscheint immer, wenn Sie ein neues Produkte anlegen. Da wir uns im nächsten Abschnitt dieses Artikels damit befassen, Produkte zu Kontingenten hinzuzufügen, können wir diese Warnung vorerst ignorieren. Dadurch verschwindet die Warnung.

Auf der nächsten Seite müssen wir das Feld "Beschreibung" anpassen. Dort informieren wir unsere Kund*innen über die Voraussetzungen, um das ermäßigte Ticket zu erhalten. Unsere Beschreibung lautet: "Dieses Ticket ist nur gültig, wenn Sie beim Check-in einen Studenten- oder Mitgliedsausweis vorlegen."

Anschließend wechseln wir zum Reiter :btn:Preis:. Wir ändern den "Standardpreis" auf 120,00 € und den ursprünglichen Preis auf den Preis des Standard-Tickets, also 250,00 €. Unser Shop zeigt den ursprünglichen Preis durchgestrichen. Der neue Standardpreis wird in Fettdruck und grün angezeigt, um den Preisnachlass hervorzuheben.

Anschließend wechseln wir zum Reiter :btn:Check-in \& Gültigkeit und aktivieren das Kontrollkästchen neben "Benötigt besondere Behandlung". Im Feld "Check-in-Hinweis" müssen wir Anweisungen für die Person bereitstellen, die den Check-in bei unserer Veranstaltung durchführt. Unsere Anweisungen lauten: `Check for student ID/member ID`. Dann klicken wir auf den Button :btn:Speichern:.

### Vortragenden-Ticket

Als Nächstes erstellen wir ein kostenloses Vortragenden-Ticket, das nur über einen Gutschein erhältlich ist. Dazu navigieren wir zurück zur Seite "Produkte" :navpath:Veranstaltung →  Produkte → Produkte:. Dann klicken wir auf den Button :btn-icon:fa3-copy:: neben dem Standard-Ticket, um es zu duplizieren. Wir nennen das neue Ticket `Speaker ticket` und geben eine Übersetzung ein. Außerdem setzen wir den "Standardpreis" auf 0,00 € und lassen die übrigen Optionen auf dieser Seite unverändert. Anschließend klicken wir auf den Button :btn:Speichern und mit mehr Einstellungen fortfahren:.

Wir wechseln zum Reiter :btn:Verfügbarkeit: und aktivieren etwa in der Mitte der Seite das Kontrollkästchen neben der Option "Dieses Produkt kann nur mit einem Gutschein gekauft werden". Neben dieser Option befindet sich ein Umschalter mit einem Augen- und einem Informationssymbol: :btn-icon:fa3-eye-slash:: :btn-icon:fa3-info::. Wir stellen diesen Umschalter auf :btn-icon:fa3-eye-slash:: mit dem Tooltip "Verstecke das Produkt, wenn es nicht verfügbar ist" ein. Das bedeutet, dass der Shop das Ticket nur den Personen anzeigt, die über einen entsprechenden Gutschein verfügen. Sobald wir das Kontrollkästchen und den Umschalter eingestellt haben, klicken wir auf den Button :btn:Speichern:.

Wir planen, unseren geladenen Vortragenden Gutscheincodes zuzusenden, mit denen sie Zugang zu dieser speziellen Art von Ticket erhalten. Weitere Informationen zu Gutscheinen finden Sie unter [Gutscheine](../../guides/vouchers.md).

### Produktvarianten

![Seite mit dem Titel "Produkt bearbeiten: Sticker", die auf dem Reiter "Varianten" geöffnet ist. Sie zeigt die Einstellungen für die Variante "Standard": Variante (Name), Standard- und ursprünglicher Preis, Beschreibung.](../../assets/screens/products/products.png "\"Produktvarianten\"")

Nachdem wir alle benötigten Zutrittsprodukte angelegt haben, erstellen wir jetzt ein Sticker-Produkt mit mehreren Varianten: lila, schwarz und glitzernd. Es ist nicht möglich, ein Produkt ohne Varianten in ein Produkt mit mehreren Varianten umzuwandeln. Daher navigieren wir zur Seite "Produkte" und klicken auf den Button :btn-icon:fa3-plus: Neues Produkt erstellen:.

Wir nennen das Produkt "Sticker", legen es als "Kein Zutrittsprodukt" fest und ordnen es der Kategorie "Extras" zu. Unter "Produktvarianten" wählen wir "Produkt mit mehreren Varianten" aus. Wir legen den Standardpreis auf 5,00 € fest. Dann klicken wir auf den Button :btn:Speichern und mit mehr Einstellungen fortfahren:.

Als Nächstes öffnen wir den Reiter :btn:Varianten:. pretix zeigt diesen Reiter nur an, wenn wir bei der Erstellung des Produkts "Produkt mit mehreren Varianten" ausgewählt haben. Hier sollte eine Variante mit dem Namen `Standard` angezeigt werden. Wir klicken auf den Namen, um die Einstellungen für diese Variante zu erweitern, und ändern den Namen in `Purple`. Weitere Einstellungen müssen hier nicht geändert werden.

Anschließend scrollen wir nach unten und klicken auf den Button :btn-icon:fa3-plus: Neue Variante hinzufügen:. Wir geben dieser neuen Variante den Namen `Black` und lassen die übrigen Einstellungen unverändert. Diesen Vorgang wiederholen wir für die Variante `Glitter` und setzen den "Standardpreis" für diese Variante auf 7,50 €. Dann klicken wir auf den Button :btn:Speichern:.

## Kontingente erstellen und bearbeiten

Ein Kontingent legt fest, wie viele Einheiten unseres Produkts wir über unseren Shop verkaufen können. Jedes Produkt muss Teil mindestens eines Kontingents sein, bevor es im Shop verfügbar wird. In diesem Abschnitt werden wir Kontingente anlegen und ihnen unsere Produkte zuordnen.

Wir navigieren zu :navpath:Veranstaltung → :fa3-ticket: Produkte → Kontingente. Auf dieser Seite wird die Liste aller Kontingente für die Veranstaltung angezeigt. Derzeit umfasst diese das Kontingent "Standard-Ticket", das das Standard-Ticket als Produkt enthält, sowie das Kontingent "Ermäßigtes Ticket", das kein Ticket enthält. Die Liste zeigt außerdem die Gesamtkapazität und die Anzahl der noch verfügbaren Plätze für jedes Kontingent an.

### Kontingente für Tickets

![Seite mit dem Titel "Kontingente", die eine Liste der Kontingente anzeigt, darunter das Kontingent für reduzierte Tickets mit einer Kapazität von 50 und das Kontingent für Standard-Tickets mit einer Kapazität von 100.](../../assets/screens/products/quotas.png "\"Kontingente\"")

Zunächst bearbeiten wir ein Kontingent für unsere Standard- und unsere ermäßigten Tickets. Es ist sinnvoll, beide Ticketarten in einem einzigen Kontingent zusammenzufassen, da wir nicht im Voraus planen können, wie viele der verkauften Tickets ermäßigte Tickets sein werden. Wir klicken auf den Button :btn-icon:fa3-edit:: neben dem Kontingent "Standard-Ticket" in der Liste. Außerdem werden wir dieses Kontingent in `Standard and discount ticket` umbenennen, um Verwechslungen zu vermeiden. Das "Standard-Ticket" sollte in der Produktliste bereits ausgewählt sein.

Wir wählen außerdem "Ermäßigtes Ticket" in der Liste aus und ändern die Kapazität auf 1900. Das ist die maximale Anzahl an Tickets dieser Art, die wir verkaufen möchten. Unser Veranstaltungsort bietet Platz für 2000 Personen, von denen 100 Referenten sein werden. Die anderen Einstellungen lassen wir unverändert und klicken auf den Button :btn:Speichern:. Dadurch gelangen wir zu einem detaillierten Überblick über den Status des Kontingents "Standard-Ticket".

Da dieses Kontingent nun sowohl die Standard- als auch die ermäßigten Tickets umfasst, benötigen wir das Kontingent "Reduziertes Ticket" nicht mehr. Wir navigieren zurück zur Seite "Kontingente" und klicken auf den Button :btn-icon:fa3-trash:: neben dem Kontingent "Reduziertes Ticket".

Auch unser Vortragenden-Ticket müssen wir einem Kontingent zuweisen. Dazu navigieren wir erneut zur Seite "Kontingente" und klicken auf den Button :btn-icon:fa3-plus: Kontingent erstellen:. Wir geben dem neuen Kontingent den Namen `Speaker ticket` und legen die Anzahl auf 100 fest. Das entspricht der erwarteten Anzahl der Referenten bei unserer Veranstaltung. In der Produktliste aktivieren wir das Kontrollkästchen neben "Vortragenden-Ticket". Dann klicken wir auf den Button :btn:Speichern:.

### Kontingente für Produktvarianten

Für unser Sticker-Produkt benötigen wir drei verschiedene Kontingente: eines für jede Produktvariante. Dazu navigieren wir erneut zur Seite "Kontingente" und klicken auf den Button :btn-icon:fa3-plus: Kontingent erstellen:. Wir nennen das neue Kontingent "Sticker lila" und legen die Gesamtkapazität auf 100 fest. Das ist die Anzahl der Sticker in dieser Farbe, die wir verkaufen können.

Anschließend wählen wir "Aufkleber – Lila" aus der Produktliste aus. Der lila Sticker ist kein Zutrittsticket, sondern ein Zusatzprodukt, das Kunden im selben Shop erwerben können. Wir möchten nicht, dass dieses Kontingent zur Gesamtanzahl der für die Veranstaltung verfügbaren Tickets hinzugerechnet wird. Daher aktivieren wir das Kontrollkästchen neben "Ignoriere dieses Kontingent für die Gesamt-Verfügbarkeit der Veranstaltung". Dann klicken wir auf den Button :btn:Speichern:.

Da wir noch Kontingente für die anderen Varianten des Produkts benötigen, navigieren wir zurück zur Seite "Kontingente" und klicken auf den Button :btn-icon:fa3-copy:: neben dem Sticker-Kontingent, das wir im vorherigen Schritt erstellt haben. Wir nennen das neue Kontingent `Sticker Black`, deaktivieren "Sticker – Lila" in der Produktliste und wählen stattdessen "Sticker – Schwarz" aus. Abschließend klicken wir auf :btn:Speichern: und wiederholen denselben Vorgang für die Farbe "Glitzernd". Die Gesamtkapazität passen wir dabei nach Bedarf an.

Jetzt navigieren wir zurück zur Seite "Produkte", öffnen das Produkt "Sticker" und klicken auf den Reiter :btn:Varianten:. Es sollten nun keine gelben Felder mehr angezeigt werden, die uns darauf hinweisen, dass wir das Produkt und die Varianten zu einem Kontingent hinzufügen müssen, bevor wir sie verkaufen können.

## Abschluss

Wir haben alle Tickets und sonstigen Produkte, die wir in unserem Shop verkaufen möchten, angelegt, sie in Kategorien sortiert und Kontingenten zugeordnet. Nun können wir damit fortfahren, die [Zahlungsmethoden einzurichten](payment.md), mit denen unsere Kund*innen diese Produkte erwerben können.