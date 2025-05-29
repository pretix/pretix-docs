# Slovenia

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Slovenia, VAT ("Davek na dodano vrednost", "DDV") may apply.
You can configure all Slovenian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Slovenia is planning to introduce requirements on electronic invoicing for transactions between businesses (B2B), likely starting in 2027.
The exact timeline and technical details are not yet finalized and we do not know if pretix will support this.

More information is available on the website of the European Commission: [eInvoicing in Slovenia](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Slovenia).

## pretixPOS

When operating a cash register in Slovenia, the cash register needs to comply with the [Act on fiscal verification of invoices (ZDavPR)](https://www.fu.gov.si/en/supervision/areas_of_work/fiscal_verification_of_invoices_and_pre_numbered_receipt_book#c3177) and report transactions to the fiscal authority in real-time.
pretixPOS currently does not support this, but implementation appears to be feasible given sufficient demand.
Please let us know if you are interested in using pretixPOS in Slovenia.