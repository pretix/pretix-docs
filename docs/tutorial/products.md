# Products

A product is anything that you sell via pretix: tickets, gift cards, meal passes, conference t-shirts and so on. You will be selling a variety of products in your shop. This article will guide you through the process of creating products and making them available in your shop using examples from the [pretix demo conference](https://pretix.eu/demoshops/democon/). Feel free to follow the methods described here while adapting the types of products, their names and prices to your event's specific needs. 

We are going to start by creating quotas for all of our products, then we will move on to additional products that can be added to the purchase of a conference ticket, and then finally we edit the basic ticket. This workflow can seem a little counterintuitive. But it represents the shortest possible route to a functional ticket shop by making sure that for every step of the process, the requirements have already been met. 

## Creating and editing categories

Categories serve three purposes: They help you keep track of all your different products in the backend; they let you group the tickets into sensible categories in your shop; and they separate standalone products from additional products. 

We are going to sell additional products, i.e. products that can be purchased as add-ons to admission tickets in our shop. That means our next step is creating a category for additional products. Navigate to [Your event] → "Products" → "Categories". This page shows the list of all product categories, which at the moment should only include a single category named "Tickets". Click the :btn:+ Create a new category: button. Give the category a name such as "add-ons" and check the box next to "products in this category are add-on products". Click the :btn:Save: button at the bottom of the page. This takes you back to the product categories page, which now lists two entries: "Tickets" and your newly created category for add-ons. 

We are also going to create a category for extras such as a t-shirt and a book package. We will name it "Extras" and we will __not__ check the box next to "products in this category are add-on products". That means that people will still be able to buy products in this category even if they don't buy an admission ticket. 

## Creating and editing products 

Now that we have prepared all necessary categories for our products, we can set about editing the existing products and creating new ones to suit our needs. 

We will create a product that can be bundled with the basic ticket. Navigate to [Your event] → "Products" → "Products". The website should show you two tickets that have already been created along with the event: "regular ticket" and "reduced ticket".  Click the :btn:+ Create a new product: button. Enter "care box - medium" into the "item name" field and add appropriate translations for any languages you have activated. In the "category" field, select the add-on category you just created. Select "non-admission product" as the product type. On the "price" tab, set the price to 30.00 € and choose the appropriate sales tax. On the "availability" tab, check the box next to "only sell this product as part of a bundle". 

We will edit the "regular ticket" so that we can base all other tickets on this one. Navigate to [Your event] → "Products" → "Products" and click the "regular ticket". This takes you to the "modify product" dialog. Change the English item name to "Standard Ticket" and add an appropriate translation for any other languages you have activated. The English description we use in the demo shop is the following: 

    "This is a simple ticket where workshops can be booked as additional products. Additional products can be set up so that they can also be rebooked later. It also includes the medium care package as a bundle." 

Add a description that tells your customers what services are included in the ticket and what conditions have to be met in order for them to purchase it. You may also add a .png or .jpg file via the "product picture" button to further distinguish this products from the others in the shop. 

Next, click on the "price" tab. Change the "default price" field to your desired value. In our demo shop, that price is 250.00 €. Select the appropriate tax rate from the "sales tax" dropdown. Then switch to the "bundled products" tab. Click the :btn:+ Add a new bundled product: button. Select the previously created "care box - medium" at a quantity of 1 and a designated price part of 30.00 €. Click :btn:Save:. The medium care box is now included in the standard ticket by default and will be displayed to the customer as making up 30.00 € out of the total price of 250.00 € during purchase. 

We will now create a t-shirt product with multiple variations to reflect sizes ranging from S to XXL. Navigate to [Your event] → "Products" → "Products". Click the :btn:+ Create a new product: button. Name it "T-Shirt", put it in the "Extras" category and set it to "non-admission product". Under "product variations", select "product with multiple variations". Select the default price, in our case, 25 euros. Then click :btn:Save and continue with more settings:. 

Next, click on the "Variations" tab. There should be one variant called "Standard" here. Click on the name to expand the settings for that variant. Change the name to "S" to reflect clothes size S. You do not need to change any other settings here. Then scroll down and click the :btn:+ Add a new variation: button. Name it "M" and keep the other settings the way they are. Repeat the same process for sizes L, XL and XXL, perhaps adjusting the "default price" option if one of the sizes is more expensive. Then click :btn:Save:. 

## Creating and editing quotas 

A quota determines how many instances of your product can be sold. Every product has to be part of at least one quota before it becomes available in the shop. Thus, we still have to create quotas and add our tickets to them. Navigate to [Your event] → "Products" → "Quotas". This page shows the list of all quotas for the event, which at the moment includes the "regular ticket" quota, containing the regular ticket as a product, and the "reduced ticket" quota, containing the reduced ticket as a product. The list also displays the total capacity and how many items are left for each quota. 

Click the :btn:change: button next to the "regular ticket" quota in the list. It has a pictogram of a pencil writing into a box on it. We want to rename our "regular ticket" to "standard ticket", so we are also going to rename this quota to avoid confusion. Enter "Standard ticket" or your preferred name into the name field. Change the capacity to the maximum amount of tickets of this type that you want to sell, for example 1000. Leave the rest of the settings unchanged and click the :btn:Save: button. This takes you to a detailed overview of the status of the "standard ticket" quota. 

Next, we are going to create a quota for an additional product: our medium care box. Navigate back to "Quotas" and click the :btn:+ Create a new quota: button. Enter "care box - medium" into the name field and 1000 into the capacity field. We have not created the associated product yet, so do not check any of the boxes next to "products". The medium care box is not an admission ticket but an additional product that will be bundled with the purchase of an admission ticket. So we do not want this quota to add to the total number of tickets available for the event. Thus, we are going to check the box next to "Ignore this quota when determining event availability" before clicking the :btn:Save: button. 

 - when to create a product with/without variants 
 - explain how to create some sensible default tickets for the given use case, for example hosting a conference
 - explain variants, additional products, bundles etc. before creating products 
 - ticket design and format (paper ticket, online only...) (maybe move this to a standalone article)
