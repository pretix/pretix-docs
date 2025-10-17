# Taxes

Most legislations require you to pay taxes on any sales you make using pretix. 
pretix gives you the tools you need to calculate the appropriate tax for each sale. 

Taxes are configured on the event level. 
During event creation, pretix prompts you to create one simple tax rule. 
This may already be enough for the most straightforward use cases. 
This article tells you how to create additional tax rules, how to configure complex custom tax rules, and how to assign them to products. 

This article does **not** tell you what taxes are appropriate for your individual situation. 
This depends on your local legislation, the type of your business, and a number of other factors. 
The pretix documentation does **not** contain any information on the appropriate tax rates for your situation. 
Speak to a professional tax consultant before setting tax rates in your shop. 

{% include "warning-tax-rules.md" %}

## Prerequisites

Taxes are handled on the event level, so you have to create an event first. 

## General usage

pretix allows you to set up a tax rule for each tax rate that is relevant for your situation.
Then, you assign that tax rule to each individual product. 

Tax rules are configured for each event individually. 
There is no default set of tax rules. 
You can only assign a tax rule to a product after you have created the tax rule. 
This is true even for a tax rate of 0%. 
If you are selling products with a 0% tax rate (such as [gift cards](../guides/gift-cards.md)), you still need to create a 0% tax rule first.

When it comes to tax rules for free products, the only material difference is the tax rate printed on the invoice. 
Create and assign the tax rule that you want to see on the invoice. 
pretix does not create invoices for orders that only contain free products. 

### Creating tax rules 

In order to create a new tax rule, navigate to :navpath:Your event → :fa3-wrench: Settings → Tax rules:. 
This page displays a list of all tax rules that you have created for the event. 
To create a new tax rule, click the :btn-icon:fa3-plus: Create a new tax rule: button. 

![Tax rule dialog. The 'General' tab is open, displaying options for official and internal name, tax rate, and whether to include the tax in the product price.](../assets/screens/tax/edit-rule.png "Tax rule advanced options" )

This takes you to a dialog for creating the new tax rule. 
On the "General" tab, choose an "Official name" that your shop will display to customers. 
Provide a translation for each language you are using. 

Optionally, you can choose an "Internal name" that the pretix backend will display to you and your team members. 

Under "Tax rate", choose a rate in percent. 
For example, if you sell products with the regular value-added tax rate in Germany, set the "Tax rate" to 19%. 

The box next to "The configured product prices include the tax amount" determines whether to handle the price of a product with this tax rule as its net price (before tax) or its gross price (after tax). 

By default, this setting is active, so pretix handles all product prices with this tax rule as gross prices (the price includes tax). 
This means that a product with a listed price of €10.00 and a tax rate of 19% has a net price of €8.40, €1.60 worth of value-added tax, and a total gross price of €10.00. 

If you uncheck the box, pretix handles all product prices with this tax rule as net prices (pretix adds tax on top of the listed price). 
A product with a price of €10.00 and a 19% tax rule will have €1.90 worth of taxes added on top of the net price, leading to a gross price of €11.90. 
This setting applies to all products that use this specific tax rule. 
It does **not** apply to all products in your shop. 

Click the :btn:Save: button to confirm your choices. 

### Custom tax rules

![Tax rule dialog. The 'Advanced' tab is open, displaying options for EU reverse charge, merchant country, and adding new custom rules.](../assets/screens/tax/advanced.png "Tax rule advanced options" )

!!! Note 
    Using custom tax rules is mutually exclusive with the EU reverse charge option. 
    If you have defined one or more custom tax rules, then the EU reverse charge taxation rule will **not** apply, even if the box next to "Use EU reverse charge taxation rules" is checked. 

pretix allows you to set "custom rules" if you have special requirements for the conditions in which to charge or not to charge value-added tax (VAT) on top of your sales. 
These "custom rules" are subordinate to a tax rule and optional. 

If you want to use custom rules specific to businesses with VAT IDs, you have to ask your customers for their VAT ID. 
Navigate to :navpath:Your event → :fa3-wrench: Settings → Invoicing:. 
Switch to the :btn:Address form: tab and ensure that the boxes next to "Ask for invoice address" and "Ask for VAT ID" are checked. 
Click the :btn:Save: button to confirm. 

