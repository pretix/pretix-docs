# Products

A product is anything that is sold via pretix: tickets, gift cards, meal passes, conference t-shirts and so on. 
We will be selling a variety of products in our shop. 
In this article, we will go through the process of creating products and making them available in our shop. 
We are going to start by creating categories to sort our products into. 
We will then create the following products: 

 - a basic admission ticket 
 - a discount ticket for students and members
 - a free speaker ticket that requires manual approval before purchase 
 - stickers that come in three variants with different prices 

Finally, we are going to create quotas to determine and keep track of availability numbers for each product. 

## Creating and editing categories

Categories serve three purposes: They help keep track of all the different products in the backend; they let us group the tickets into sensible categories in our shop; and they separate standalone products from additional products. 

We are not only going to sell admission tickets in our shop, but also extras such as stickers. 
That means our next step is creating a category for those extras. 
For that, we will navigate to [Event] → "Products" → "Categories". 
This page shows the list of all product categories, which at the moment should only include a single category named "Tickets". 
We will click the :btn:+ Create a new category: button and give the category a name such as "Extras". 
We will __not__ check the box next to "products in this category are add-on products". 
Leaving that box unchecked means that people will still be able to purchase products in this category even if they don't buy an admission ticket. 
Clicking the :btn:Save: button at the bottom of the page takes us back to the product categories page, which now lists two entries: "Tickets" and our newly created category for extras. 

## Creating and editing products

Now that we have prepared all necessary categories for our products, we can set about editing the existing products and creating new ones to suit our needs. 

We will edit the "regular ticket" so that we can base all other tickets on this one. 
We will navigate to [Your event] → "Products" → "Products". 
The website should display two tickets that have already been created along with the event: "regular ticket" and "reduced ticket". 
We will click the "regular ticket". 
This takes us to the "modify product" dialog. 
We will change the English item name to "Standard Ticket" and the German translation to "Standard-Ticket". 
We are going to add the following description: 
"Regular ticket that gives you access to the entire conference." 
We are also going to add a .png file via the "product picture" button to further distinguish this products from the others in the shop. 
Next, we will click on the "price" tab and change the "default price" to 250.00 €. 
We will also select the appropriate tax rate of 19% from the "sales tax" dropdown. 

We will now create a discount ticket. 
We are going to base it on the "standard ticket" we just edited so that we don't have to repeat all the same steps. 
That means that the "reduced ticket" is not needed anymore. 
We will navigate to [Your event] → "Products" → "Products", click the red :btn:🗑: next to the reduced ticket, and confirm that we want to delete it. 
This takes us back to the product overview. 
We will click the :btn:Clone: button next to the standard ticket in order to clone it. 
We will name the new ticket "Discount ticket", provide a translation, and change the "default price" to 120.00 €. 
We will leave the other options on this page unchanged and click the :btn:Save: button. 

A warning will now be displayed in a yellow box at the top of the page, saying: 
"Please note that your product will not be available for sale until you have added your item to an existing or newly created quota." 
This warning will also be displayed during the creation of subsequent products. 
We are going to ignore it for now. 
We will tackle adding products to quotas in the next section. 
That will take care of the problem and make the warning go away. 

On the next page, we have to adapt the "description" field so that it tells our customers what criteria they have to fulfill to get access to the discounted ticket. 
Our description says the following: 
"This ticket is only valid if you provide a valid student ID or member ID during check-in."
We will upload a different product picture on this site to better distinguish the discount ticket from the standard one. 
We will then switch to the "price" tab and change the original price to the price of the standard ticket, i.e. 250.00 €. 
Then, we will to the "check-in and validity" tab and check the box next to "requires special attention". 
We have to provide instructions for the person operating the check-in at your event in the "check-in text" field. 
Our instructions say the following: 
"Only admit the attendee to the event if they can provide a valid student ID or member ID during check-in." 
We will then click the :btn:Save: button. 

