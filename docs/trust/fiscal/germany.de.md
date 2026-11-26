# Deutschland

{% include "warning-tax.de.md" %}

## Umsatzsteuer (USt)

Beim Verkauf von Waren und Dienstleistungen in Deutschland kann Umsatzsteuer (USt) anfallen.
Sie können in pretix alle deutschen USt-Sätze mittels [Steuer-Regeln](../../guides/taxes.md) konfigurieren, auch für komplexere Sachverhalte (z. B. Reverse Charge bei EU-Geschäften).

## Rechnungsstellung

### Rechnungsdaten

Die in Deutschland geltenden Anforderungen an Rechnungsangaben finden Sie in [§ 14 (4) UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html).
Bei Rechnungsbeträgen unter 250 € dürfen einige Angaben entfallen ([§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html)).
Andere Gesetze erfordern je nach Rechtsform des Unternehmens weitere Angaben, beispielsweise seine Nummer im Handelsregister ([§ 37a HGB](https://www.gesetze-im-internet.de/hgb/__37a.html), [§ 125 HGB](https://www.gesetze-im-internet.de/hgb/__125.html), [§ 177a HGB](https://www.gesetze-im-internet.de/hgb/__177a.html), [§ 35a GmbHG](https://www.gesetze-im-internet.de/gmbhg/__35a.html), [§ 80 AktG](https://www.gesetze-im-internet.de/aktg/__80.html)).

Sie können pretix so konfigurieren, dass die generierten Rechnungen alle notwendigen Angaben enthalten. 

### Rechnungsnummern

pretix kann Rechnungsnummern nach einem von den Benutzer\*innen definierten Schema generieren, beispielsweise mit einen Nummernbereich pro Veranstalter, Veranstaltung oder sogar Bestellung.
Alle diese Optionen sind in Deutschland möglich.
Es ist nicht erforderlich, fortlaufende Nummern zu generieren ([14.5 (10) UStAE](https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerarten/Umsatzsteuer/Umsatzsteuer_Anwendungserlass/umsatzsteuer_anwendungserlass.html)).

### E-Rechnungen

Deutschland implementiert derzeit die Pflicht zu E-Rechnungen.
Alle Rechnungen von Unternehmen an Unternehmen (B2B) müssen in einem strukturierten elektronischen Format ausgestellt werden.
Eine Ausnahme gilt für Rechnungsbeträge unter 250 € sowie für Kleinunternehmen (gemäß [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html)).

Bis Ende 2026 (2027 für Kleinunternehmen) ist der Versand von Rechnungen auf Papier oder im PDF-Format noch zulässig, wobei für PDF-Rechnungen unter Umständen die Zustimmung des\*der Rechnungsempfänger\*s\*in erforderlich ist.

Jede Form einer E-Rechnung ist erlaubt, sofern sie der europäischen Norm EN16931 entspricht und von dem\*der Empfänger\*in akzeptiert wird.
Die gängigsten Formate sind [ZUGFeRD](https://de.wikipedia.org/wiki/ZUGFeRD) und [XRechnung](https://de.wikipedia.org/wiki/XRechnung).

pretix unterstützt mit der [ZUGFeRD-Erweiterung](https://marketplace.pretix.eu/products/zugferd/) die Erstellung von ZUGFeRD-Rechnungen gemäß EN16931.
ZUGFeRD-Rechnungen sind hybride Dokumente mit einem PDF- und einem XML-Teil.
Dadurch können sie von deutschen B2B-Kund\*innen elektronisch verarbeitet und von allen anderen als klassische PDF-Rechnungen genutzt werden.

Weitere Informationen finden Sie in unserem Blog-Artikel [Durchstarten mit der E-Rechnung](https://pretix.eu/about/de/blog/20241218-e-rechnung-starten/).

## Nachprüfbarkeit

### Verfahrensdokumentation

Alle deutschen Unternehmen, die für ihre Buchhaltung elektronische Systeme nutzen, müssen ihre Verfahren intern dokumentieren ([10.1 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).

Diese Dokumentation sollte beispielsweise darlegen, wie Sie pretix nutzen, wer Zugriff auf Ihr pretix-Konto bzw. den pretix-Server hat und wie Sie Daten von pretix an Ihre Buchhaltungssysteme übertragen.

Wenn Sie technische Angaben über pretix in Ihre Verfahrensdokumentation aufnehmen möchten, können Sie unsere [Anlage zur Verfahrensdokumentation](https://download.pretix.eu/vd.pdf) nutzen.

### Protokollierung von Änderungen

pretix protokolliert alle Änderungen an Konfigurations- oder Transaktionsdaten. 
Dabei werden der\*die Benutzer\*in, der Zeitpunkt und die Art der Änderung am System protokolliert.
pretix enthält keine Funktion, mit der sich diese Protokolle ändern oder löschen lassen (ausgenommen bei der Pseudonymisierung personenbezogener Daten durch unsere Datenschutz-Funktionen).
Bestellungen können Sie niemals aus dem System löschen (außer sie wurden im Testmodus getätigt).
Wir sind daher überzeugt, dass pretix die gesetzlichen Anforderungen an die Nachprüfbarkeit erfüllt (z. B. [§ 146 (4) AO](https://www.gesetze-im-internet.de/ao_1977/__146.html), [§ 293 (3) HGB](https://www.gesetze-im-internet.de/hgb/__239.html)).

### Archivierung

Sie müssen alle Rechnungen und Belege mindestens 8 Jahre lang digital aufbewahren ([§ 257 HGB](https://www.gesetze-im-internet.de/hgb/__257.html), [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html)).
pretix löscht zwar keine alten Rechnungen, garantiert aber nicht die erforderliche Sicherheit für die langfristige Archivierung.
Wir empfehlen daher nachdrücklich, alle erstellten Rechnungen regelmäßig zu exportieren und in einem Archivierungssystem aufzubewahren.

Sie müssen auch weitere Unterlagen, die für die Nachvollziehbarkeit Ihrer Buchhaltung erforderlich sind, archivieren (siehe z. B. [1.3, 5.2 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).
Dazu gehören mindestens Bestellungsdaten, Zahlungsdaten und Ihre Verfahrensdokumentation.
Wir empfehlen, diese Daten zum bequemen Exportieren und Verarbeiten in pretix zu belassen, aber auch regelmäßig eine Offline-Kopie zu exportieren (siehe auch [9.4 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).

## pretixPOS

Sie können pretixPOS im Einklang mit den deutschen Gesetzen zu elektronischen Aufzeichnungssystemen nutzen ([§ 146a AO](https://www.gesetze-im-internet.de/ao_1977/__146a.html), [KassenSichV](https://www.gesetze-im-internet.de/kassensichv/BJNR351500017.html)).

Die Nutzung eines solchen Kassensystems ist in Deutschland nicht verpflichtend.
Wenn Sie ein Kassensystem nutzen, stellen Sie durch folgende Maßnahmen sicher, dass Sie die rechtlichen Anforderungen einhalten:

- Verwenden Sie eine [technische Sicherheitseinrichtung](../../guides/pretixpos/tse.md) (TSE), die sicherstellt, dass jede Veränderung der erfassten Daten bemerkt wird.
  pretixPOS ist mit den TSE der meisten Hersteller kompatibel.

- Registrieren Sie alle Kassensysteme bei den Steuerbehörden.
  pretix enthält [Funktionen zur Vereinfachung der Registrierung](../../guides/pretixpos/register.md).

- Stellen Sie Belege aus, die alle laut [§ 6 KassenSichV](https://www.gesetze-im-internet.de/kassensichv/BJNR351500017.html) und [§ 14 (4) UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) erforderlichen Angaben enthalten.
  pretixPOS ermöglicht die Ausgabe entsprechender Belege über einen Bondrucker oder in digitaler Form.

- Exportieren Sie Ihre Daten in ein offiziell definiertes Format. 
  pretixPOS kann Daten im Format [DSFinV-K](https://www.bzst.de/DE/Unternehmen/Aussenpruefungen/DigitaleSchnittstelleFinV/digitaleschnittstellefinv_node.html) exportieren.

Die pretix GmbH (zuvor rami.io GmbH) ist Mitglied im [Deutschen Fachverband für Kassen- und Abrechnungssystemtechnik](https://dfka.net/). 
Dadurch sind wir immer auf dem aktuellen Stand hinsichtlich Änderungen in der Gesetzgebung zu Kassensystemen.