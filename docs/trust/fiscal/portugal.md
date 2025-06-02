# Portugal

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Portugal, VAT ("Imposto sobre o valor acrescentado", "IVA") may apply.
You can configure all Portuguese VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

All invoices in Portugal must be created by [certified invoicing software](https://vat-one-stop-shop.ec.europa.eu/national-vat-rules/portugal-vat-rules_en).
Starting in 2026, they must also be [signed](https://diariodarepublica.pt/dr/en/detail/decree-law/28-2019-119622094) using a [qualified electronic signature](https://en.wikipedia.org/wiki/Qualified_electronic_signature).
pretix does **not** support this, but it is possible to sell tickets through pretix and send invoices outside of pretix.

More information is available on the website of the European Commission: [eInvoicing in Portugal](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Portugal).

## pretixPOS

When operating a cash register in Portugal, the cash register software must be certified by the fiscal authority.
pretixPOS is currently **not** certified and can therefore **not** be used as cash register software in Portugal.
