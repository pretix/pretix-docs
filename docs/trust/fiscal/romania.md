# Romania

{% include "warning-tax-law.md" %}

## Value-added Tax (VAT)

When selling goods and services in Romania, VAT ("Taxa pe valoarea adăugată", "TVA") may apply.
You can configure all Romanian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Romania's [tax regulations](https://legislatie.just.ro/Public/DetaliiDocumentAfis/275745) require all domestic invoices to be issued using an [electronic system](https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/strategii_anaf/proiecte_digitalizare/e.factura).
pretix does **not** support this process.
It is possible to sell tickets through pretix and issue invoices outside of pretix.

More information is available on the website of the European Commission: [eInvoicing in Romania](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Romania).

## pretixPOS

Using a cash register in Romania requires the use of a fiscal printer that exchanges data with the financial authority (ANAF).
pretixPOS currently does **not** support Romanian fiscal printers and can therefore **not** be used as a cash register in Romania.