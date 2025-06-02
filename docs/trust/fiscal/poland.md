# Poland

{% include "warning-tax-law.md" %}

## Value-added Tax (VAT)

When selling goods and services in Poland, VAT ("Podatek od towarow i uslug", "PTU") may apply.
You can configure all Polish VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Poland will introduce a required centralized system ([KSeF](https://www.gov.pl/web/finanse/krajowy-system-e-faktur--plan-wdrozenia)) for all B2B invoicing in 2026.
pretix does **not** support this, but it is possible to sell tickets through pretix and send invoices outside of pretix.

More information is available on the website of the European Commission: [eInvoicing in Poland](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Poland).

## pretixPOS

Using a cash register in Poland requires the use of a [certified system](https://www.gov.pl/web/finance/fiscal-cash-registers) that integrates with a fiscal device and communicates with the fiscal authority.
pretixPOS currently does **not** support this and can therefore **not** be used as a cash register in Poland.