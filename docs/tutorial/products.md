# Products

A product is anything sold via pretix: tickets, gift cards, conference t-shirts and so on. 
We will be selling a variety of products in our shop. 
In this article, we will cover the process of creating the following products and making them available in our shop: 

 - a basic admission ticket 
 - a discount ticket for students and members
 - a free speaker ticket requiring manual approval before purchase 
 - stickers that come in three variants with different prices 

We are going to start by creating categories to sort our products into, then we will create the products themselves, and lastly, we are going to create quotas to determine and keep track of availability numbers for each product. 

## Creating and editing categories

Categories can help us group products into sensible categories both in the backend and in our shop. 
They also separate standalone products from additional products. 
We are not only going to sell admission tickets in our shop, but also extras such as stickers. 
That means our next step is to create a category for those extras. 
For that, we will navigate to [Event] → "Products" → "Categories". 
This page shows the list of all product categories, which at the moment should only include a single category named "Tickets". 
We will click the :btn:+ Create a new category: button and give the category a name such as "Extras". 
Clicking the :btn:Save: button at the bottom of the page takes us back to the product categories page, which now lists two entries: "Tickets" and our newly created category named "Extras". 

## Creating and editing products

Now that we have prepared the necessary categories for our products, we can set about editing the existing products and creating new ones to suit our needs. 

First, we will edit the "regular ticket" so that we can base all other tickets on this one. 
In order to do that, we will navigate to [Event] → "Products" → "Products". 
The website should display two tickets that have already been created along with the event: "regular ticket" and "reduced ticket". 
We will click "regular ticket", which takes us to the "modify product" dialog. 
We will change the English item name to "Standard Ticket" and provide a German translation. 
We are going to add the following description: 
"Regular ticket granting access to the entire conference." 
Next, we will click on the "price" tab and change the "default price" to €250.00. 
We will also select the appropriate tax rate of 19% from the "sales tax" dropdown. 

### Discount ticket

We will now create the discount ticket based on the "standard ticket" we just edited. 
There are two advantages to  this approach: First, we do not have to repeat all the same steps, and second, we are reducing our risk of forgetting any of them. 
The "reduced ticket" is not needed anymore. 
We will navigate to [Event] → "Products" → "Products", click the red :btn:🗑: button next to the reduced ticket, and confirm that we want to delete it. 
Back on the product overview, we will click the :btn:Clone: button next to the standard ticket in order to clone it. 
We will name the new ticket "Discount ticket", provide a translation, change the "default price" to €120.00, and click the :btn:Save: button. 

A warning is now displayed in a yellow box at the top of the page, saying: 
"Please note that your product will not be available for sale until you have added your item to an existing or newly created quota." 
This warning will also appear during the creation of subsequent products. 
We can safely ignore it for now because we will take care of adding products to quotas in the very next section of this article. 
That will make the warning disappear. 

On the next page, we have to adjust the "description" field to inform our customers of the prerequisites for access to the discounted ticket. 
Our description reads:
"This ticket is only valid if you provide student ID or member ID during check-in."
We will then switch to the "price" tab, change the "default price" to €120.00 and the original price to the price of the standard ticket, i.e. €250.00. 
The original price will be displayed as struck-through and the new default price will be displayed in bold green, highlighting the discount price. 
Then, we will go to the "check-in and validity" tab and check the box next to "requires special attention". 
We have to provide instructions for the person operating the check-in at our event in the "check-in text" field. 
Our instructions say: "Check for student ID/member ID". 
We will then click the :btn:Save: button. 

### Speaker ticket

Next, we are going to create a speaker ticket that is free, but requires manual approval before purchase. 
For that, we will navigate to [Event] → "Products" → "Products" and click the :btn:Clone: button next to the standard ticket in order to clone it. 
We will name the new ticket "Speaker ticket", provide a translation, and change the "default price" to €0.00, leave the other options on this page unchanged and click the :btn:Save and continue with more settings: button. 
We will check the box next to "Buying this product requires approval". 
This means that every order placed in our shop that includes this type of ticket will first enter an "approval pending" state. 
Even if the order also includes products that do not require approval, the order will still enter the "approval pending" state. 
It will be necessary to to manually review and approve every order that includes this ticket in order to confirm that it has been ordered by one of our invited speakers. 
We will then click the :btn:Save: button. 

