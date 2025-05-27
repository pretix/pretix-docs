# Barrierefreiheit

Die Barrierefreiheit Ihres pretix-Ticketshops ist nicht nur aus ethisch und unternehmerisch von Bedeutung, sondern auch eine rechtliche Verpflichtung.
Der [European Accessibility Act] (https://en.wikipedia.org/wiki/European_Accessibility_Act) und seine nationalen Umsetzungsgesetze schreiben ab 2025 vor, dass alle Websites, über die Verträge mit Verbrauchern geschlossen werden, den Standards der Barrierefreiheit entsprechen müssen.
Wenn Sie einen Online-Shop betreiben, der Produkte oder Dienstleistungen an Verbraucher in der EU verkauft, dann gilt dies für Sie. 
Dazu gehören auch Ticketshops, die mit pretix erstellt wurden. 

Die entsprechende europäische Norm [EN 301 549](https://en.wikipedia.org/wiki/EN_301_549) verweist auf den Standard [WCAG 2.1 AA](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines).
Deshalb entwickeln wir pretix so, dass Sie die **WCAG 2.1/2.2 AA** Konformität für Ihren Ticketshop leicht erreichen können.

## Ihre Verantwortlichkeiten

pretix ist kein Ticketshop, sondern eine Software zur Erstellung von Ticketshops.
Die tatsächliche Barrierefreiheit des Shops hängt daher von einer Kombination aus unseren Bemühungen bei der Erstellung der Software und Ihren Bemühungen bei der Konfiguration für eine gute Barrierefreiheit ab.
Es liegt in Ihrer Verantwortung, die Konfigurationsparameter für pretix so zu wählen, dass sie den Anforderungen der Barrierefreiheit entsprechen.
Dies beinhaltet, ist aber nicht beschränkt auf:

- Verwenden Sie benutzerkonfigurierte Farben, die [gut unterscheidbar](https://www.w3.org/TR/WCAG22/#use-of-color) sind und [ausreichenden Kontrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) zu den umgebenden Farben bieten.

- Stellen Sie alle Informationen, die Sie [als Bilder](https://www.w3.org/TR/WCAG22/#images-of-text) präsentieren (z. B. das Kopfzeilenbild oder Produktbilder), auch als Text auf derselben Seite bereit. 

- Wenn Sie formatierten Text mit [Markdown](../guides/markdown.md) bereitstellen, achten Sie auf eine semantisch korrekte Verwendung des Markups. 
Wir empfehlen, keine Überschriften (``##``) oder HTML-Tags zu verwenden. 

- Wählen Sie Zahlungsanbieter, die gute Unterstützung für Barrierefreiheit bieten.

- Achten Sie beim Einbetten des [Widgets](../guides/widget.md) darauf, dass das CSS-Styling auf der einbettenden Website die Zugänglichkeit nicht beeinträchtigt, und stellen Sie sicher, dass der Pfad des Nutzers zum Widget ebenfalls zugänglich ist.

## Erklärung der Zugänglichkeit

Je nach Gerichtsbarkeit müssen Sie möglicherweise Informationen über die Zugänglichkeit Ihres Ticketshops veröffentlichen.
Sie können diese Informationen mit Hilfe der Konfigurationsoptionen unter :navpath:Ihr Veranstalter → :fa3-wrench einbetten: Einstellungen → Allgemein → Barrierefreiheit:. 

Hier ist ein Markdown-formatiertes Beispiel, das auf den Anforderungen des deutschen Rechts für eine nicht-staatliche Einrichtung basiert.
!!! Warnung 
    Die pretix-Dokumentation stellt keine Rechtsberatung dar. 
    Die nachfolgenden Informationen werden **ohne Gewähr** zur Verfügung gestellt. 
Die Verwendung erfolgt auf eigene Gefahr.

```
TODO
```

## Zugänglichkeitstests

Externe Experten haben die Erreichbarkeit mehrerer Beispielshops getestet. 
Die letzte Testrunde fand zwischen November 2024 und Mai 2025 statt.

!!! Hinweis

    Unser Engagement für Barrierefreiheit gilt derzeit nur für die mit pretix erstellten Ticketshops.
    Wir arbeiten an der Verbesserung der Barrierefreiheit des pretix-Backends, haben aber noch keine intensiven Barrierefreiheitstests durchgeführt oder das Backend entsprechend aktualisiert. 
    Unsere aktuelle Priorität sind die Ticketshops. 

### Umfang der Tests

Aufgrund der komplexen und hochgradig konfigurierbaren Natur von pretix ist es unmöglich, alle möglichen Konfigurationen zu testen.
Daher haben wir den Test an Beispiel-Ticketshops durchgeführt und versucht, möglichst viele pretix Features und Konfigurationen einzubeziehen.
Wenn eine Konfiguration, ein Plugin oder ein Prozess hier nicht aufgeführt ist, dann haben wir ihn nicht in unsere Zugänglichkeitstests einbezogen.
Wenn Sie den Nachweis der Barrierefreiheit für Ihren individuellen pretix-Ticketshop benötigen, müssen Sie Ihre eigenen Tests durchführen.

Die Zugänglichkeitstests umfassten **alle Kernfunktionen des Systems** sowie die folgenden Plugins:

- Banküberweisung
- Doppelter Opt-in-Schritt 
- Sparbuch-Tickets
- PDF-Ticket-Ausgabe
- Newsletter-Integration (am Beispiel von rapidmail)
- Seiten
- Sitzplätze
- Versand

Wir haben folgende Funktionen von pretix auf Barrierefreiheit getestet: 

#### Organizer-Seiten

- Umschalten der Seitensprache.
- Erkundung der Veranstaltungsliste durch Listen- und Kalenderansichten.
- Kontaktaufnahme mit dem Organisator.
- Anlegen eines Kundenkontos.
- Sich bei einem Kundenkonto anmelden.
- Zurücksetzen des Passworts für ein Kundenkonto.
- Aktualisieren von Kundenkontoinformationen.
- Anzeigen von Mitgliedschaften, letzten Bestellungen, gespeicherten Adressen und Profilen.

#### Veranstaltungsseiten

- Navigation durch die Termine einer Veranstaltungsreihe.
- Auffinden aller Veranstaltungsinformationen (Datum, Uhrzeit, Ort, Beschreibung).
- Entdecken und Navigieren in der Liste der Produkte, einschließlich ermäßigter Tickets, ausverkaufter Tickets, Tickets mit Variationen, Tickets mit Warteliste und Tickets, die einen Gutschein erfordern.
- Entdecken und Navigieren durch den Sitzplan.
- Eintragung in die Warteliste für ein ausverkauftes Ticket.
- Hinzufügen von Tickets zum Warenkorb. 
- Mit dem Warenkorb interagieren. 
- Auswählen von Zusatz- und Cross-Selling-Produkten.
- Zur Kasse gehen, ohne ein Kundenkonto zu erstellen, ein bestehendes Kundenkonto zu verwenden oder ein Kundenkonto zu erstellen.
- Beantwortung benutzerdefinierter Fragen verschiedener Art.
- Abschluss des Double-opt-in-Schritts.
- Auswählen einer Versandart.
- Auswahl einer Zahlungsmethode (Wir haben keine externen Komponenten von Zahlungsmethoden getestet).
- Anklicken von Zustimmungs-Checkboxen vor der Bestätigung der Bestellung.
- Abschließen der Bestellung.

#### Widget

- Entdecken und Navigieren in der Liste der Produkte.
- Navigation durch die Veranstaltungstermine einer Veranstaltungsreihe in einer Kalenderansicht.
- Mit der Schaltfläche pretix direkt zur Kasse gehen.