In order to set custom tax rules, navigate to :navpath:Your event → :fa3-wrench: Settings → Tax rules:. 
Click the tax rule for which you want to set custom rules, switch to the :btn:Advanced: tab and click the :btn-icon:fa3-plus: Add a new rule: button. 

Under "Condition", in the first dropdown menu, select the country or territory where the custom rule will apply or select "Any country". 
In the second menu, select the type of customer (individual, business, or business with valid VAT ID) or select "Any customer". 

Under "Calculation", choose how pretix should calculate tax under the specified conditions (country and customer). 
If you want to charge a tax rate specific to the conditions you defined, select "Charge VAT" and enter the tax rate in the input field below. 
If you want to implement a reverse charge rule for the condition, select "Reverse charge" and leave the field below empty. 

The other options allow you to charge **no** tax, to require manual approval, or to forbid sales altogether for the condition you defined. 
You may leave the input field below empty in those cases. 

Under "Reason", you can select a legal reason for the tax rule you put into place. 
If the drop-down menu does **not** offer your specific reason, select a more general option. 
You can use the "Text on invoice" fields to add an explanation for the taxes charged to your customers' invoices. 

When a customer places an order, pretix will check the custom rules from top to bottom. 
The first rule matching the order decides if and how pretix will charge VAT. 
You can move the rules up or down the priority list using the arrow buttons :btn-icon:fa3-arrow-up:: and :btn-icon:fa3-arrow-down::. 

![Tax rule dialog. The 'Advanced' tab is open, displaying four custom rules, as described in the paragraph below.](../assets/screens/tax/custom-rules.png "Example for custom rules" )

For illustrative purposes, assume that a company in Germany is hosting an event which is eligible for EU reverse charge. 
Such a company might first create a rule for "Germany", applying to "Any customer" the calculation "Charge VAT". 
The tax rate would be 19.00% and the reason would be "Default tax code". 
The company might then create a rule for "European Union", applying to "Business with valid VAT ID" the calculation "Reverse charge" with the tax rate field left empty and the reason set to "Reverse charge". 

It might then create a rule for Austria, applying to "Any customer" the calculation "Charge VAT" with the tax rate set to the VAT rate of the country in question. 
It might then create the same rule for every single member state in the EU from Belgium to Sweden, always setting the appropriate deviating tax rate. 
Finally, the company might create a rule for "Any country", applying to "Any customer" the calculation "Charge VAT". 

In this example, if a company located in Austria with a valid VAT ID places an order, this matches both the second and the third rule. 
However, since pretix always checks custom rules top to bottom and only applies the first matching rule, the software will only apply the second rule from our list (European Union → "Business with valid VAT ID" → "Reverse charge") to the transaction. 

The order in which the hypothetical company arranged the rules here also ensures that no business from an EU country outside of Germany will be charged VAT on their transaction, as long as they provide a valid VAT ID while placing their order. 

!!! Note 
    The example case described above is for illustrating the use of the software only. 
    It does not constitute legal advice. 

### EU reverse charge

!!! Warning 
    Reverse charge rules are **not applicable** to most events handled with pretix. 
    We therefore **strongly recommend not to enable this feature** if you do not have a specific reason to do so. 
    According to article 52 of the [VAT directive](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32006L0112&from=EN) (page 17), the place of supply is always the location of your event. 
    Therefore, the applicable tax law will always be that of the country where the event is held, regardless of the location of the customer. 

!!! Note 
    The EU reverse charge feature is deprecated. 
    A future update of pretix will remove this feature. 
    Avoid using EU reverse charge if possible and define custom tax rules instead. 
    That way, you can tailor taxation rules to your individual use case and ensure you are complying with all relevant laws. 

!!! Note 
    Using custom tax rules is mutually exclusive with the EU reverse charge option. 
    If you have defined one or more custom tax rules, then the EU reverse charge taxation rule will not apply, even if the box next to "Use EU reverse charge taxation rules" is checked. 

"Reverse charge" is a rule in European Union VAT legislation that specifies how to calculate taxes if the seller and buyer of a good reside in different EU countries. 
If the buyer is registered as a VAT-paying business in their country, you charge them only the net price without taxes and state that the buyer is responsible for paying the appropriate taxes. 

If you want to use reverse charge, you have to ask your customers for their VAT ID. 
Navigate to :navpath:Your event → :fa3-wrench: Settings → Invoicing:. 
Switch to the :btn:Address form: tab and ensure that the boxes next to "Ask for invoice address" and "Ask for VAT ID" are checked. 
Click the :btn:Save: button to confirm. 

