# Products

A product is anything that you sell via pretix. A ticket is a product. A gift card is a product. A meal pass is a product. A conference t-shirt is a product. You will be selling a variety of products in your shop. Some of those products will be admission tickets. Some of them will be additional products. This article will guide you through the process of creating products and making them available in your shop. The result will look similar to the [pretix demo conference](https://pretix.eu/demoshops/democon/). 

## Editing products 

We are going to sell additional products, i.e. products that can be purchased as add-ons to admission tickets in our shop. That means our first step is creating a category for additional products. Navigate to [Your event] → "Products" → "Categories". This page shows the list of all product categories, which at the moment should only include a single category named "Tickets". Click the :btn:+ Create a new category: button. Name the category "add-ons" or something similar and check the box next to "products in this category are add-on products". Click the :btn:Save: button at the bottom of the page. This will take you back to the product categories page, which now lists two entries: "Tickets" and your newly created category for add-ons. 

Next, we will create a product that can be bundled with the basic ticket. Navigate to [Your event] → "Products" → "Products". The website should show you two tickets that have already been created along with the event: "regular ticket" and "reduced ticket".  Click the :btn:+ Create a new product: button. Enter "care box - medium" into the "item name" field and add appropriate translations for any languages you have activated. In the "category" field, select the add-on category you just created. Select "non-admission product" as the product type. On the "price" tab, set the price to 30.00 € and choose the appropriate sales tax. On the "availability" tab, check the box next to "only sell this product as part of a bundle". 

We will edit the "regular ticket" so that we can base all other tickets on this one. Click the "regular ticket". This takes you to the "modify product" dialog. Change the English item name to "Standard Ticket" and to an appropriate translation in any other languages you have activated. The English description we use in the demo shop is the following: 

    "This is a simple ticket where workshops can be booked as additional products. Additional products can be set up so that they can also be rebooked later. It also includes the medium care package as a bundle." 

Add a description that tells your customers what services are included in the ticket and what conditions have to be met in order for them to purchase it  in the "description" field. Add an appropriate translation if applicable. You may also add a .png or .jpg file via the "product picture" button to further distinguish this products from the others in the final shop. 

Next, click on the "price" tab. Change the "default price" field to your desired value. In our demo shop, that price is 250.00 €. Select the appropriate tax rate from the "sales tax" dropdown. 


 

 - what is a quota
 - what is a category 
 - what is a ticket 
 - when to create a product with/without variants 
 - explain how to create some sensible default tickets for the given use case, for example hosting a conference
 - explain variants, additional products, bundles etc. before creating products 
 - ticket design and format (paper ticket, online only...) (maybe move this to a standalone article)
