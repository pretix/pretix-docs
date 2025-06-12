# France

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in France, VAT ("taxe sur la valeur ajoutée", "TVA") may apply.
You can configure all French VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

France is introducing mandatory electronic invoicing for B2B transactions in 2026/2027.
All invoices must be transmitted through certified service providers ("PDPs") and reported to the government through [Chorus Pro](https://portail.chorus-pro.gouv.fr).

pretix will be able to generate invoice files in one of the supported formats, but will not become a certified service provider.
If you are interested in an integration with a certified third-party service provider, reach out to us at [support@pretix.eu](mailto:support@pretix.eu]. 

More information is available on the website of the European Commission: [eInvoicing in France](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+France).

## pretixPOS

Using a cash register in France requires the software to be certified under the [NF525](https://infocert.org/en/nf525/) standard.
pretixPOS is currently **not** certified under this standard and can therefore **not** be used as cash register software in France.