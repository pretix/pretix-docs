# Österreich

{% include "warning-tax.de.md" %}

## Umsatzsteuer (USt)

Beim Verkauf von Waren und Dienstleistungen in Österreich kann Umsatzsteuer (USt) anfallen.
Sie können in pretix alle österreichischen USt-Sätze mittels [Steuer-Regeln](../../guides/taxes.de.md) konfigurieren, auch für komplexere Sachverhalte (z. B. Reverse Charge bei EU-Geschäften).

## Rechnungsstellung

### Rechnungsdaten

Die österreichischen Anforderungen, welche Daten in Rechnungen enthalten sein müssen, finden sich in [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=).
Bei Rechnungsbeträgen unter 400 € dürfen einige Angaben entfallen.

Sie können pretix so konfigurieren, dass die generierten Rechnungen alle notwendigen Angaben enthalten. 

### Rechnungsnummern

pretix kann Rechnungsnummern nach einem von den Benutzer\*innen definierten Schema generieren, beispielsweise mit einen Nummernbereich pro Veranstalter, Veranstaltung oder sogar Bestellung.
Wir empfehlen, in Österreich mit fortlaufenden Rechnungsnummern zu arbeiten.

### E-Rechnungen

In Österreich gibt es für Geschäfte zwischen Unternehmen (B2B) oder zwischen Unternehmen und Verbraucher\*innen (B2C) derzeit keine Pflicht, elektronische Rechnungen in einem strukturierten Format auszustellen.
Nur für Geschäfte zwischen Unternehmen und Bundesbehörden (B2G) sind E-Rechnungen in Österreich Pflicht.
pretix unterstützt dies derzeit nicht. 

Weitere Informationen finden Sie (in englischer Sprache) auf der Website der Europäischen Kommission: [eInvoicing in Austria](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Austria).

## pretixPOS

Sie können pretixPOS im Einklang mit österreichischen Gesetzen zu Kassensystemen ([§ 131b BAO](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&FassungVom=2025-01-27&Artikel=&Paragraf=131b&Anlage=&Uebergangsrecht=), [RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390)) nutzen.

In Österreich sind alle Unternehmen mit einem jährlichen Gesamtumsatz ab 15 000 € und einem Barumsatz ab 7 500 € zur Verwendung eines Kassensystems verpflichtet.
Mit den folgenden Maßnahmen stellen Sie sicher, dass Ihr Kassensystem den Regeln entspricht: 

- Verwenden Sie eine Signaturerstellungseinheit, die sicherstellt, dass jede Veränderung der erfassten Daten bemerkt wird.
  pretixPOS ist kompatibel mit der Signaturerstellungseinheit A-Trust.

- Registrieren Sie das Kassensystem über FinanzOnline bei den Steuerbehörden. 
Melden Sie jeden Ausfall des Kassensystems oder der Signaturerstellungseinheit.

- Erstellen Sie nach der Registrierung einen sogenannten "Startbeleg", am Monatsende "Monatsbelege", am Jahresende "Jahresbelege" und vor der Außerbetriebnahme des Kassensystems einen "Schlussbeleg". 
  pretixPOS unterstützt die Erstellung dieser Belege. 
  
- Scannen Sie diese Belege mit der App [BMF Belegcheck](https://www.bmf.gv.at/services/apps.html#belegcheck) des Bundesministeriums für Finanzen (BMF). 

- Stellen Sie Belege aus, die alle laut [§ 11 RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390) und [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=) erforderlichen Angaben enthalten.
  pretixPOS ermöglicht die Ausgabe entsprechender Belege über einen Bondrucker.
  Ihre Kund\*innen sind verpflichtet, den Beleg in Empfang zu nehmen.

- Exportieren Sie Daten in ein definiertes Exportformat.
  pretixPOS kann Daten im Format "Datenerfassungsprotokoll" (DEP) exportieren.
  Erstellen Sie mindestens alle drei Monate ein Backup dieser Datei. 
  Dies ist eine gesetzliche Pflicht. 