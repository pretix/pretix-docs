# Veranstaltung

Nachdem Sie ein Veranstalterkonto eingerichtet haben, ist der nächste Schritt, eine Veranstaltung zu erstellen. 
Dieser Artikel beschreibt, wie Sie eine Veranstaltung anlegen und grundlegend einrichten. 
Hier ist ein kurzer Überblick über die Schritte, die wir in diesem Abschnitt durchführen werden:

- [eine Veranstaltung erstellen](event.md#event-creation)
- sich auf der Übersicht über den Status der Veranstaltung [einen Überblick verschaffen](event.md#event-level-dashboard)
- die Erfassung von [Daten zu Kund\*innen- und Teilnehmer\*innen](event.md#customer-and-attendee-data) aktivieren
- dem Ticketshop [Bilder hinzufügen](event.md#shop-design)

Das sind alle notwendigen Schritte, um eine Veranstaltung zu erstellen. 
Im nächsten Artikel dieses Tutorials werden wir dann damit fortfahren, unsere Produkte an unsere Bedürfnisse anzupassen.

## Eine Veranstaltung erstellen

Um eine Veranstaltung zu erstellen, müssen wir uns zuerst mit unserem [pretix-Konto](https://pretix.eu/control/) anmelden. 
Anschließend gelangen wir durch einen Klick auf den Button :btn:pretix.eu: in der oberen linken Ecke der Webseite zur Übersicht. 
Dort erhalten wir einen Überblick über unsere nächsten Veranstaltungen. 
Jetzt klicken wir auf den Button :btn-icon:fa3-plus:Neue Veranstaltung erstellen:.

<br>

![Seite mit dem Titel "Neue Veranstaltung erstellen – Schritt 1", die Optionen zur Auswahl eines Veranstalterkontos, der Veranstaltungsart sowie der Sprachen zeigt.](../../assets/screens/event/create-event1.png "\"Neue Veranstaltung erstellen Schritt 1\"")

Da eine Veranstaltung in pretix immer mit einem Veranstalterkonto verknüpft ist, müssen wir hier eines auswählen. 
Wir wählen den Veranstalter aus, der diese Veranstaltung ausrichtet. 
In diesem Fall ist das der, den wir im vorherigen Schritt dieses Tutorials eingerichtet haben. 
Diese Auswahl können wir nicht mehr ändern, sobald wir die Veranstaltung erstellt haben. 
Daher müssen wir sicherstellen, dass wir hier das richtige Veranstalterkonto auswählen.

Wenn unser Konto nur auf ein einziges Veranstalterkonto Zugriff hat, wählt pretix dieses Veranstalterkonto automatisch für dieses Feld aus.

Als Nächstes müssen wir die Veranstaltungsart auswählen. 
Es gibt zwei Optionen: "Einzelveranstaltung oder Shop, der keine Veranstaltung ist" und "Veranstaltungsreihe oder Zeitslotbuchung". 
Für dieses Tutorial möchten wir eine einfache Konferenz erstellen, die an einem einzigen Wochenende stattfindet. 
Daher wählen wir die Option "Einzelveranstaltung oder Shop, der keine Veranstaltung ist".

Wir legen fest, welche Sprachen für die Veranstaltung verwendet werden sollen. 
Standardmäßig sollten die Sprachen aktiv sein, die wir bei der Einrichtung des Veranstalterkontos ausgewählt haben. 
Wir werden Sprachen nach Bedarf aktivieren oder deaktivieren.

Es ist zwar möglich, Sprachen später hinzuzufügen oder zu entfernen, wir werden unsere Entscheidung jedoch jetzt endgültig treffen. 
So behalten wir den Überblick darüber, welche Übersetzungen wir noch hinzufügen müssen, beispielsweise für die Beschreibung unserer Veranstaltung.

Sobald wir mit unserer Auswahl zufrieden sind, klicken wir auf den Button :btn:Weiter:.

{% include "note-translations.md" %}

![Seite mit dem Titel "Neue Veranstaltung erstellen – Schritt 2", die Optionen zur Auswahl von Veranstaltungstitel, Kurzform, Datum, Veranstaltungsort und Geo-Koordinaten für die Veranstaltung zeigt. 
Nicht abgebildet: Veranstaltungswährung, Umsatzsteuersatz, Zeitzone und Start- und Enddatum des Vorverkaufs.](../../assets/screens/event/create-event2.png "\"Neue Veranstaltung erstellen Schritt 2\"")

Wir werden nun aufgefordert, einen Titel und eine Kurzform für die Veranstaltung anzugeben. 
Für dieses Tutorial erstellen wir eine einfache Konferenz, die im Jahr 2027 stattfindet. 
Deshalb wählen wir im Feld "Veranstaltungstitel" den Titel "Tutorial-Konferenz". 
Für das Feld "Kurzform" denken wir uns eine Abkürzung für "Tutorial-Konferenz" aus. 
Außerdem fügen wir die letzten beiden Ziffern des Jahres hinzu.

In das Feld geben wir `tutcon27` ein. 
pretix fügt die Kurzform an die URL des Veranstalters an. 
In unserem Fall ergibt sich daraus die folgende URL: https://pretix.eu/tut/tutcon27

{% include "note-short-form.md" %}

Genau wie der Name und die Kurzform ist auch der Veranstaltungsbeginn eine Pflichtangabe. 
Wir geben den 4. 
Juni 2027 in das Feld "Veranstaltungsbeginn" ein.

Da wir unseren Veranstaltungsort bereits kennen, geben wir diesen nun in pretix ein. 
Diese Angabe ist optional. 
Wir können sie später noch ändern. 
pretix verwendet unsere Eingabe im Feld "Veranstaltungsort", um in OpenStreetMap nach diesem Ort zu suchen.

Wenn pretix den Ort findet, werden die Felder "Geo-Koordinaten" automatisch ausgefüllt. 
Außerdem wird die Kartenvorschau auf diesen Ort zentriert. 
Wenn keine Ergebnisse für die Eingabe gefunden werden, können wir die Markierung auf der Karte manuell an den Veranstaltungsort ziehen. 
Dadurch werden die Felder "Geo-Koordinaten" automatisch aktualisiert. 
Alternativ können wir die erweiterte Suchfunktion auf [OpenStreetMap.org](https://www.openstreetmap.org) nutzen und die Koordinaten in die Felder "Geo-Koordinaten" kopieren.

Wir müssen eine Währung für unsere Veranstaltung auswählen. 
Wir klicken auf das Dropdown-Menü "Veranstaltungswährung" und wählen `Euro`.

Auf dieser Seite können wir außerdem einen Umsatzsteuersatz für unsere Veranstaltung festlegen. 
Es ist möglich, die Steuer-Regeln zu ändern, nachdem wir die Veranstaltung bereits angelegt haben. 
Wir richten unsere Veranstaltung in Deutschland aus, und für alle unsere Produkte gilt ein einheitlicher Prozentsatz. 
Daher werden wir hier eine Steuer-Regel von 19 % hinzufügen.

{% include "note-tax-rules.md" %}

Sobald wir mit unserer Auswahl zufrieden sind, klicken wir auf den Button :btn:Weiter:.

{% include "warning-tax-rules.md" %}

<br>

![Seite mit dem Titel "Neue Veranstaltung erstellen – Schritt 3", die eine Infobox zeigt, in der der Benutzer aufgefordert wird, alle Einstellungen sorgfältig zu überprüfen. 
Außerdem gibt es die Option, Einstellungen aus einer zuvor erstellten Veranstaltung zu importieren.](../../assets/screens/event/create-event3.png "\"Neue Veranstaltung erstellen Schritt 3\"")

Anschließend werden wir gefragt, ob wir Informationen aus einer zuvor erstellten Veranstaltung kopieren möchten. 
Diese Option kann uns ab der zweiten Veranstaltung viel Arbeit ersparen. 
Da dies aber die erste Veranstaltung ist, die wir mit diesem Veranstalterkonto organisieren, behalten wir die Standardeinstellung ("_Nicht übernehmen_") bei und klicken auf :btn:Weiter:.

<br>

![Seite mit dem Titel "Herzlichen Glückwunsch! Sie haben gerade eine Veranstaltung erstellt!", die Optionen zur Erstellung von Ticketarten und zur Aktivierung einiger grundlegender Funktionen für die Veranstaltung zeigt. 
Nicht abgebildet: Zahlungsoptionen einrichten und Kontaktdaten angeben.](../../assets/screens/event/create-event4.png "\"Neue Veranstaltung erstellen Schritt 4\"")

Auf der nächsten Seite werden wir zur Erstellung unserer Veranstaltung beglückwünscht. 
Hier haben wir außerdem die Möglichkeit, schnelle Änderungen an den Produkten und den Grundeinstellungen für die Veranstaltung vorzunehmen. 
Diese Schnelleinstellungen müssen wir im Moment nicht anpassen. 
Die Produkte (Tickets, Wertgutscheine, usw.) werden wir im [nächsten Abschnitt](products.md) dieses Tutorials genauer betrachten.

Im Feld "Kontakt-E-Mail" geben wir eine allgemeine E-Mail-Adresse an, unter der unsere Kund*innen uns erreichen können. 
Diese E-Mail-Adresse wird in der Fußzeile unserer Shop-Seite mit der Bezeichnung "Kontakt" angezeigt. 
Außerdem geben wir im Feld "Impressum (URL)" eine URL zu den rechtlichen Impressumsangaben für den Online-Auftritt unserer Organisation an. 
Diese beiden Angaben sind zwingend erforderlich, damit unser Ticket-Shop veröffentlicht werden kann.

Sobald wir unten auf der Seite auf :btn:Speichern: klicken, leitet uns pretix zu einem Überblick über die Veranstaltung weiter. 
Dieser Überblick enthält den Veranstaltungstitel und die Zeitpläne für den Ticket- und den Vorverkauf. 
Außerdem können wir den Status unseres Ticketshops sehen. 
Der Ticketshop sollte sich zu diesem Zeitpunkt im Testmodus befinden.

## Veranstaltungs-Übersicht

Nachdem wir unsere Veranstaltung erstellt haben, stehen uns jetzt alle möglichen Optionen für die Veranstaltung zur Verfügung. 
Wir können die Veranstaltungs-Übersicht aufrufen, indem wir oben links auf den Button :btn:pretix.eu: klicken und anschließend unsere Veranstaltung in der Liste "Ihre nächsten Veranstaltungen" auswählen. 
Die Veranstaltungs-Übersicht gibt uns einen Überblick über die grundlegenden Informationen und den Status der Veranstaltung. 
Sie ermöglicht uns, interne Kommentare für uns selbst oder unser Team zu hinterlassen, und protokolliert die letzten Änderungen.

![Screenshot der Übersicht für eine Beispielveranstaltung mit dem Titel "Tutorial-Konferenz", der den Veranstaltungstitel, Buttons zum Teilen der Veranstaltung, den Zeitplan, eine Übersicht über Bestellungen, Zahlungen und verbleibende Tickets sowie ein Feld für interne Kommentare zeigt. 
Nicht abgebildet: Veranstaltungs-Protokolle zu den letzten Änderungen.](../../assets/screens/event/event-dashboard.png "\"Veranstaltungs-Übersicht\"")

Derzeit wird in der Übersicht wahrscheinlich eine Warnung angezeigt, dass unser Veranstalterkonto noch nicht aktiv ist. 
Wenn wir diese Warnung zum ersten Mal sehen, klicken wir auf den Link und geben die erforderlichen Informationen in das Formular ein.

Die Aktivierung eines Kontos erfolgt manuell und kann je nach Verfügbarkeit des pretix-Teams einige Zeit in Anspruch nehmen. 
Das Team wird unser Konto am folgenden Werktag aktivieren. 
Bis dahin bleibt die Warnung bestehen, auch wenn wir bereits alle erforderlichen Angaben gemacht haben.

## Kunden- und Teilnehmerdaten

Wir planen, vor der Konferenz Namensschilder für unsere Teilnehmer*innen zu drucken. 
Dazu müssen wir beim Kauf die Namen und Zugehörigkeit unserer Teilnehmer*innen erfassen.

In der Veranstaltungs-Übersicht klicken wir in der Seitenleiste auf :btn-icon:fa3-wrench: Einstellungen:. 
Dadurch gelangen wir zur Seite mit den allgemeinen Einstellungen für die Veranstaltung. 
Wir öffnen oben den Reiter :btn:Kunden- und Teilnehmerdaten:. 
Mit den Optionen auf diesem Reiter können wir Fragen zu bestimmten Informationen für jedes gekaufte Ticket einrichten. 
Wir scrollen nach unten zur Zwischenüberschrift "Teilnehmerdaten (einmal pro personalisiertem Ticket)".

Wir setzen "Name Teilnehmer\*in" auf "Fragen, Eingabe ist verpflichtend" und die Option "Teilnehmer\*innen-Firma" auf "Fragen, aber Eingabe ist optional". 
Im Textfeld "Erklärung zu Teilnehmerdatenerfassung" fügen wir eine Erklärung hinzu, warum wir die betreffenden Daten erfassen. 
Unsere Erklärung lautet wie folgt: "Wir verwenden den von Ihnen angegebenen Namen und Titel sowie die Firma für Ihr Namensschild."

Unter "Formular-Einstellungen" können wir das Format auswählen, in dem pretix die Teilnehmer nach Namen und Titeln fragt. 
Wir wählen `Ask for Title + Given name + Family name, display like Dr John Doe` für Namen und `Free text input` für Titel. 
Wenn Sie diese Einstellungen ändern, nachdem bereits Bestellungen eingegangen sind, kann dies zu Problemen beim Sortieren oder Ändern von Namen führen. 
Daher legen wir unsere Auswahl hier endgültig fest, bevor wir den Ticketshop veröffentlichen.

Um diese Einstellungen zu speichern, klicken wir auf den Button :btn:Speichern:.

## Shop-Design

![Screenshot des Reiters "Shop-Design", der Optionen für das Header-Bild und das Social-Media-Bild sowie einen gesperrten Bereich am unteren Rand zeigt.](../../assets/screens/event/shop-design.png "\"Veranstaltung Shop-Design\"")

Wenn wir oben auf den Reiter "Shop-Design" wechseln, können wir Bilder zu unserem Ticketshop hinzufügen und dessen Farben anpassen. 
Ein Klick auf den Button :btn-icon:fa3-eye:Shop aufrufen: in der Leiste oben führt uns zu einer Vorschau des Shops aus Sicht der Kund*innen. 
Eine mit Pretix Hosted erstellter Shop ist standardmäßig unter https://pretix.eu/:placeholder:OrganizerShortForm:/:placeholder:EventShortForm:/ zu finden. 
Der Shop, den wir für dieses Tutorial erstellen, befindet sich unter [https://pretix.eu/tut/tutcon27/](https://pretix.eu/tut/tutcon27/).

Standardmäßig wird in der Kopfzeile unseres Shops der Name der Veranstaltung angezeigt. 
Über die Einstellungen des Shop-Designs können wir den Titel durch ein Header-Bild ersetzen, das unsere Kund*innen über die Veranstaltung informiert (beispielsweise durch den Veranstaltungstitel, das Logo oder ein eindeutiges Design).

Wir fügen das Header-Bild hinzu, indem wir auf den Button :btn:Durchsuchen…: neben der Option "Header-Bild" klicken. 
Dort wählen wir von unserem Computer eine PNG-Datei mit einer Auflösung von 1140 × 120 Pixel aus. 
Standardmäßig ersetzt das Header-Bild den Titel der Veranstaltung oben auf der Seite. 
Wir möchten den Veranstaltungstitel jedoch weiterhin anzeigen. 
Daher aktivieren wir das Kontrollkästchen neben "Veranstaltungs-Titel auch anzeigen, obwohl ein Header-Bild hochgeladen wurde".

Außerdem laden wir eine PNG-Datei für die Option "Social-Media-Bild" hoch. 
pretix verwendet dieses Bild als Vorschau für alle Links zu unserem Ticket-Shop, die wir auf Social Media veröffentlichen. 
Wenn wir hier keine Datei hochladen, verwendet pretix stattdessen das Header-Bild für die Vorschau.

Alle Änderungen, die wir auf dieser Seite vornehmen, werden erst im Ticketshop sichtbar, nachdem wir auf den Button :btn:Speichern: geklickt haben.

## Abschluss

Wir haben den vierstufigen Prozess zur Erstellung einer Veranstaltung durchlaufen, uns auf der Veranstaltungs-Übersicht einen Überblick über den Status der Veranstaltung verschafft, die Erfassung von Kunden- und Teilnehmerdaten aktiviert und Bilder zum Ticketshop hinzugefügt. 
Nun können wir dazu übergehen, [Produkte zu erstellen](products.md), die wir in unserem Shop verkaufen möchten.