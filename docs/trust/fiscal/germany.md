# Germany

{% include "warning-tax-law.md" %}

## Value-added Tax (VAT)

When selling goods and services in Germany, VAT ("Umsatzsteuer") may apply.
You can configure all German VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### Invoice information

German requirements on information included in invoices are defined in [§ 14 (4) UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html).
Some information can be omitted for invoices of less than €250 ([§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html)).
Additional information like company registration information is required by other laws, depending on the legal form of the company ([§ 37a HGB](https://www.gesetze-im-internet.de/hgb/__37a.html), [§ 125 HGB](https://www.gesetze-im-internet.de/hgb/__125.html), [§ 177a HGB](https://www.gesetze-im-internet.de/hgb/__177a.html), [§ 35a GmbHG](https://www.gesetze-im-internet.de/gmbhg/__35a.html), [§ 80 AktG](https://www.gesetze-im-internet.de/aktg/__80.html)).

You can configure pretix to include all necessary information in the invoices it generates. 

### Invoice numbering

pretix can create invoice numbers using a user-defined numbering scheme e.g. using a number range per organizer, event, or even order.
All of these options are possible in Germany.
It is not necessary to generate consecutive numbers ([14.5 (10) UStAE](https://www.bundesfinanzministerium.de/Web/DE/Themen/Steuern/Steuerarten/Umsatzsteuer/Umsatzsteuer_Anwendungserlass/umsatzsteuer_anwendungserlass.html)).

### E-invoicing

Germany is currently implementing an electronic invoicing mandate.
All invoices sent in a business-to-business (B2B) relationship must be issued in a structured electronic format.
An exception is made for invoices below €250 and for small businesses (those that fall under [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html)).

Up to the end of 2026 (2027 for smaller businesses), sending paper or PDF invoices is still allowed, although PDF invoices may require the consent of the receiver.

Any type of electronic invoice is allowed as long as it is compliant with European norm EN16931 and accepted by the receiver.
The most common formats are [ZUGFeRD](https://de.wikipedia.org/wiki/ZUGFeRD) and [XRechnung](https://de.wikipedia.org/wiki/XRechnung).

pretix supports generating ZUGFeRD invoices compliant with EN16931 using the [ZUGFeRD plugin](https://marketplace.pretix.eu/products/zugferd/).
ZUGFeRD invoices are hybrid documents with a PDF part and an XML part.
This way, they can be processed as electronic invoices by German B2B customers, and as regular PDF invoices by everyone else.

Additional guidance is available in our German blog article [Durchstarten mit der E-Rechnung](https://pretix.eu/about/de/blog/20241218-e-rechnung-starten/).

## Audit readiness

### Procedure documentation

All German companies using electronic systems in their financial processes are required to have internal documentation of their processes ([10.1 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).

This documentation should include, for example, how you use pretix, who has access to your pretix account or pretix server, and how you transfer data from pretix to your accounting systems.

To include technical details about pretix in your procedure documentation, you can use our [Annex for the Procedure Documentation](https://download.pretix.eu/vd.pdf).

### Logging of changes

pretix logs all changes to configurations or transaction data. 
This logging includes the user, time, and type of change made in the system.
pretix does not include functionality to modify or delete these logs (other than by applying pseudonymization of personal information through our privacy tools).
You can never delete orders deleted from the system (unless they were made during test mode).
We therefore consider pretix to be audit-proof as required by law (e.g. [§ 146 (4) AO](https://www.gesetze-im-internet.de/ao_1977/__146.html), [§ 293 (3) HGB](https://www.gesetze-im-internet.de/hgb/__239.html)).

### Archiving

You have to archive all invoices and receipts digitally for at least 8 years ([§ 257 HGB](https://www.gesetze-im-internet.de/hgb/__257.html), [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html)).
While pretix does not delete old invoices, it is not a suitable system to provide sufficient guarantees about long-term archival.
We strongly recommend regularly exporting all created invoices and storing them in an archival system.

You also have to archive additional material that is required for understanding your accounting (see e.g. [1.3, 5.2 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).
This includes at least order data, payment data, and your procedure documentation.
We recommend keeping this data in pretix for easy exporting and processing, but also exporting an offline copy regularly (see also [9.4 GoBD](https://ao.bundesfinanzministerium.de/ao/2023/Anhaenge/BMF-Schreiben-und-gleichlautende-Laendererlasse/Anhang-64/inhalt.html)).

## pretixPOS

pretixPOS can be used in compliance with German laws on cash registers ([§ 146a AO](https://www.gesetze-im-internet.de/ao_1977/__146a.html), [KassenSichV](https://www.gesetze-im-internet.de/kassensichv/BJNR351500017.html)).

Use of a cash register is not mandatory in Germany.
If you use a cash register, take the following steps to ensure that you are complying with legal requirements:

- Use a so-called [technische Sicherheitseinrichtung](../../guides/pretixpos/tse.md) (TSE), a specialized device that ensures that no modification of recorded data can go unnoticed.
  pretixPOS is compatible with TSEs from multiple vendors.

- Register all cash registers with the tax authorities.
  pretix includes [utilities to simplify registration](../../guides/pretixpos/register.md).

- Issue receipts with all information required by [§ 6 KassenSichV](https://www.gesetze-im-internet.de/kassensichv/BJNR351500017.html) and [§ 14 (4) UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html).
  pretixPOS allows issuing compliant receipts using a receipt printer or in digital form.

- Export data in an officially defined format. 
  pretixPOS can export data in the [DSFinV-K](https://www.bzst.de/DE/Unternehmen/Aussenpruefungen/DigitaleSchnittstelleFinV/digitaleschnittstellefinv_node.html) format.

pretix GmbH (previously rami.io GmbH) is a member of the [German association of cash register manufacturers](https://dfka.net/). 
This means that we always stay up-to-date with changes in cash register regulation.