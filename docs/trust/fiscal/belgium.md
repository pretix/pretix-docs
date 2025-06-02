# Belgium

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Belgium, VAT ("taxe sur la valeur ajoutée", "TVA") may apply.
You can configure all Belgian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Belgium is introducing mandatory electronic invoicing for B2B transaction in 2026.
All invoices must be transmitted through the [PEPPOL](https://en.wikipedia.org/wiki/PEPPOL) network.

pretix is planning to provide a PEPPOL integration by the end of 2025.

More information is available on the website of the European Commission: [eInvoicing in Belgium](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Belgium).

## pretixPOS

Cash registers in Belgium are required to use a certified cash register that automatically reports data to the fiscal authority.
pretixPOS is **not** certified and does **not** support this.
More information is available on the website of the Belgian government: [Le système de caisse enregistreuse](https://www.systemedecaisseenregistreuse.be/).

However, this requirement [only applies to](https://www.systemedecaisseenregistreuse.be/fr/klant/algemeen/qui-doit-utiliser-le-sce) businesses who operate restaurant or catering services with a turnover of €25,000 or more.
Therefore, if you do not offer restaurant or catering services, you might be able to use pretixPOS.
Please ask your attorney or accountant for an individual assessment if you need to use a certified cash register system.