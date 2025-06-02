# Italy

{% include "warning-tax-law.md" %}

## Value-added Tax (VAT)

When selling goods and services in Italy, VAT ("imposta sul valore aggiunto", "IVA") may apply.
You can configure all Italian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Italy requires all domestic invoices to be issued using an [electronic standard](https://www.agenziaentrate.gov.it/portale/aree-tematiche/fatturazione-elettronica) and sent through the national invoicing system.

pretix currently does **not** support this process, but we are working on a solution to this.
In the meantime, it is possible to sell tickets through pretix and send invoices outside of pretix.

More information is available on the website of the European Commission: [eInvoicing in Italy](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Italy).

## pretixPOS

Using a cash register in Italy requires the use of a "Registratore Telematico" (RT).
pretixPOS currently does **not** support RT and can therefore **not** be used as a cash register in Italy.

## SIAE

[SIAE](https://www.siae.it/en/) is Italy's association of authors and publishers.
If you sell tickets for events involving works protected by SIAE, you must report ticket sales to SIAE using a specialized system.
pretix does **not** support this.