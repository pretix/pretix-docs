# Switzerland

{% include "warning-tax-law.md" %}

## Value Added Tax (VAT)

When selling goods and services in Switzerland, VAT ("Mehrwertsteuer") may apply.
All Swiss VAT rates can be configured in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. cross-border transactions).

## Invoicing

### Invoice information

Swiss requirements on information contained on invoices are defined in [Art. 26 MWSTG](https://www.fedlex.admin.ch/eli/cc/2009/615/de#art_26).

Invoices created by pretix, if properly configured, can include all necessary information.

### Invoice numbering

We are not aware of legal requirements on how to number invoices in Switzerland.

### E-invoicing

Switzerland currently does not require sending electronic invoices in a structured format.

## pretixPOS

We are not aware of specific requirements on cash registers in Switzerland.
Therefore, we believe pretixPOS can generally be used in Switzerland.

For receipts exceeding CHF 400, an invoice including the recipient address must be issued, which is currently not possible using pretixPOS ([Art. 26 (3) MWSTG](https://www.fedlex.admin.ch/eli/cc/2009/615/de#art_26)).

Generic requirements to create complete, correct and audit-proof data on all sales apply to cash registers as well (e.g. [Art 957a OR](https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de#part_4/tit_32/chap_1/lvl_A)).