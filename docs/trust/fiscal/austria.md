# Austria

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Austria, VAT ("Umsatzsteuer") may apply.
You can configure all Austrian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### Invoice information

Austrian requirements on information included in invoices are defined in [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=).
Some information can be omitted for invoices of less than €400.

You can configure pretix to include all necessary information in the invoices it generates. 

### Invoice numbering

pretix can generate invoice numbers with a user-defined numbering scheme, for example using a number range per organizer, event, or even order.
We recommend using consecutive invoice numbers in Austria.

### E-invoicing

Austria currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).
Austria only mandates e-invoices for transactions between businesses and the government (B2G).
pretix currently does not support this. 

More information is available on the website of the European Commission: [eInvoicing in Austria](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Austria).

## pretixPOS

You can use pretixPOS in compliance with Austrian laws on cash registers ([§ 131b BAO](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&FassungVom=2025-01-27&Artikel=&Paragraf=131b&Anlage=&Uebergangsrecht=), [RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390)).

Use of a cash register is mandatory in Austria for every company with a total yearly turnover of at least €15,000 and a yearly cash turnover of at least €7,500.
To ensure that your cash register complies with regulations, take the following steps: 

- Use a signature creation unit that ensures that no modification of recorded data can go unnoticed.
  pretixPOS is compatible with the  A-Trust online signature creation unit.

- Register the cash register with the tax authorities through FinanzOnline. 
Report every failure of the cash register or signature creation unit.

- Create so-called "initial receipts" after registration, "monthly receipts" at the end of every month, "yearly receipts" at the end of every year, and "final receipts" before you decommission the cash register. 
  pretixPOS supports creating these receipts. 
  
- Use the app [BMF Belegcheck](https://www.bmf.gv.at/services/apps.html#belegcheck) by Bundesministerium für Finanzen (BMF) to scan these receipts. 

- Issue receipts with all information required by [§ 11 RKSV](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009390) and [§ 11 UStG 1994](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004873&FassungVom=2024-08-29&Artikel=&Paragraf=11&Anlage=&Uebergangsrecht=).
  pretixPOS allows issuing compliant receipts using a receipt printer.
  Your customers are required to take the receipt.

- Export data in a defined export format.
  pretixPOS is able to export data in the "Datenerfassungsprotokoll" (DEP) format.
  Create a backup of this file at least once every three months. 
  This is required by law. 