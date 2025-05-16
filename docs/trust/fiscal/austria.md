# Austria

{% include "warning-tax-law.md" %}

## Value Added Tax (VAT)

When selling goods and services in Austria, VAT ("Umsatzsteuer") may apply.
All Austrian VAT rates can be configured in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### Invoice information

Austrian requirements on information contained on invoices are defined in [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=).
Some information can be omitted for invoices of less than €400.

Invoices created by pretix, if properly configured, can include all necessary information.

### Invoice numbering

pretix can create invoice numbers using a user-defined numbering scheme e.g. using a number range per organizer, event, or even order.
We recommend using consecutive invoice numbers in Austria.

### E-invoicing

Austria currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).
Austria only mandates e-invoices for transactions between businesses and the government (B2G).
This is currently not supported by pretix.

## pretixPOS

pretixPOS can be used in compliance with Austrian laws on cash registers ([§ 131b BAO](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&FassungVom=2025-01-27&Artikel=&Paragraf=131b&Anlage=&Uebergangsrecht=), [RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390)).

Use of a cash register is mandatory in Austria for every company with a total yearly turnover of at least € 15,000 and a yearly cash turnover of at least € 7,500.
The cash register must comply with the following requirements:

- Usage of a signature creation unit that ensures that no modification of recorded data can go unnoticed.
  pretixPOS is compatible with the online signature creation unit of A-Trust.

- Registration of the cash register with the tax authorities through FinanzOnline, as well as reporting of every failure of the cash register or signature creation unit.

- Creation of "initial receipts" after registration, "monthly receipts" at the end of every month, "yearly receipts" at the end of every year, and "final receipts" before deprovisioning of the cash register.
  pretixPOS supports creating these receipts. Note that initial receipts and yearly receipts *must* be scanned using the BMF's [Beleg Check app](https://play.google.com/store/apps/details?id=at.gv.bmf.belegcheck&hl=de).

- Issuing of receipts with all information required by [§ 11 RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390) and [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=).
  pretixPOS allows issuing compliant receipts using a receipt printer.
  Customers are required to take the receipt.

- Compatibility with a defined export format.
  pretixPOS is able to export data in the "Datenerfassungsprotokoll" (DEP) format.
  Note that you are required by law to make a backup of this file at least once every three months.