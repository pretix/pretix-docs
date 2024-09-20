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

## General usage

pretix allows you to set up a tax rule for each tax rate that is relevant for your situation.
Then, you assign that tax rule to each individual product. 
If you are selling products with a 0 % tax rate (such as gift cards), you still need to create a 0 % tax rule first. 

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
This means that a product with a listed price of €10.00 and a tax rate of 19.00 % has a net price of €8.40, €1.60 worth of value-added tax, and a total gross price of €10.00. 

If you uncheck this box, all product prices with this tax rule are handled as net prices (tax is added on top of the listed price). 
A product with a price of €10.00 and a 19.00 % tax rule will have €1.90 worth of taxes added on top of the net price, leading to a gross price of €11.90. 
This setting applies to all products that use this specific tax rule. 
It does **not** apply to all products in your shop. 

Click the :btn:Save button once you are happy with your choices. 

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

### Advanced settings  

## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 