# Barrierefreiheit

Die Barrierefreiheit Ihres pretix-Ticketshops ist nicht nur aus ethischen und unternehmerischen Gründen von Bedeutung, sondern auch eine rechtliche Verpflichtung.
Ab 2025 legen der [European Accessibility Act](https://en.wikipedia.org/wiki/European_Accessibility_Act) und seine nationalen Ausführungsgesetze (in Deutschland das [Barrierefreiheitsstärkungsgesetz](https://www.bmas.de/SharedDocs/Downloads/DE/Gesetze/barrierefreiheitsstaerkungsgesetz) und in Österreich das [Barrierefreiheitsgesetz](https://www.ris.bka.gv.at/eli/bgbl/i/2023/76/P0/NOR40254410)) fest, dass alle Websites, über die Verträge mit Verbraucher\*innen geschlossen werden, bestimmten Barrierefreiheitsstandards entsprechen müssen.

Wenn Sie einen Online-Shop betreiben, über den Sie Produkte oder Dienstleistungen an Verbraucher\*innen in der EU verkaufen, dann sind diese Gesetze auf Sie anwendbar. 
Das schließt Ticketshops mit ein, die mit pretix erstellt wurden. 

Die entsprechende europäische Norm [EN 301 549](https://en.wikipedia.org/wiki/EN_301_549) verweist auf den Standard [WCAG 2.1 AA](https://de.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines).
Deshalb entwickeln wir pretix so, dass es für Sie ein Leichtes ist, die Auflagen von **WCAG 2.1/2.2 AA** mit Ihrem Ticketshop zu erfüllen. 

## Ihre Verantwortung

pretix ist kein Ticketshop, sondern eine Software für die Erstellung von Ticketshops.
Die tatsächliche Barrierefreiheit des Shops ergibt sich daher aus unseren Bemühungen bei der Erstellung der Software einerseits und Ihren Bemühungen bei der Konfiguration andererseits. 
Es liegt in Ihrer Verantwortung, die Konfiguration für pretix so zu wählen, dass sie den Anforderungen der Barrierefreiheit entspricht.
Das beinhaltet unter anderem:

- Verwenden Sie benutzerkonfigurierte Farben, die [gut unterscheidbar](https://www.w3.org/TR/WCAG22/#use-of-color) sind und [ausreichenden Kontrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) zu den umgebenden Farben bieten.

- Bieten Sie alle Informationen, die Sie [als Bilder](https://www.w3.org/TR/WCAG22/#images-of-text) präsentieren (z. B. das Kopfzeilenbild oder Produktbilder), auch als Text auf derselben Seite an. 

- Wenn Sie formatierten Text mit [Markdown](../guides/markdown.md) auf Ihre Shopseite stellen, achten Sie auf semantisch korrekte Verwendung des Markups. 
Wir empfehlen, keine Überschriften (``##``) oder HTML-Tags zu verwenden. 

- Wählen Sie Zahlungsanbieter, die gute Unterstützung für Barrierefreiheit bieten.

- Achten Sie beim Einbetten des [Widgets](../guides/widget.md) darauf, dass das CSS-Styling auf der einbettenden Website die Barrierefreiheit nicht beeinträchtigt.
Gestalten Sie den Navigationspfad zum Widget ebenfalls barrierefrei. 

## Information zur Barrierefreiheit

Abhängig von den für Sie geltenden Gesetzen müssen Sie möglicherweise Informationen über die Barrierefreiheit Ihres Ticketshops veröffentlichen.
Sie können diese Informationen einbetten, indem Sie die Konfigurationsoptionen unter :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Allgemein → Barrierefreiheit: nutzen.

Hier ist ein Markdown-formatiertes Beispiel, das auf den Anforderungen des deutschen Rechts für eine nicht-staatliche Einrichtung basiert.

!!! Warning 
    Die pretix-Dokumentation stellt keine Rechtsberatung dar. 
    Die nachfolgenden Informationen werden **ohne Gewähr** zur Verfügung gestellt. 
    Die Verwendung erfolgt auf eigene Gefahr.

```
TODO
```

## Barrierefreiheits-Tests

Externe Expert\*innen haben die Barrierefreiheit mehrerer Beispielshops getestet. 
Die letzte Testrunde fand zwischen November 2024 und Mai 2025 statt.

!!! Note

    Unser Engagement für Barrierefreiheit gilt momentan nur für die mit pretix erstellten Ticketshops.
    Wir arbeiten an der Verbesserung der Barrierefreiheit des pretix-Backends. 
    Allerdings haben wir noch keine intensiven Barrierefreiheits-Tests durchgeführt oder das Backend entsprechend aktualisiert. 
    Unsere derzeitige Priorität sind die Ticketshops. 

### Umfang der Tests

Aufgrund der komplexen und hochgradig konfigurierbaren Natur von pretix ist es unmöglich, alle möglichen Konfigurationen zu testen.
Daher haben wir den Test an Beispiel-Ticketshops durchgeführt und versucht, möglichst viele Features und Konfigurationen von pretix einzubeziehen.
Wenn eine Konfiguration, ein Plugin oder ein Prozess hier nicht aufgeführt ist, dann haben wir den entsprechenden Aspekt nicht extern auf Barrierefreiheit testen lassen.
Wenn Sie den Nachweis der Barrierefreiheit für Ihren individuellen pretix-Ticketshop benötigen, müssen Sie Ihre eigenen Tests durchführen.

Die Barrierefreiheits-Tests umfassten **alle Kernfunktionen des Systems** sowie die folgenden Erweiterungen:

- Banküberweisung
- Double-Opt-In Schritt 
- Passbook-Tickets
- PDF-Ticketausgabe
- rapidmail (beispielhaft für Newsletter-Integration)
- Seiten
- Sitzplätze
- Versand

Wir haben folgende Features von pretix auf Barrierefreiheit getestet: 

#### Organizer-Seiten

- Umschalten der Sprache der Webseite.
- Erkundung der Veranstaltungsliste durch Listen- und Kalenderansichten.
- Kontaktaufnahme mit dem Veranstalter.
- Anlegen eines Kundenkontos.
- Anmeldung mit einem Kundenkonto. 
- Zurücksetzen des Passworts eines Kundenkontos.
- Ändern von Informationen in einem Kundenkonto. 
- Anzeigen von Mitgliedschaften, letzten Bestellungen, gespeicherten Adressen sowie Profilen.

#### Veranstaltungsseiten

- Navigation der Termine einer Veranstaltungsreihe.
- Auffinden aller Veranstaltungsinformationen (Datum, Uhrzeit, Ort, Beschreibung).
- Auffinden und Navigieren der Produktliste, einschließlich ermäßigter Tickets, ausverkaufter Tickets, Tickets mit Varianten, Tickets mit Warteliste und Tickets, die einen Gutschein erfordern.
- Auffinden und Navigieren des Sitzplans.
- Eintragung in die Warteliste für ein ausverkauftes Ticket.
- Hinzufügen von Tickets zum Warenkorb. 
- Benutzung des Warenkorbs. 
- Auswählen von Zusatz- und Cross-Selling-Produkten.
- Einloggen in ein bestehendes Kundenkonto. 
- Erstellen eines neuen Kundenkontos. 
- Fortfahren ohne Kundenkonto. 
- Beantwortung verschiedener Typen von benutzerdefinierten Fragen. 
- Abschließen des Double-Opt-In-Schritts.
- Auswählen einer Versandart.
- Auswählen einer Zahlungsmethode (Wir haben keine externen Komponenten von Zahlungsmethoden getestet).
- Anklicken von Einwilligungs-Checkboxen beim Prüfen der Bestellung.
- Abschließen der Bestellung.

#### Widget

- Entdecken und Navigieren der Produktliste.
- Navigation durch die Veranstaltungstermine einer Veranstaltungsreihe in einer Kalenderansicht.
- Mit dem pretix-Button direkt zur Kasse gehen.