If you want to enable reverse charge, navigate to :navpath:Your event → :fa3-wrench: Settings → Tax rules:. 
Select the tax rule for which you want to enable reverse charge and switch to the :btn:Advanced: tab. 
Check the box next to "Use EU reverse charge taxation rules" and select your country from the "Merchant country" dropdown menu. 

If you enable the reverse charge feature and specify your merchant country, then pretix will perform the following process whenever a customer places an order:

 1. The shop presents the customer with net or gross prices as configured for the applicable tax rule (on the :btn:General: tab). 
 2. The customer adds a product to their cart. 
    The shop displays gross prices including taxes. 
 3. In the "Your information" step, the customer can enter their "Invoice information". 
    If the invoice address is in a non-EU country, then pretix will remove the tax from the price. 
    If the invoice address is a business address in an EU country other than the merchant country **and** has a valid VAT ID, then pretix will remove the tax from the price and add a reverse charge note to the invoice. 

pretix validates VAT IDs against the EU validation web service when the customer clicks the "Continue" button. 
If the service is unavailable at that moment, then the customer has to pay VAT tax and reclaim the taxes with their government at a later point. 

If your and your buyer's EU countries use different currencies, the invoice will include the total and VAT amount in both your event's currency and the local currency of the buyer. 

For existing orders, a change of the invoice address will **not** result in an automatic change of taxes. 
In order to trigger such a change manually, navigate to :navpath:Your event → :fa3-shopping-cart: Orders → All orders: and click one of the orders in question. 
Click the :btn:Check: button next to the VAT ID. 
Then, click the :btn-icon:fa3-edit: Change products: button. 
Under the "Other operations" heading, select one of the options next to "Recalculate taxes". 
Confirm your choices by clicking the :btn:Perform changes: button. 

!!! Note 
    Modifying tax status back and forth may introduce rounding errors of up to one cent from the intended price. 
    This is unavoidable due to the flexible manner of price calculation. 

### Assigning tax rules 

![Create product dialog. The last option is a dropdown menu labeled 'Sales tax'. The current selection is 'No taxation'. At the bottom of the page, there is a button labeled 'Save and continue with more settings'.](../assets/screens/tax/create-product.png "Create product dialog" )

If you want to assign a tax rule to a **new product** you are creating, navigate to :navpath:Your event → :fa3-ticket: Products → Products:. 
Click the :btn-icon:fa3-plus: Create a new product: button. 
Under the "Price settings" subheading, click on the "Sales tax" drop-down menu and select the tax rule that you want to assign to the product. 
This list will display the internal name you specified on the tax rules settings page and the specified percentage. 
Once you have made your selection, click the :btn:Save and continue with more settings: button. 

<br>

![Edit product dialog. The 'Price' tab is open. The second option is a dropdown menu labeled 'Sales tax'. The current selection is 'VAT (incl- 19.00% VAT)'. At the bottom of the page, there is a button labeled 'Save'.](../assets/screens/tax/edit-product.png "Edit product dialog" )

If you want to assign a tax rule to an **existing product**, navigate to :navpath:Your event → :fa3-ticket: Products → Products:. 
Click the :btn-icon:fa3-edit:: edit button next to the product in question and switch to the :btn:Price: tab. 
In the "Sales tax" drop-down menu, select the tax rule that you want to assign to the product. 
This list will display the internal name you specified on the tax rules settings page and the specified percentage. 
Once you have made your selection, click the :btn:Save: button. 

## Troubleshooting 

### Appropriate tax rule does not appear in the drop-down menu

If you are trying to assign a tax rate to a product, but the "Sales tax" drop-down menu does **not** display the appropriate tax rate, then you have to create that tax rate first. 
Follow the instructions in the section [Creating tax rules](taxes.md#creating-tax-rules) to create a tax rule with the name and rate that you need. 
After you have done that, edit your product. 
The tax rate will now appear in the "Sales tax" drop-down menu and you will be able to assign it. 

### International business customer places order without VAT ID 

If an international business customer places an order without giving you their VAT ID, you can manually edit the order in question. 
On the "Order details" page, click :btn-icon:fa3-edit: Change answers:. 
Under "Invoice information", select "Business or institutional customer". 
The page will now display a "VAT ID" field where you can enter the customer's VAT ID. 