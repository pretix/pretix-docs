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

## How To 

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

By default, the box next to "The configured product prices include the tax amount" is checked. 
Uncheck this box if you want to add the tax rate on top of the specified product price. 
This applies to all products that use this specific tax rule. 

Click the :btn:Save button once you are happy with your choices. 

### Applying tax rules 

## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 