# Product structure guide

A product is anything sold via pretix: tickets, gift cards, conference t-shirts and so on. 
pretix offers you almost unlimited possibilities for configuring and structuring products. 
This article guides you through the basic process of creating a product and explain how to implement a complex product structure with some of the more advanced features of pretix. 

## Prerequisites

Products are configured on the event level, so you have to create an event first. 

## General usage

This section guides you through the basic process of product creation. 
This involves first creating categories, then the products themselves, and finally quotas. 

### Creating and editing categories

![Page titled 'Product categories', showing a list of categories only containing 'Tickets' and a button for creating a new category.](../assets/screens/products/categories.png "Product categories screenshot") 

Categories separate standalone products from additional products. 
You have to have at least two different categories if you want to sell not only admission tickets, but also extras such as stickers. 
You also need an extra category if you are planning to use the cross-selling feature. 
Finally, categories can help you group products into sensible categories both in the backend and in your shop. 

In order to edit categories, navigate to :navpath:Your event → :fa3-ticket: Products → Categories:. 
This page shows the list of all product categories. 

Click the :btn-icon:fa3-plus: Create a new category: button and give the new category a descriptive name. 
Choose the category type depending on the type of products in this category: normal, add-on, cross-selling, or normal + cross-selling. 
Click the :btn:Save: button at the bottom of the page. 
This takes you back to the product categories page, which now also lists the newly created category. 

You can also edit an already existing category and change its name, description and type by clicking the :btn-icon:fa3-edit:: edit button next to it in the list. 

### Creating and editing products

![Page titled 'Products', showing a list of products containing two entries and a button for creating a new product.](../assets/screens/products/products.png "Products screenshot") 

Now that we have prepared the necessary categories for our products, we can set about editing the existing products and creating new ones to suit our needs. 

First, we will edit the "Regular ticket" so that we can base all other tickets on this one. 
In order to do that, we will navigate to :navpath:Event → :fa3-ticket: Products → Products:. 
The website should display two tickets that have already been created along with the event: "Regular ticket" and "Reduced ticket". 
We will click "Regular ticket", which takes us to the "Modify product" dialog. 

We will change the English item name to "Standard Ticket" and provide a German translation. 
We are going to add the following description: 
"Regular ticket granting access to the entire conference." 
Next, we will click on the :btn:Price: tab and change the "Default price" to €250.00. 
We will also select the appropriate tax rate of 19% from the "Sales tax" dropdown. 

Once we have done that, we are going to click the :btn:Save: button. 

## Creating and editing quotas 

A quota determines how many instances of our product can be sold. 
Every product has to be part of at least one quota before it becomes available in the shop.
In this section, we are going to create quotas and add our products to them. 

We will navigate to :navpath:Event → :fa3-ticket: Products → Quotas:. 
This page shows the list of all quotas for the event, which at the moment includes the "Regular ticket" quota, containing the standard ticket as a product, and the "Reduced ticket" quota, not containing any ticket. 
The list also displays the total capacity and how many items are left for each quota. 

## Applications 

### Multiple price levels 

### Early bird products 

### Upselling extras 

### Workshops at a conference 

### Discount packages 

### Group discounts 

### Restricted audience 

### Time slots 

### Season tickets

### Mixed taxation 

## Troubleshooting 

### A product does not appear in the ticket shop 

If you have created a product and it is not displayed in your ticket shop, perform the following checks: 

 1. Check if the product’s "active” checkbox is enabled.

 2. Check if the product’s "Available from” or "Available until” settings restrict it to a date range.

 3. Check if the product’s checkbox "This product will only be shown if a voucher matching the product is redeemed.” is enabled. 
 If this is the case, the product will  only be shown if the customer redeems a voucher that directly matches to this product. 
 It will not be shown if the voucher only is configured to match a quota that contains the product.

 4. Check if the product is in a category that has the "Products in this category are add-on products” checkbox enabled. 
 If this is the case, the product won’t show up on the shop front page, but only in the first step of checkout when a product in the cart allows to add add-on products from this category.

 5. Check that a quota exists that contains this product. 
 If your product has variations, check that at least one variation is contained in a quota. 
 If your event is an event series, make sure that the product is contained in a quota that is assigned to the series date that you access the shop for.

 6. If the sale period has not started yet or is already over, check the "Show items outside presale period” setting of your event.

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 