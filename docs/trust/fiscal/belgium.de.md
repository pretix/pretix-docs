# Belgien

{% include "warning-tax.de.md" %}

## Umsatzsteuer (USt)

Beim Verkauf von Waren und Dienstleistungen in Belgien kann Umsatzsteuer ("taxe sur la valeur ajoutée", "TVA") anfallen.
Sie können in pretix alle belgischen USt-Sätze mittels [Steuer-Regeln](../../guides/taxes.de.md) konfigurieren, auch für komplexere Sachverhalte (z. B. Reverse Charge bei EU-Geschäften).

## Rechnungsstellung

### E-Rechnungen

Belgien hat 2026 die Pflicht zu elektronischen Rechnungen für B2B-Geschäfte eingeführt.
Alle Rechnungen müssen über das Netzwerk [Peppol](https://de.wikipedia.org/wiki/PEPPOL) übertragen werden.

Für unser Produkt pretix Hosted ist eine native Integration von pretix mit Peppol als Erweiterung erhältlich.

Weitere Informationen finden Sie (in englischer Sprache) auf der Website der Europäischen Kommission: [eInvoicing in Belgium](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Belgium).

## pretixPOS

Kassensystem in Belgien müssen ein zertifiziertes Kassensystem verwenden, das die Daten automatisch an die Steuerbehörde meldet.
pretixPOS ist **nicht** zertifiziert und unterstützt dies **nicht**.
Weitere Informationen finden Sie (in französischer Sprache) auf der Website der belgischen Regierung: [Le système de caisse enregistreuse](https://www.systemedecaisseenregistreuse.be/).

Aber: Diese Anforderung [gilt nur](https://www.systemedecaisseenregistreuse.be/fr/klant/algemeen/qui-doit-utiliser-le-sce) für Unternehmen, die ein Restaurant oder einen Catering-Service mit einem Umsatz ab 25.000 € betreiben.
Wenn Sie also kein Restaurant und keinen Catering-Service betreiben, können Sie pretixPOS eventuell doch einsetzen.
Holen Sie eine individuelle anwaltliche oder buchhalterische Rat ein, ob Sie zur Verwendung eines zertifizierten Kassensystems verpflichtet sind.