We will now create a speaker ticket that is free, but requires manual approval before purchase. 
For that, we will navigate to [Event] → "Products" → "Products". 
We will click the :btn:Clone: button next to the standard ticket in order to clone it. 
We will name the new ticket "Speaker ticket", provide a translation, and change the "default price" to 0 euros. 
We will leave the other options on this page unchanged and click the :btn:Save and continue with more settings: button. 
We will check the box next to "Buying this product requires approval". 
This means that every order that arrives in our shop and includes this ticket will first enter an "approval" state. 
We will have to manually review and approve every order that includes this ticket in order to confirm that it has been ordered by one of our invited speakers. 
We will then click the :btn:Save: button. 

We will now create a sticker product with multiple variations to reflect different colors: purple, black, and glitter. 
For that, we will navigate to [Event] → "Products" → "Products". 
We will click the :btn:+ Create a new product: button. 
We will name the product "Sticker", set it to "non-admission product" and put it in the "Extras" category. 
Under "product variations", we will select "product with multiple variations". 
We will set the default price to 5.00 €. 
Then, we will click :btn:Save and continue with more settings:. 

Next, we will click on the "Variations" tab. 
There should be one variant called "Standard" here. 
We will click the name to expand the settings for that variant and change the name to "Purple". 
We do not need to change any other settings here. 
Then, we will scroll down and click the :btn:+ Add a new variation: button. 
We will name this new variation "Black" and keep the other settings the way they are. 
We will repeat the same process for the "Glitter" color variation and set the "default price" option for that variant to 7.50 €. 
Then, we will click :btn:Save:. 

## Creating and editing quotas 

A quota determines how many instances of your product can be sold. 
Every product has to be part of at least one quota before it becomes available in the shop. 
A product can be part of more than one quota. 
In that case, it will only remain available as long as neither quota is sold out. 
In other words, if a product is part of several quotas, as soon as one of those quotas is empty, the product will not be available anymore. 
For most use cases, it is enough to add every product to one quota only. 
This section will tell you how. 

Navigate to [Your event] → "Products" → "Quotas". 
This page shows the list of all quotas for the event, which at the moment includes the "regular ticket" quota, containing the regular ticket as a product, and the "reduced ticket" quota, containing the reduced ticket as a product. 
The list also displays the total capacity and how many items are left for each quota. 

Click the :btn:change: button next to the "regular ticket" quota in the list. 
It has a pictogram of a pencil writing into a box on it. 
We renamed our "regular ticket" to "Standard ticket", so we are also going to rename this quota to avoid confusion. 
Enter "Standard ticket" or your preferred name into the name field. 
Change the capacity to the maximum amount of tickets of this type that you want to sell, for example 1000. 
Leave the rest of the settings unchanged and click the :btn:Save: button. 
This takes you to a detailed overview of the status of the "Standard ticket" quota. 

Repeat the same process for the discount ticket and speaker ticket. 
Name the quota for the discount ticket "Discount ticket" and set its number to the maximum number of discount tickets you want to sell. 
In our case, that number is 900. 
Name the quota for the speaker ticket "Speaker ticket" and set its number to the number of speakers at your event. 
In our case, that number is 100. 

Our sticker product needs three different quotas: one for each product variant, i.e. one for each color. 
Navigate back to "Quotas" and click the :btn:+ Create a new quota: button. 
Call the new quota "Sticker purple" and set the total capacity to the number of stickers in that color that you're going to sell, for example, 100. 
Select "Sticker - Purple" in the list of products. 
The purple sticker is not an admission ticket but extra product that can be purchased in the same shop. 
We do not want this quota to add to the total number of tickets available for the event. 
Thus, we are going to check the box next to "Ignore this quota when determining event availability" before clicking the :btn:Save: button. 

Navigate back to "Quotas". 
Click the "clone" button next to the sticker quota you just created. 
Name the new quota "Sticker Black", unselect "Sticker - Purple" from the list of products and select "Sticker - Black" instead. 
Adjust the total capacity if necessary. 
Click :btn:Save: and repeat the same process for the glitter color, again, adjusting the total capacity as needed. 

If you now navigate back to [Your event] → "Products" → "Products" → "Sticker" and click on the "Variations" tab, there should be no more yellow boxes warning you that you need to add the product and variations to a quota before they can be sold. 