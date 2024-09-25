# Taxes

In most legislations, you are required to pay taxes for sales you make using pretix. 
pretix lets you make sure that you pay the correct amount of tax for each sale. 
You can set up a tax rule for each relevant tax rate, and then assign that tax rule to each individual product. 

The amount of taxes you need to pay for each product depend on your local legislation, the type of your business, and a number of other factors. 
The pretix documentation does not contain any information on the appropriate tax rates for your situation. 
Please speak to a professional tax consultant before setting tax rates in your shop. 

{% include "warning-tax.md" %}

## Prerequisites

Taxes are handled on the event level, so you have to create an event first. 
If you want to use reverse charge or more advanced tax application rules, the box next to "Ask for VAT ID" in the invoicing settings needs to be checked.

## General usage

pretix allows you to set up a tax rule for each tax rate that is relevant for your situation.
Then, you assign that tax rule to each individual product. 
If you are selling products with a 0% tax rate (such as gift cards), you still need to create a 0% tax rule first. 

### Creating tax rules 

In order to create a new tax rule, navigate to :navpath:Your event → :fa3-wrench: Settings → Tax rules:. 
This page displays a list of all tax rules that have been created for the event. 
To create a new tax rule, click the :btn-icon:fa3-plus: Create a new tax rule: button. 

This takes you to a dialog for creating the new tax rule. 
On the "General" tab, choose an "Official name" that will be displayed to customers in your shop. 
Provide a translation for each language you are using. 

Optionally, you may choose an "Internal name" that will only be displayed in the backend. 

Under "Tax rate", choose a rate in percent. 
For example, if your products are sold with the regular value-added tax rate in Germany, set the "Tax rate" to 19%. 

The box next to "The configured product prices include the tax amount" determines whether the price of a product with this tax rule is handled as its net price (before tax) or its gross price (after tax).  
By default, this box is checked, so all product prices with this tax rule are handled as gross prices (tax is included in the price). 
This means that a product with a listed price of €10.00 and a tax rate of 19% has a net price of €8.40, €1.60 worth of value-added tax, and a total gross price of €10.00. 

If you uncheck this box, all product prices with this tax rule are handled as net prices (tax is added on top of the listed price). 
A product with a price of €10.00 and a 19% tax rule will have €1.90 worth of taxes added on top of the net price, leading to a gross price of €11.90. 
This setting applies to all products that use this specific tax rule. 
It does **not** apply to all products in your shop. 

Click the :btn:Save: button once you are happy with your choices. 

### EU reverse charge

!!! Warning 
    Reverse charge rules are **not applicable** for most events handled with pretix. 
    We therefore **strongly recommend not to enable this feature** if you do not have a specific reason to do so. 
    According to article 52 of the [VAT directive](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32006L0112&from=EN) (page 17), the place of supply is always the location of your event. 
    Therefore, tax always has to be paid according to the laws of the country where the event is held, regardless of the location of the customer. 

“Reverse charge” is a rule in European Union VAT legislation that specifies how taxes are paid if the seller and buyer of a good reside in different EU countries. 
If the buyer is registered as a VAT-paying business in their country, you charge them only the net price without taxes and state that the buyer is responsible for paying the correct taxes. 

If you want to enable reverse charge, navigate to :navpath:Your event → :fa3-wrench: Settings → Tax rules:. 
Select the tax rule for which you want to enable reverse charge and switch to the :btn:Advanced: tab. 
Check the box next to "Use EU reverse charge taxation rules" and select your country from the "Merchant country" dropdown menu. 

If you enable the reverse charge feature and specify your merchant country, then the following process will be performed whenever an order is placed:
 - The user will first be presented with the “normal” prices (net or gross, as configured).
 - The user adds a product to their cart. 
   The cart will at this point always show gross prices including taxes. 
 - In the next step, the user can enter an invoice address. Tax will be removed from the price if one of the following statements is true:
   - The invoice address is in a non-EU country.
   - The invoice address is a business address in an EU-country different from the merchant country **and** has a valid VAT ID.
     In this second case, a reverse charge note will be added to the invoice.

VAT IDs are validated against the EU's validation web service. 
Should that service be unavailable, the user needs to pay VAT tax and reclaim the taxes at a later point in time with their government.

If your and your buyer's EU countries use different currencies, the invoice will include the total and VAT amount in the local currency of the buyer in addition to your event's currency. 

For existing orders, a change of the invoice address will **not** result in an automatic change of taxes. 
If you want to trigger this manually, navigate to :navpath:Your event → :fa3-shopping-cart: Orders → All orders: and click one of the orders in question. 
There, first click the “Check” button next to the VAT ID. 
Then, go to “Change products” and select the option “Recalculate taxes” at the end of the page.

During back-and-forth modification of taxation status, unfortunately there can be rounding errors of usually up to one cent from the intended price. This is unavoidable due to the flexible nature in which prices are being calculated.


### Assigning tax rules 

If you want to assign a tax rule to a new product you are creating, navigate to :navpath:Your event → :fa3-ticket: Products → Products:. 
Click the :btn-icon:fa3-plus: Create a new product: button. 
Under the "Price settings" subheading, click on the "Sales tax" drop-down menu and select the tax rule that you want to assign to the product. 
This list will use the internal name you specified on the tax rules settings page and the specified percentage. 
Once you have made your selection, click the :btn:Save and continue with more settings: button. 

If you want to assign a tax rule to an existing product, navigate to :navpath:Your event → :fa3-ticket: Products → Products:. 
Click the :btn-icon:fa3-edit: edit button next to the product in question and switch to the :btn:Price: tab. 
In the "Sales tax" drop-down menu, select the tax rule that you want to assign to the product. 
This list will use the internal name you specified on the tax rules settings page and the specified percentage. 
Once you have made your selection, click the :btn:Save: button. 


## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 