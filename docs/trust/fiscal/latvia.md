# Latvia

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Latvia, VAT ("Pievienotās vertības nodoklis", "PVN") may apply.
You can configure all Latvian VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Latvia is introducing requirements on electronic invoicing and real-time reporting for transactions between businesses (B2B) starting in 2026.
The technical details of this are not yet published and we do not know if pretix will support this.

More information is available on the website of the European Commission: [eInvoicing in Latvia](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Latvia).

## pretixPOS

When operating a cash register in Latvia, the cash register must be [certified](https://likumi.lv/ta/en/en/id/265487) to conform with a [local technical standard](https://likumi.lv/ta/en/en/id/265486).
pretixPOS is not certified and therefore cannot be used in Latvia.

To our understanding, it is possible to use pretixPOS and a certified cash register side-by-side, using pretixPOS to create tickets and the certified cash register to record the payments.