### Product with variants

After having created all the admission products we need, we will now create a sticker product with multiple variants: purple, black, and glitter. 
For that, we will navigate to [Event] → "Products" → "Products" and click the :btn:+ Create a new product: button. 
We will name the product "Sticker", set it to "non-admission product" and put it in the "Extras" category. 
Under "product variations", we will select "product with multiple variations". 
We will set the default price to €5.00. 
Then, we will click :btn:Save and continue with more settings:. 

Next, we will click on the "Variations" tab. 
There should be one variant called "Standard" here. 
We will click the name to expand the settings for that variant and change the name to "Purple". 
It is not necessary to change any other settings here. 
Then, we will scroll down and click the :btn:+ Add a new variation: button. 
We will name this new variant "Black" and keep the other settings the way they are. 
We will repeat the same process for the "Glitter" variant and set the "default price" option for that variant to €7.50. 
Then, we will click :btn:Save:. 

## Creating and editing quotas 

A quota determines how many instances of our product can be sold. 
Every product has to be part of at least one quota before it becomes available in the shop.
In this section, we are going to create quotas and add our products to them. 

We will navigate to [Event] → "Products" → "Quotas". 
This page shows the list of all quotas for the event, which at the moment includes the "regular ticket" quota, containing the standard ticket as a product, and the "reduced ticket" quota, not containing any ticket. 
The list also displays the total capacity and how many items are left for each quota. 

### Quotas for tickets 

We will click the :btn:change: button next to the "regular ticket" quota in the list. 
Since we have renamed our "regular ticket" to "Standard ticket", we are also going to rename this quota to avoid confusion. 
We will enter "Standard ticket" into the name field and change the capacity to 1000 because that is the maximum amount of tickets of this type that we want to sell. 
We will leave the rest of the settings unchanged and click the :btn:Save: button. 
This takes us to a detailed overview of the status of the "Standard ticket" quota. 

Our discount ticket also needs to be assigned to a quota. 
In order to do that, we will navigate back to [Event] → "Products" → "Quotas" and click the :btn:change: button next to the "reduced ticket" quota. 
We will rename it to "Discount ticket" and set its number to 900 because that is the maximum number of discount tickets we want to sell. 
In the list of products, we will check the box next to "Discount ticket". 

Our speaker ticket needs to be assigned to a quota, too. 
We will now navigate back to [Event] → "Products" → "Quotas" and click the :btn:+ Create a new quota: button. 
We will name the new quota "Speaker ticket" and set its number to 100 because that is the expected number of speakers at our event. 
In the list of products, we will check the box next to "Speaker ticket". 

### Quotas for variants 

Our sticker product needs three different quotas: one for each product variant. 
We will navigate back to "Quotas" and click the :btn:+ Create a new quota: button. 
We will call the new quota "Sticker purple" and set the total capacity to 100 because that is the number of stickers in that color that we're going to sell. 
Then, we will select "Sticker - Purple" in the list of products. 
The purple sticker is not an admission ticket but an additional product that can be purchased in the same shop. 
We do not want this quota to add to the total number of tickets available for the event. 
Thus, we are going to check the box next to "Ignore this quota when determining event availability" before clicking the :btn:Save: button. 

Since we still need quotas for the other variants of the product, we will navigate back to "Quotas" and click the "clone" button next to the sticker quota we just created. 
We will name the new quota "Sticker Black", unselect "Sticker - Purple" from the list of products and select "Sticker - Black" instead.  
Finally, we will click :btn:Save: and repeat the same process for the glitter color, adjusting the total capacity as needed. 

If we now navigate back to [Event] → "Products" → "Products" → "Sticker" and click on the "Variations" tab, there should be no more yellow boxes warning us that we need to add the product and variants to a quota before they can be sold. 
