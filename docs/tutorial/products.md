# Products

A product is anything that you sell via pretix: tickets, gift cards, meal passes, conference t-shirts and so on. You will be selling a variety of products in your shop. This article guides you through the process of creating products and making them available in your shop. We are going to start by creating categories to sort our products into. We will then create the following products: 
 - a basic admission ticket 
 - a discount ticket for students and members
 - a free speaker ticket that is only available with a voucher code 
 - a voucher for sending out invitation codes to your speakers 
 - stickers that come in three variants with different prices 
 - additional product
 - bundled product 
Finally, we are going to create quotas to determine and keep track of availability numbers for each product. Feel free to follow the methods described here while adapting the types of products, their names and prices to your event's specific needs. 

## Creating and editing categories

Categories serve three purposes: They help you keep track of all your different products in the backend; they let you group the tickets into sensible categories in your shop; and they separate standalone products from additional products. 

We are going to sell additional products, i.e. products that can be purchased as add-ons to admission tickets in our shop. That means our next step is creating a category for additional products. Navigate to [Your event] → "Products" → "Categories". This page shows the list of all product categories, which at the moment should only include a single category named "Tickets". Click the :btn:+ Create a new category: button. Give the category a name such as "add-ons" and check the box next to "products in this category are add-on products". Click the :btn:Save: button at the bottom of the page. This takes you back to the product categories page, which now lists two entries: "Tickets" and your newly created category for add-ons. 

We are also going to create a category for extras such as a t-shirt and a book package. We will name it "Extras" and we will __not__ check the box next to "products in this category are add-on products". That means that people will still be able to buy products in this category even if they don't buy an admission ticket. 

## Creating and editing products 

Now that we have prepared all necessary categories for our products, we can set about editing the existing products and creating new ones to suit our needs. 

We will create a product that can be bundled with the basic ticket. Navigate to [Your event] → "Products" → "Products". The website should show you two tickets that have already been created along with the event: "regular ticket" and "reduced ticket".  Click the :btn:+ Create a new product: button. Enter "care box - medium" into the "item name" field and add appropriate translations for any languages you have activated. In the "category" field, select the add-on category you just created. Select "non-admission product" as the product type. On the "price" tab, set the price to 30.00 € and choose the appropriate sales tax. On the "availability" tab, check the box next to "only sell this product as part of a bundle". In our shop, we will also include a small care box at a price of 0 and a large care box at a price of 50 euros. So we repeat the same process for those two products with all the same settings, adjusting only name and price. 

We will edit the "regular ticket" so that we can base all other tickets on this one. Navigate to [Your event] → "Products" → "Products" and click the "regular ticket". This takes you to the "modify product" dialog. Change the English item name to "Standard Ticket" and add an appropriate translation for any other languages you have activated. Add a description that tells your customers what services are included in the ticket and what conditions have to be met in order for them to purchase it. You may also add a .png or .jpg file via the "product picture" button to further distinguish this products from the others in the shop. 

Next, click on the "price" tab. Change the "default price" field to your desired value. In our demo shop, that price is 250.00 €. Select the appropriate tax rate from the "sales tax" dropdown. Then switch to the "bundled products" tab. Click the :btn:+ Add a new bundled product: button. Select the previously created "care box - medium" at a quantity of 1 and a designated price part of 30.00 €. Click :btn:Save:. The medium care box is now included in the standard ticket by default and will be displayed to the customer as making up 30.00 € out of the total price of 250.00 € during purchase. 

We will now create a t-shirt product with multiple variations to reflect sizes ranging from S to XXL. Navigate to [Your event] → "Products" → "Products". Click the :btn:+ Create a new product: button. Name it "T-Shirt", put it in the "Extras" category and set it to "non-admission product". Under "product variations", select "product with multiple variations". Select the default price, in our case, 25 euros. Then click :btn:Save and continue with more settings:. 

Next, click on the "Variations" tab. There should be one variant called "Standard" here. Click on the name to expand the settings for that variant. Change the name to "S" to reflect clothes size S. You do not need to change any other settings here. Then scroll down and click the :btn:+ Add a new variation: button. Name it "M" and keep the other settings the way they are. Repeat the same process for sizes L, XL and XXL, perhaps adjusting the "default price" option if one of the sizes is more expensive. Then click :btn:Save:. 

## Creating and editing quotas 

A quota determines how many instances of your product can be sold. Every product has to be part of at least one quota before it becomes available in the shop. It is possible to add a product to more than one quota. In that case, it will only remain available as long as neither quota is sold out. In other words, if a product is part of several quotas, as soon as one quota is empty, the product will not be available anymore. Thus, we still have to create quotas and add our tickets to them. Navigate to [Your event] → "Products" → "Quotas". This page shows the list of all quotas for the event, which at the moment includes the "regular ticket" quota, containing the regular ticket as a product, and the "reduced ticket" quota, containing the reduced ticket as a product. The list also displays the total capacity and how many items are left for each quota. 

Click the :btn:change: button next to the "regular ticket" quota in the list. It has a pictogram of a pencil writing into a box on it. We renamed our "regular ticket" to "standard ticket", so we are also going to rename this quota to avoid confusion. Enter "Standard ticket" or your preferred name into the name field. Change the capacity to the maximum amount of tickets of this type that you want to sell, for example 1000. Leave the rest of the settings unchanged and click the :btn:Save: button. This takes you to a detailed overview of the status of the "standard ticket" quota. 

Next, we are going to create a quota for an additional product: our medium care box. Navigate back to "Quotas" and click the :btn:+ Create a new quota: button. Enter "care box - medium" into the name field and 1000 into the capacity field. In the "products" section, select "care box - medium" and make sure all other products are unselected. The medium care box is not an admission ticket but an additional product that will be bundled with the purchase of an admission ticket. So we do not want this quota to add to the total number of tickets available for the event. Thus, we are going to check the box next to "Ignore this quota when determining event availability" before clicking the :btn:Save: button. 

Our t-shirt product needs five different quotas: one for each product variant, i.e. one for each size. Navigate back to "Quotas" and click the :btn:+ Create a new quota: button. Call the new quota "T-Shirt S" and set the total capacity to the number of t-shirts of that size that you're going to sell, for example, 50. Select "T-Shirt - S" in the list of products and check the "Ignore this quota when determining event availability" box. Click :btn:Save: and navigate back to "Quotas". Click the "clone" button next to the quota you just created. Name the new quota "T-Shirt M", unselect "T-Shirt - S" from the list of products and select "T-Shirts - M" instead. Adjust the total capacity if necessary. Click :btn:Save: and repeat the same process for sizes L, XL and XXL, again, adjusting the total capacity as needed. If you now navigate back to [Your event] → "Products" → "Products" → "T-Shirt" and click on the "Variations" tab, there should be no more yellow boxes warning you that you need to add the product and variations to a quota before they can be sold. 

 - when to create a product with/without variants 
 - explain how to create some sensible default tickets for the given use case, for example hosting a conference
 - explain variants, additional products, bundles etc. before creating products 
 - ticket design and format (paper ticket, online only...) (maybe move this to a standalone article)
