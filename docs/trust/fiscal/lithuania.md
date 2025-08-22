# Lithuania

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Lithuania, VAT ("Pridetines vertes mokestis", "PVM") may apply.
You can configure all Lithuanian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Lithuania currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).

Lithuania only mandates e-invoices for transactions between businesses and the government (B2G) in a way compatible with the PEPPOL network.
pretix is planning to provide a PEPPOL integration.

Lithuania requires monthly reporting of all invoices through the "i.SAF" system.
pretix does not support this but you can implement this outside of pretix, e.g. through an accounting system that imports the pretix data.

More information is available on the website of the European Commission: [eInvoicing in Lithuania](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Lithuania).

## pretixPOS

When operating a cash register in Lithuania, the cash register must be certified according to [local legislation](https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/4cab53a0d91111eb866fe2e083228059?jfwid=bkaxm9ia).
pretixPOS does **not** support this and can therefore **not** be used as cash register software in Lithuania.