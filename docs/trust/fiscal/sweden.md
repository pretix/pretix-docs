# Sweden

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Sweden, VAT ("Mervärdesskatt", "Mons") may apply.
You can configure all Swedish VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Sweden currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).
Widespread formats for B2B e-invoicing include EDIFACT, Svefaktura, and with Peppol.
A native integration of pretix with Peppol is available as a plugin as part of our pretix Hosted product.

Sweden mandates e-invoices for transactions between businesses and the government (B2G) using the Peppol network.
A native integration of pretix with Peppol is available as a plugin as part of our pretix Hosted product.

More information is available on the website of the European Commission: [eInvoicing in Sweden](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Sweden).

## pretixPOS

According to the [website of the Swedish Tax Agency](https://www.skatteverket.se/servicelankar/otherlanguages/inenglishengelska/businessesandemployers/startingandrunningaswedishbusiness/cashregisters.4.57cadbbd15a3688ff44ddf9.html), Skatteverket, use of a cash register is mandatory in Sweden in most cases.
The cash register must follow Swedish regulations including the use of a certified control unit.
pretixPOS does **not** support this and can therefore **not** be used as a cash register in Sweden.
