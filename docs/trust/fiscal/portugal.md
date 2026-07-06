# Portugal

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Portugal, VAT ("Imposto sobre o valor acrescentado", "IVA") may apply.
You can configure all Portuguese VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

All invoices in Portugal must be created by [certified invoicing software](https://vat-one-stop-shop.ec.europa.eu/national-vat-rules/portugal-vat-rules_en) and submitted electronically to the tax authority (Autoridade Tributária e Aduaneira, AT).

<!-- md:hosted -->

pretix Hosted supports sending invoices to AT through our partner Invopop S.L. and their subprocessor RUPEAL.
This feature is not available on pretix Enterprise and pretix Community.
In order to set up the transmission of invoices to the Portuguese tax authority, navigate to :navpath:Your organizer → :fa3-wrench: Settings → Plugins:. 
Open the :btn:Integrations: tab. 
The list on this page includes the  "E-invoicing for Portugal (via Invopop)" plugin. 
Click the :btn:Enable: button next to it.

In the list labeled "Events with active plugin", check the events for which you want to submit invoices to AT.
Alternatively, navigate to :navpath:Your event → :fa3-wrench: Settings → Plugins: and enable the plugin "E-invoicing for Portugal (via Invopop)" for your event.
Navigate to :navpath:Your organizer → :fa3-wrench: Settings → E-invoicing (PT):, fill out details about your company and follow the displayed steps for obtaining AT credentials.

Navigate to :navpath:Your event → :fa3-wrench: Settings → E-invoicing:, fill out the mandatory information and follow the recommendations on this page. 
pretix will automatically transmit invoices to AT through our partner Invopop S.L. and their subprocessor RUPEAL.
We will charge an additional fee per invoice according to our [price list](https://pretix.eu/about/en/pricing).


More information is available on the website of the European Commission: [eInvoicing in Portugal](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Portugal).

## pretixPOS

When operating a cash register in Portugal, the cash register software must be certified by the fiscal authority.
pretixPOS is currently **not** certified and can therefore **not** be used as cash register software in Portugal.
