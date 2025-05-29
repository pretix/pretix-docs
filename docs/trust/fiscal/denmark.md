# Denmark

{% include "warning-tax-law.md" %}

## Value-added tax (VAT)

When selling goods and services in Denmark, VAT ("Merværdiafgift o Moms", "DPH") may apply.
You can configure all Danish VAT rates in pretix using [tax rules](../../guides/taxes.md), including more complex tax cases (e.g. intra-EU reverse charge transactions).

## Invoicing

### E-invoicing

Denmark currently does not require sending electronic invoices in a structured format for transactions between businesses (B2B) or businesses and consumers (B2C).
Denmark only mandates e-invoices for transactions between businesses and the government (B2G).
pretix currently does not support this. 

More information is available on the website of the European Commission: [eInvoicing in Denmark](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+in+Denmark).

## pretixPOS

When operating in Denmark, you need to be able to supply your financial data in the "Standard Audit File for Tax (SAF-T)" format during a tax audit.
This is not supported by pretix, but might be supported by a bookkeeping system where you can import your data from pretix.
Please consult your attorney or accountant for more information.

We are not aware of other specific requirements on cash registers in Denmark.
Therefore, we believe pretixPOS can generally be used in Denmark.