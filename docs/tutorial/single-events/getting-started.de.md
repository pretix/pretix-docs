# Erste Schritte

Willkommen beim pretix-Tutorial!
In diesem Tutorial durchlaufen wir alle Schritte, die für unsere allererste Veranstaltung mit pretix notwendig sind.
Zur Veranschaulichung erstellen wir eine einfache Konferenz.
Wir werden konkrete Beispiele für unseren Veranstalter, die Veranstaltung und die Produkte sowie deren Namen und Preise verwenden.
Ersetzen Sie diese Beispiele gerne durch Ihre eigenen, wenn Sie Ihre Veranstaltung entsprechend Ihren Anforderungen erstellen.

!!! Note
    Dieses Tutorial erklärt die Einrichtung eines Shops für **Einzelveranstaltungen** wie Konferenzen, Conventions, Messen, Konzerte oder Festivals.
    Wenn Sie einen Ticket-Shop für eine Einrichtung mit Dauerbetrieb wie ein öffentliches Schwimmbad, einen Freizeitpark oder ein Museum erstellen möchten, sollten Sie sich stattdessen das Tutorial für den [fortlaufenden Betrieb](../continuous-operation/getting-started.md) ansehen.

pretix ist quelloffene Software.
Sie können sie entweder in der Cloud oder auf Ihrem eigenen Server nutzen.
Der Betrieb von pretix auf Ihrem eigenen Server erfordert einige technische Kenntnisse.
Wenn Sie pretix selbst hosten möchten, lesen Sie unsere [Dokumentation zum Selbsthosten](https://docs.pretix.eu/self-hosting/).
Dieses Tutorial befasst sich mit der einfacheren Methode: der Nutzung unseres cloudbasierten Angebots pretix Hosted.

Hier ist ein kurzer Überblick über die Schritte, die wir in diesem Tutorial durchführen werden:

- ein [persönliches Konto](#ein-konto-erstellen) und ein Veranstalterkonto erstellen
- unser [Veranstalterkonto](organizer-account.de.md) einrichten
- unsere [Veranstaltung](event.de.md) erstellen
- [Produkte](products.de.md) (Tickets und Werbeartikel) für unsere Veranstaltung erstellen
- [Zahlungsmethoden](payment.de.md) einrichten
- unseren Shop [testen](testing.de.md) und finale Anpassungen vornehmen

## Ein Konto erstellen

Bevor wir mit pretix arbeiten können, müssen wir ein Konto erstellen.
Die gute Nachricht: Ein Konto zu erstellen ist __völlig kostenlos__.
Sie gehen damit keinerlei Verpflichtung ein, in Zukunft für die Nutzung von pretix zu bezahlen.
Wir können nach Herzenslust mit der pretix-Software experimentieren, bevor wir entscheiden, ob pretix die richtige Wahl für uns ist.
Kosten entstehen erst beim Verkauf von echten Tickets.

!!! Note
    Falls Ihre Firma, Ihre Organisation oder Ihre Institution bereits über ein Veranstalterkonto verfügt, dann müssen Sie kein neues Konto anlegen.
    Sie können stattdessen Ihre Mitveranstaltenden bitten, Ihnen eine Einladung zu senden und Sie zum Team hinzuzufügen.
    Eine Anleitung dazu, wie Sie jemanden in ein Team einladen können, finden Sie in unserem [Guide zum Thema Teams](../../guides/teams.md#inviting-someone-to-your-team).

![pretix.eu, eine Webseite, auf der pretix und dessen wichtigsten Funktionen vorgestellt werden. Auf der rechten Seite befindet sich ein Button mit der Aufschrift "Ticketshop erstellen".](../../assets/screens/account/pretix-eu.de.png "pretix.eu")

Um ein Konto zu erstellen, klicken wir auf der Webseite [pretix.eu](https://pretix.eu/about/de/ "https://pretix.eu/about/de") den Button :btn:Ticketshop erstellen:.
Dadurch gelangen wir zu einer neuen Seite, auf der wir in der linken Spalte die Daten für unser persönliches pretix-Konto eingeben.
In der rechten Spalte geben wir dann den Namen und die Kurzform unseres Veranstalters ein.

<br>

![Pretix.eu, Seite "Erste Schritte" mit Eingabefeldern für Kontoinformationen sowie den Namen und die Kurzform des Veranstalters](../../assets/screens/account/pretix-create-account.png "pretix.eu/about/de/setup")

Für unser persönliches Konto geben wir unseren Namen, unsere E-Mail-Adresse und ein sicheres Passwort an.
Das Feld oben links ist für den Namen der Person vorgesehen, der das Konto gehört, **nicht** für einen Firmennamen.
Wir werden einen Namen auswählen, anhand dessen uns unsere Mitveranstaltenden erkennen und mit dem das pretix-Supportteam uns ansprechen kann.
In diesem Tutorial lautet unser Name Maxi Musterperson.

Jedes Teammitglied sollte einen eigenen persönlichen Login haben.
Wenn auch andere Mitglieder unseres Teams Zugriff auf das System haben sollen, können wir sie im weiteren Verlauf [einladen](../../guides/teams.md#inviting-someone-to-your-team).

!!! Warning
    Die Kurzform ist der eindeutige Identifikator Ihrer Firma im pretix-Backend.
    pretix wird sie auch in der Shop-URL verwenden.
    Wählen Sie die Kurzform sorgfältig aus.
    Bestätigen Sie Ihre Eingabe erst dann, wenn Sie mit Ihrer Auswahl zufrieden sind.

    Wenn Sie eine andere Kurzform benutzen wollen, dann müssen Sie ein neues Veranstalterkonto erstellen.
    If you want to use a different short form, then you will have to create a new organizer account.

Das Feld "Veranstaltername" ist für den Namen der Firma, der Organisation oder der Institution vorgesehen, in deren Namen wir die Veranstaltungen organisieren möchten.
Das Feld "Kurzform/Adresse" ist für die Kurzform des Names der Organisation vorgesehen.
pretix wird diese Kurzform für die URL verwenden, unter der Kunden unsere Veranstaltungen finden können.

In diesem Tutorial werden wir ein Konto für unsere Firma "Tutorial Ltd." anlegen.
Dazu geben wir "Tutorial Ltd." in das Feld "Veranstaltername" und "tut" in das Feld "Kurzform/Adresse" ein.
Das bedeutet, dass das Profil unseres Veranstalters und alle Veranstaltungen, die wir in Zukunft organisieren werden, ab sofort unter [https://pretix.eu/tut/](https://pretix.eu/tut/) zu finden sind.

Es ist **nicht** nötig, zuerst ein Testkonto anzulegen oder das Wort "Test" in der Kurzform oder im Namen zu verwenden.
Unsere Shops bleiben so lange für die Öffentlichkeit unsichtbar, bis wir sie manuell veröffentlichen.
Bis dahin haben wir trotzdem schon Zugriff auf alle Funktionen und Einstellungen.

Wenn wir von Anfang an den offiziellen Namen unserer Organisation für das Konto verwenden, können wir sicherstellen, dass wir unsere bevorzugte URL nutzen können.
Außerdem vermeiden wir so, dass wir dieselben Anpassungen an zwei verschiedenen Konten vornehmen müssen.
Bis wir beschließen, unsere Veranstaltungen zu veröffentlichen, sind sie für die Öffentlichkeit nicht sichtbar
pretix GmbH wird uns bis zu diesem Zeitpunkt auch keine Gebühren in Rechnung stellen.

{% include "note-short-form.de.md" %}

Sowohl die [Datenschutzerklärung](https://pretix.eu/about/de/privacy) als auch die [Nutzungsbedingungen](https://pretix.eu/about/de/terms) sind auf dieser Seite verlinkt.
Es ist eine Voraussetzung für die Nutzung von pretix, diese Texte sorgfältig zu lesen, ihnen zustimmen und die entsprechenden Kontrollkästchen aktivieren.

Wir klicken jetzt auf den Button :btn:Speichern und weiter: und machen damit den ersten Schritt zur Einrichtung unserer ersten Veranstaltung mit pretix.
Als Nächstes richten wir unser [Veranstalterkonto](organizer-account.de.md) ein.