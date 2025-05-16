# Italy

{% include "warning-tax-law.md" %}

## Value Added Tax (VAT)

When selling goods and services in Italy, VAT ("IVA") may apply.
All Italian VAT rates can be configured in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

Italy requires all domestic invoices to be issued using an [electronic standard](https://www.agenziaentrate.gov.it/portale/aree-tematiche/fatturazione-elettronica) and sent through the national invoicing system.

pretix currently does not support this process, but we are working to resolve this.

## pretixPOS

Using a cash register in Italy requires the use of a "Registratore Telematico" (RT).
pretixPOS is currently does not support RT and can therefore not be used as a cash register in Italy.

## SIAE

[SIAE](https://www.siae.it/en/) is Italy's association of authors and publishers.
When selling tickets for events involving works protected by SIAE, it is required to report ticket sales to SIAE using a specialized system.
pretix currently does not support this.