# Slovakia

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Slovakia, VAT ("Daň z pridanej hodnoty", "DPH") may apply.
You can configure all Slovakian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Slovakia is planning to introduce mandatory e-invoicing for transactions between businesses (B2B) in 2027.
The [proposed law](https://www.slov-lex.sk/elegislativa/legislativne-procesy/SK/PI/2024/334) is not yet passed and therefore the exact technical details and timelines are not clear.
Most likely, the system will be based on Peppol.
A native integration of pretix with Peppol is available as a plugin as part of our pretix Hosted product.
But the system will probably also require real-time reporting to the fiscal authority, which pretix does not support.

More information is available on the website of the European Commission: [eInvoicing in Slovakia](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Slovakia).

## pretixPOS

When operating a cash register in Slovakia, the cash register must be compliant with [local regulations](https://www.financnasprava.sk/sk/podnikatelia/dane/ekasa) and interface with the fiscal authority.
pretixPOS does **not** support this and can therefore **not** be used as cash register software in Slovakia.
