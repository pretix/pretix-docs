# Spain

{% include "warning-tax-law.md" %}

## Value-added Tax (VAT)

When selling goods and services in Spain, VAT ("Impuesto sobre el Valor Añadido", "IVA") may apply.
You can configure all Spanish VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Spain is planning to introduce mandatory electronic invoicing for business-to-business (B2B) transactions starting in 2026.
Additionally, digital signatures of invoices are already mandatory.
pretix does **not** support this, but it is possible to sell tickets through pretix and issue invoices outside of pretix.

More information is available on the [website of the Spanish Government](https://www.facturae.gob.es/) as well as the website of the European Commission: [eInvoicing in Spain](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Spain).

## pretixPOS

The use of cash-registers in Spain is complicated to assess as it differs by region and is dynamically changing.
For example, Basque Country is currently implementing [TicketBAI](https://www.gipuzkoa.eus/es/web/ogasuna/ticketbai)
Additional regulations like [Immediate Supply of Information (SII)](https://sede.agenciatributaria.gob.es/Sede/en_gb/iva/suministro-inmediato-informacion.html) and [Verifactu](https://sede.agenciatributaria.gob.es/Sede/en_gb/iva/sistemas-informaticos-facturacion-verifactu.html) might affect the requirements as well.

Talk to your attorney or accountant to find out what requirements affect you and if you can use pretixPOS.