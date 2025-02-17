# Products

A product is anything sold via pretix: tickets, gift cards, conference t-shirts and so on. 
pretix offers you almost unlimited possibilities for configuring and structuring products. 
This article guides you through the basic process of creating a product and explains several practical applications of some of the more advanced features of pretix. 

## Prerequisites

Products are configured on the event level, so you have to create an event first. 

## General usage

This section guides you through the basic process of product creation. 
This involves first creating categories, then the products themselves, and finally quotas. 
You cannot create a product without choosing a category for it. 
You cannot create a quota without adding at least one product to it. 
Thus, this guide will explain those steps in that order.

### Creating and editing categories

![Page titled 'Product categories', showing a list of categories only containing 'Tickets' and a button for creating a new category.](../assets/screens/products/categories.png "Product categories screenshot") 

Categories separate standalone products from additional products. 
If you want to sell not only admission tickets, but also extras such as stickers, you have to have at least two different categories. 
You also need an extra category if you are planning to use the cross-selling feature. 
Sorting products into categories can help you better keep track of them in the backend. 
Finally, your shop page will display products grouped by categories which can help customers find the article they are looking for more easily. 

In order to edit categories, navigate to :navpath:Your event → :fa3-ticket: Products → Categories:. 
This page shows the list of all product categories. 

Click the :btn-icon:fa3-plus: Create a new category: button and give the new category a descriptive name. 
Choose the category type depending on the type of products in this category: normal, add-on, cross-selling, or normal + cross-selling. 

Normal products are standalone products that can be purchased directly. 
Add-on products are products that are only offered as add-ons to normal products. 
Cross-selling products are products that are only offered in the cross-selling step as a customer is purchasing other products. 
Finally, products in the "normal + cross-selling" category are both offered as standalone products and in the cross-selling step. 
The "Cross-selling condition" setting below determines how products in cross-selling and normal + cross-selling categories are offered in your shop. 

Click the :btn:Save: button at the bottom of the page. 
This takes you back to the product categories page, which now also lists the newly created category. 

You can also edit an already existing category and change its name, description and type by clicking its name or the :btn-icon:fa3-edit:: edit button next to it in the list. 

### Creating and editing products

![Page titled 'Products', showing a list of products containing two entries and a button for creating a new product.](../assets/screens/products/products.png "Products screenshot") 

If you want to create or edit products, navigate to :navpath:Event → :fa3-ticket: Products → Products:. 
This page shows the list of all products. 
Click the :btn-icon:fa3-plus: Create a new product: button. 
Choose a name, a description, a default price and a sales tax and click the :btn:Save: button. 

You can also edit an already existing product by clicking its name or the :btn-icon:fa3-edit:: edit button next to it in the list. 

### Creating and editing quotas 

A quota determines how many instances of your product can be sold. 
Every product has to be part of at least one quota before it becomes available in the shop. 

If you want to create or edit quotas, navigate to :navpath:Event → :fa3-ticket: Products → Quotas:. 
This page shows the list of all quotas for the event as well as the total capacity and how many items are left for each quota. 

Click the :btn-icon:fa3-plus: Create a new quota: button. 
Choose a name and a capacity, check the products to be contained in this quota, and any advanced options, and then click the :btn:Save: button. 

You can also edit an already existing quota by clicking its name or the :btn-icon:fa3-edit:: edit button next to it in the list. 

## Applications 

This section covers advanced use cases and how to implement them using the options pretix offers for customizing products. 

### Workshops at a conference 

When running a conference, you might also organize a number of workshops with smaller capacity. 
To be able to plan, it would be great to know which workshops an attendee plans to attend.

#### Option A: Questions

Your first and simplest option is to just create a multiple-choice question. 
This has the upside of making it easy for users to change their mind later on, but will not allow you to restrict the number of attendees signing up for a given workshop – or even charge extra for a given workshop.

#### Option B: Add-on products with fixed time slots

The usually better option is to go with add-on products. 
Let's take for example the following conference schedule, in which the lecture can be attended by anyone, but the workshops only have space for 20 persons each:

