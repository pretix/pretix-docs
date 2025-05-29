# Croatia

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Croatia, VAT ("Porez na dodanu vrijednost", "PDV") may apply.
You can configure all Croatian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Croatia currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).

Croatia only mandates e-invoices for transactions between businesses and the government (B2G) in a way compatible with the PEPPOL network.
pretix is planning to provide a PEPPOL integration.

More information is available on the website of the European Commission: [eInvoicing in Croatia](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Croatia).

## pretixPOS

When operating a cash register in Croatia, the cash register must [report all data](https://www.fina.hr/poslovni-digitalni-certifikati/poslovni-certifikati-za-fiskalizaciju#info) to the fiscal authority in real-time.
pretix does not support this.