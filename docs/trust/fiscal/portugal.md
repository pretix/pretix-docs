# Portugal

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Portugal, VAT ("Imposto sobre o valor acrescentado", "IVA") may apply.
You can configure all Portuguese VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

All invoices in Portugal must be created by [certified invoicing software](https://vat-one-stop-shop.ec.europa.eu/national-vat-rules/portugal-vat-rules_en) and submitted electronically to the tax authority (Autoridade Tributária e Aduaneira, AT).

<!-- md:hosted -->

On pretix Hosted, sending invoices to AT is supported through a partner.
To get started, go to :navpath:Your organizer → :fa3-wrench: Settings → Plugins: and enable the plugin "E-invoicing for Portugal (via Invopop)".
Then, go to :navpath:Your organizer → :fa3-wrench: Settings → E-invoicing (PT):, fill out details about your company and follow the displayed steps for obtaining AT credentials.

Once you have completed this setup, you can go to :navpath:Your event → :fa3-wrench: Settings → Plugins: and enable the plugin "E-invoicing for Portugal (via Invopop)" for your event.
Then, to :navpath:Your event → :fa3-wrench: Settings → E-invoicing: fill out the settings and follow all recommendations.
Invoices will be transmitted to SdI automatically through our partner Invopop S.L. and their subprocessor RUPEAL.
An additional price per invoice is charged according to our [price list](https://pretix.eu/about/en/pricing).

pretix Enterprise and pretix Community currently do not support the Portuguese invoicing process.

More information is available on the website of the European Commission: [eInvoicing in Portugal](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Portugal).

## pretixPOS

When operating a cash register in Portugal, the cash register software must be certified by the fiscal authority.
pretixPOS is currently **not** certified and can therefore **not** be used as cash register software in Portugal.
