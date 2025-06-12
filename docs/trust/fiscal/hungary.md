# Hungary

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Hungary, VAT ("Általános forgalmi adó", "ÁFA") may apply.
You can configure all Estonian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Hungary has complex legal requirements around sending invoices, including an obligation for real-time invoice reporting.
pretix does **not** support this, but it is possible to sell tickets through pretix and send and report invoices outside of pretix.

More information is available on the website of the European Commission: [eInvoicing in Hungary](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Hungary).

## pretixPOS

Cash registers operated in Hungary must be certified to comply with [local regulations](https://njt.hu/jogszabaly/2025-8-20-2X).
Cash registers also have to interface with a fiscal device. 
pretixPOS does **not** support this and can therefore **not** be used as cash register software in Hungary if the law applies.
To our understanding, the law applies only to specific industry sectors.
Please check with your attorney or accountant if it applies to you.
