# Sweden

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Sweden, VAT ("Mervärdesskatt", "Mons") may apply.
You can configure all Swedish VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Sweden currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).
There are widespread formats for B2B e-invoicing, including EDIFACT, Svefaktura, and PEPPOL.
pretix currently does not support these but is planning to provide a PEPPOl integration.

Sweden mandates e-invoices for transactions between businesses and the government (B2G) using the PEPPOL network.
pretix is planning to provide a PEPPOL integration.

More information is available on the website of the European Commission: [eInvoicing in Sweden](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Sweden).

## pretixPOS

Use of a cash register ist [mandatory](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/businessesandemployers/startingandrunningaswedishbusiness/cashregisters.4.57cadbbd15a3688ff44ddf9.html) in Sweden in most cases.
The cash register must follow Swedish regulations including the use of a certified control unit.
pretixPOS does **not** support this and can therefore **not** be used as a cash register in Sweden.
