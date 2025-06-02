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

- Verwenden Sie einfache Sprache für Ihre Veranstaltungsbeschreibung, Produktbezeichnungen, etc.

Durch die Vielfältigkeit der von pretix angebotenen Konfigurationsoptionen können wir keine abschließende Liste von Schritten angeben, die eine Barrierefreiheit des Shops unter allen Umständen garantieren.

## Information zur Barrierefreiheit

Abhängig von den für Sie geltenden Gesetzen müssen Sie möglicherweise Informationen über die Barrierefreiheit Ihres Ticketshops veröffentlichen.
Sie können diese Informationen einbetten, indem Sie die Konfigurationsoptionen unter :navpath:Ihr Veranstalter → :fa3-wrench: Einstellungen → Allgemein → Barrierefreiheit: nutzen.

Hier ist ein Markdown-formatiertes Beispiel, das auf den Anforderungen des deutschen Rechts für eine nicht-staatliche Einrichtung basiert.

!!! Warning 
    Die pretix-Dokumentation stellt keine Rechtsberatung dar. 
    Die nachfolgenden Informationen werden **ohne Gewähr** zur Verfügung gestellt. 
    Die Verwendung erfolgt auf eigene Gefahr.

```
# Musterinformation zur Barrierefreiheit 

## Allgemeine Beschreibung

Auf dieser Website können Sie Tickets für unsere Veranstaltungen erwerben. Weitere Informationen zu den jeweiligen Veranstaltungen finden Sie in der jeweiligen Beschreibung.

Für die Bezahlung der Ticket stehen Ihnen folgende Zahlungsmöglichkeiten zur Verfügung:

 - zu ergänzen

## Information zum Anbieter

_Max Mustermann, Sesamstraße 1, 12345 Berlin, Telefon: 0815 12345678, E-Mail: mustermann@example.org._

## Gesetzliche Anforderungen

Die gesetzlichen Anforderungen ergeben sich aus dem Barrierefreiheitsstärkungsgesetz (BFSG), insbesondere § 14 im Verbindung mit § 3 Abs. 1 BFSG unter Verweis auf die Verordnung zum Barrierefreiheitsstärkungsgesetz (BFSGV).

## Erfüllung der Barrierefreiheitsanforderungen:

Bei der Erfüllung der Barrierefreiheitsanforderungen dieses Ticketshops wurden folgende Normen und Richtlinien angewandt:

 - Harmonisierte Europäische Norm (EN) 301 549, Version 3.2.1
 - Web Content Accessibility Guidelines (WCAG), Version 2.2, Stufen A und AA

Unser Angebot basiert auf einer standardisierten Software für Ticketshops. Der Hersteller dieser Software hat diese Software mit der Unterstützung von Fachleuten für digitale Barrierefreiheit optimiert und anhand von Beispielen einem unabhängigen externen Barrierefreiheitstest unterzogen. Der Hersteller führt intern regelmäßig weitere automatisierte oder manuelle Tests durch.

Bei der Konfiguration der Software zur Umsetzung unseres Ticketshops haben wir die Hinweise des Herstellers berücksichtigt, um ein barrierefreies Ergebnis zu erzielen.

Konkret erfüllt der Ticketshop die Anforderungen unter anderem durch folgende Maßnahmen:

 - Der Ticketshop ist klar strukturiert, enthält aussagekräftige und sinnvoll strukturierte Überschriften und Beschriftungen. Links sind gut erkennbar und aussagekräftig beschriftet.
 - Sie können diesen Ticketshop ohne Verlust von Informationen mit assistiven Technologien, wie z.B. Screenreadern, nutzen.
 - Sie können den Ticketshop mit einer externen Tastatur nutzen und steuern. Das funktioniert für alle Bereiche und Funktionen. Die Navigation erfolgt in einer sinnvollen Reihenfolge. 
Wenn Sie interaktive Elemente, wie beispielsweise Links oder Schaltflächen, mit der Tastatur auswählen, heben sich diese visuell deutlich hervor (Fokusmarkierung).
 - Texte und visuelle Inhalte haben gut erkennbare Kontraste. Die Darstellung (z.B. Schriftgrößen) ist über die Einstellungen im Browser und/oder in Ihrem Betriebssystem anpassbar. Alle Inhalte sind ohne Farbunterscheidung zugänglich und es gibt Textalternativen für Nutzer mit eingeschränktem Sehvermögen.
 - Unser Ticketshop funktioniert mit unterschiedlichen Ausrichtungen. Sie können Ihren Bildschirm sowohl quer, als auch hochkant ausrichten. Die Darstellung der Bereiche, Inhalte und Funktionen passt sich automatisch an.
 - Die Benutzung unseres Ticketshops setzt kein Hör- oder Sprechvermögen voraus.
 - Wenn der Abschluss einer Buchung eine Zeitbegrenzung hat, wird das rechtzeitig angekündigt. Sie können die Begrenzung dann verlängern.
 - Der Ticketshop wurde so gestaltet, dass er Sie beim Vermeiden von Fehlern und bei der Korrektur von Fehlern unterstützt.
 - Die Benutzung des Ticketshops funktioniert ohne komplexe, pfadbasierte oder gleichzeitige Bewegungen.
 - Der Ticketshop enthält keine Licht- oder Blitz-Effekte, die fotosensitive Anfälle auslösen.

Wenn Sie uns Feedback zur Barrierefreiheit unseres Ticketshops geben möchten, kontaktieren Sie uns bitte unter den oben unter "Informationen zum Anbieter" angegebenen Kontaktdaten.

## Zuständige Marktüberwachungsbehörde:

Marktüberwachungsstelle der Länder für die Barrierefreiheit von Produkten und Dienstleistungen (MLBF) in Magdeburg (Sachsen-Anhalt).
```

**Achtung für öffentliche Stellen:** Das BFSG gilt zusätzlich zur bereits länger gültigen [BITV](https://de.wikipedia.org/wiki/Barrierefreie-Informationstechnik-Verordnung). Die BITV erfordert eine *Erklärung der Barrierefreiheit*, deren Umfang über die von BFSG geforderten Informationen hinausgeht. Die EU-Kommission hat eine [offizielle Vorlage](https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32018D1523) zum Aufbau einer solchen Erklärung herausgegeben.

## Barrierefreiheits-Tests

Externe Expert\*innen haben die Barrierefreiheit mehrerer Beispielshops getestet. 
Die letzte Testrunde fand zwischen November 2024 und Mai 2025 statt.

!!! Note

    Unsere Zusicherung der Barrierefreiheit gilt momentan nur für die mit pretix erstellten Ticketshops.
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

Wir haben folgende Bestandteile von pretix auf Barrierefreiheit getestet: 

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
 - Im Bestellprozess in ein bestehendes Kundenkonto einloggen, ein neues Kundenkonto erstellen, oder ohne Kundenkonto fortfahren. 
 - Beantwortung verschiedener Typen von benutzerdefinierten Fragen. 
 - Abschließen des Double-Opt-In-Schritts.
 - Auswählen einer Versandart.
 - Auswählen einer Zahlungsmethode (Wir haben keine externen Komponenten von Zahlungsmethoden getestet).
 - Anklicken von Einwilligungs-Checkboxen beim Prüfen der Bestellung.
 - Abschließen der Bestellung.

#### Widget

 - Auffinden und Navigieren der Produktliste.
 - Navigation durch die Veranstaltungstermine einer Veranstaltungsreihe in einer Kalenderansicht.
 - Mit dem pretix-Button direkt zur Kasse gehen.