| Time                | Room A     | Room B                         |
|---------------------|------------|--------------------------------|
| Wednesday morning   | Lecture    |                                |
| Wednesday afternoon | Workshop A | Workshop B                     |
| Thursday morning    | Workshop C | Workshop D (20 € extra charge) |

Assuming you already created one or more products for your general conference admission, we suggest that you additionally create:

 - A category called "Workshops" with the checkbox "Products in this category are add-on products" activated
 - A free product called "Wednesday afternoon" within the category "Workshops" and with two variations:
   - Workshop A
   - Workshop B
 - A free product called "Thursday morning" within the category "Workshops" and with two variations:
   - Workshop C
   - Workshop D with a price of 20 €
 - Four quotas for each of the workshops
 - One add-on configuration on your base product that allows users to choose between 0 and 2 products from the category "Workshops"

#### Option C: Add-on products with variable time slots

The above option only works if your conference uses fixed time slots and every workshop uses exactly one time slot. 
If your schedule looks like this, it's not going to work great:

| Time        | Room A                  | Room B                   |
|-------------|-------------------------|--------------------------|
| 09:00-11:00 | Talk 1                  | Workshop 1 (first half)  |
| 11:00-13:00 | Talk 2                  | Workshop 1 (second half) |
| 14:00-16:00 | Workshop 2 (first half) | Talk 3                   |
| 16:00-18:00 | Workshop 2 (second half | Talk 4                   |

This issue can be solved with the "Agenda constraints" plugin. 
In order to activate that plugin, navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and open the :btn:Features: tab. 
Seek out the "Agenda constraints" plugin in the list and click the :btn:Enable: button next to it. 

Then, create a product (without variations) for every single part that should be bookable (talks 1-4 and long workshops 1 and 2) as well as appropriate quotas for each of them.

All of these products should be part of the same category. 
In your base product (e.g. your conference ticket), you can then create an add-on product configuration allowing users to add products from this category.

If you edit these products, you will be able to enter the "Start date" and "End date" of the talk or workshop close to the bottom of the page. 
If you fill in these values, pretix will automatically ensure no overlapping talks are booked.

!!! Note

    This option is currently only available on pretix Hosted. 
    If you are interested in using it with pretix Enterprise, please contact sales@pretix.eu.


### Time slots 

A more advanced use case of pretix is using pretix for time-slot-based access to an area with a limited visitor capacity, such as a museum or other attraction. 
This guide will show you the quickest way to set up such an event with pretix.

First of all, when creating your event, you need to select that your event represents an "event series":

![](../assets/screens/products/create_step11.png "Create step 11")

For general instructions on how to set up an event series with pretix, refer to our guide on [event series](../event-series.md).

#### Creating slots

To create the time slots, you need to create a number of "dates" in the event series. 
Navigate to :navpath:Your event → :fa3-calendar: Dates: and click the :btn-icon:fa3-plus:Create many new dates: button. 
Then, first enter the pattern of your opening days. 
In the example, the museum is open week Tuesday to Sunday. 
We recommend to create the slots for a few weeks at a time, but not e.g. for a full year, since it will be more complicated to change things later.

![](../assets/screens/products/timeslots_create1.png "Timeslots create 1")

Then, scroll to the times section and create your time slots. 
You can do any interval you like. 
If you have different opening times on different days of the week, you will need to go through the creation process multiple times.

![](../assets/screens/products/timeslots_create_21.png "Timeslots create 21")

Scroll further down and create one or multiple quotas that define how many people can book a ticket for that time slot. 
In this example, 50 people in total are allowed to enter within every slot:

![](../assets/screens/products/timeslots_create_31.png "Timeslots create 31")

Do **not** create a check-in list at this point. 
We will deal with this further below in the guide. 
Now, press "Save" to create your slots.

!!! Warning

    If you create a lot of time slots at once, the server might need a few minutes to create them all in our system. 
    If you receive an error page because it took too long, please do not try again immediately but wait for a few minutes. 
    Most likely, the slots will be created successfully even though you saw an error.

#### Event settings

We recommend that you navigate to :navpath:Your Event → :fa3-wrench: Settings → General:. 
Open the :btn:Display: tab and set "Default overview style" to "Week calendar":

![](../assets/screens/products/timeslots_settings_11.png "Timeslots settings 11")

Now, your ticket shop should give users a nice weekly overview over all time slots and their availability:

![](../assets/screens/products/timeslots_presale1.png "Timeslots presale 1")

#### Check-in

If you want to scan tickets at the entrance to your event and only admit the ticket holders at their designated time, we recommend the following setup: 
Go to "Check-in" in the main navigation on the left and create a new check-in list. 
Give it a name and do not choose a specific data. 
We will use one check-in list for all dates. 
Then, go to the "Advanced" tab at the top and set up two restrictions to make sure people can only get in during the time slot they registered for. 

Under "Custom check-in rule", click the :btn-icon:fa3-plus-circle: Add condition: button and select "All of the conditions below (AND)" from the dropdown menu. 
Click :btn-icon:fa3-plus-circle: Add condition: again and select "Current date and time", then "is after", then "Event start". 
Leave the "Tolerance (minutes)" field empty. 
Click :btn-icon:fa3-plus-circle: Add condition: again and select "Current date and time", then "is before", then "Event end". 
Again, leave the "Tolerance (minutes)" field empty. 
Your custom check-in rule should now look like the one in the following screenshot: 

![Custom check-in rule page set up according to the instructions above.](../assets/screens/products/timeslots_checkinlists1.png "Timeslots check-in lists 1")

If you want, you can enter a tolerance of e.g. "10" if you want to be a little bit more relaxed and admit people up to 10 minutes before or after their time slot.

Now, download our Android or Desktop app and register it to your account. 
The app will ask you to select one of the time slots, but it does not matter, you can select any one of them and then select your newly created check-in list. 
That's it, you're good to go!

### Season tickets

Season tickets and similar time-based tickets are popular for swimming pools, sports clubs, theaters and lots of other types of venues. 
In this article, we show you different ways to set them up with pretix. 
Of course, other types of tickets such as week tickets, month tickets or tickets of ten can be created with the same mechanism.

There is a big difference between the two ways we show below.

With Option A, a customer who purchases a season ticket creates an account with their email address and a password and the season ticket will be saved in that account. 
If the customer wants to use the season ticket, they need to buy an additional free ticket for the specific event they want to visit. 
This makes sense for all events or venues with limited capacity or reserved seating, because it still allows you to set an upper limit of people showing up for a specific event or time slot.

With Option B, a customer who purchases a season ticket receives a single ticket with a single QR code that can be used an unlimited number of times. 
This makes sense if the capacity of your venue is virtually unlimited and you do not need to know in advance how many season ticket holders will show up.

#### Option A: Memberships and multiple tickets

Since this approach requires customers to be identified with a customer account, you first need to enable the customer accounts feature in your organizer settings in the "Customer accounts" tab. 
See also: [Customer accounts](../customer-accounts.md) 

![](../assets/screens/products/seasontickets_orgsettings1.png "Season tickets organizer settings 1")

After doing so, a new menu item "Customer accounts" will also show up in the main menu of your organizer account on the left. 
Open its menu and click "Membership types". 
Then, select to "create a new membership type".

You can name the membership type in a way that clearly explains where it is valid, e.g. "season pass main location" or "season pass all locations". 
There are a few details you can configure on this page, such as whether the season pass can be used by multiple different persons, or if the season pass can be used for multiple tickets for the same time slot. 
You can also define a maximum number of usages, which is useful if you e.g. use this feature to add a "ticket of ten".

![](../assets/screens/products/seasontickets_membershiptype1.png "Season tickets membership type 1")

Next, you need a way of selling these season passes. 
Theoretically this can be done through the same event series that you usually use, but it's probably cleaner and easier to find for customers if you create a new event that you only use to sell season passes. 
The start and end date of the new event should correspond to the dates of your season.

Inside the new event, you only need to create a single product which you can call "season ticket". 
Inside that product's settings, head to the "Additional settings" section and look for the option "This product creates a membership of type". 
Select the membership type you just created. 
By default, the checkbox "The duration of the membership is the same as the duration of the event or event series date" is active, which is fine for our season ticket example, but you might need to unset it and provide custom timing for other ticket types such as week passes.

![](../assets/screens/products/seasontickets_issue1.png "Season tickets issue 1")

To prevent confusion, it might be useful to turn off ticket downloading at "Settings" → "Tickets" for your new event. 
That's it, you are now ready to sell season tickets!

We can now deal with how to use the season tickets. 
Move back to your existing event and create a new product or product variation of your regular product which you call "ticket for season ticket holders" and assign a price of zero. 
In the "Availability" section of the product or variation settings, check the option "Require a valid membership" and again select the membership type you created. 
You can of course repeat this with all events the season ticket holder should have access to.

![](../assets/screens/products/seasontickets_require1.png "Season tickets require 1")

#### Option B: All-access in a single pass

If you have only a single event series with many time slots and you do not care how many season ticket holders show up, there's a solution that does not require your customers to set up accounts and book a new ticket on every visit.

Instead, you can just create an additional product "Season ticket" that you enable either in a "special" date of your event series just created for this purpose, or in all of your dates so it can be easily found by customers.

Then, you can set up your check-in lists with custom logic in the "Advanced" tab of your check-in list settings. 
The logic needs to ensure the following requirements:

 - Regular ticket holders can only get in during their assigned time frame and when they haven't used their ticket before.
 - Season ticket holders can always get in.

Here's an example on how to set this up:
Create an OR-bracket (At least one of the conditions below). 
Within that OR-condition, create two AND-brackets (All of the conditions below). 
Within the first AND-bracket, create the following conditions: 

 - "Product" "is one of" "Day pass" 
 - "Current date and time" "is after" "Event start" with a tolerance of 0 
 - "Current date and time" "is before" "Event end" with a tolerance of 0 
 - "Number of previous entries" equals 0 

Then, within the second AND-bracket, create the following condition: 
"Product" "is one of" "Season pass".  

![Custom check-in rule page set up according to the instructions above.](../assets/screens/products/seasontickets_rules1.png "Season tickets rules 1")

### Mixed taxation 

{% include "warning-tax.md" %}

For general information on how to set up taxation in pretix, refer to our article on [taxes](../taxes.md). 

Let's say you are a charitable organization in Germany and are allowed to charge a reduced tax rate of 7% for your educational event. 
However, your event includes a significant amount of food, you might need to charge a 19% tax rate on that portion. 
For example, your desired tax structure might then look like this:

 - Conference ticket price: € 450 (incl. € 150 for food)

  - incl. € 19.63 VAT at 7%

  - incl. € 23.95 VAT at 19%

You can implement this in pretix using product bundles. 
In order to do so, you should create the following two products:

 - Conference ticket at € 450 with a 7% tax rule

 - Conference food at € 150 with a 19% tax rule and the option “Only sell this product as part of a bundle" set

In addition to your normal conference quota, you need to create an unlimited quota for the food product.

Then, head to the Bundled products tab of the “conference ticket" and add the “conference food" as a bundled product with a designated price of € 150.

Once a customer tries to buy the € 450 conference ticket, a sub-product will be added and the price will automatically be split into the two components, leading to a correct computation of taxes.

## Troubleshooting 

### A product does not appear in the ticket shop 

If you have created a product and it is not displayed in your ticket shop, perform the following checks: 

 1. Check if the product's "active" checkbox is enabled.

 2. Check if the product's "Available from" or "Available until" settings restrict it to a date range.

 3. Check if the product's checkbox "This product will only be shown if a voucher matching the product is redeemed." is enabled. 
 If this is the case, the product will  only be shown if the customer redeems a voucher that directly matches to this product. 
 It will not be shown if the voucher only is configured to match a quota that contains the product.

 4. Check if the product is in a category that has the "Products in this category are add-on products" checkbox enabled. 
 If this is the case, the product won't show up on the shop front page, but only in the first step of checkout when a product in the cart allows to add add-on products from this category.

 5. Check that a quota exists that contains this product. 
 If your product has variations, check that at least one variation is contained in a quota. 
 If your event is an event series, make sure that the product is contained in a quota that is assigned to the series date that you access the shop for.

 6. If the sale period has not started yet or is already over, check the "Show items outside presale period" setting of your event.