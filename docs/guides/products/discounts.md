# Discounts 

pretix has several different ways for offering your customers discounts on their purchase under certain conditions. 
This article explains several use cases for different types of discounts. 

## Prerequisites 

Most of the methods described here are handled on the event level, so you have to create an event first. 
The article assumes some general knowledge on how to create and edit products, so it makes sense to take a look at the [guide on products](index.md) first. 

## How To 

The most straightforward way to offer a discount is to create two or more admission products with different price levels. 
This makes sense if, for example, if you are selling discount tickets for pensioners or students. 
In order to do so, first create the basic admission ticket and configure it according to your requirements. 

Then, clone the ticket once for each differing price level. 
Adjust the name and the price of each cloned ticket. 
In the "Description" field, add an informative text along the following lines: 
"This ticket is only valid if you provide a student ID during check-in."
Switch to the :btn:Check-in & Validity: tab and add a "Check-in text" with instructions for the person scanning the ticket, for example: 
"Check for student ID". 

Add all products to one general quota. 
Set the capacity of the quota to the maximum number of tickets you want to sell. 

If you want to place an additional limit on the number of discount tickets available, create another quota and set the capacity to the maximum number of discount tickets you want to sell. 
Add only the discount tickets to this quota. 
pretix will subtract from both quotas whenever a discount ticket is sold, and only subtract from the general quota when a regular ticket is sold. 

The following sections will guide you through some more advanced methods for offering discounts based on certain conditions. 

### Early bird tickets

This section explains how to offer early bird tickets that can only be bought far in advance of the event and which get replaced with more expensive tickets at some point. 
It is possible to create a ticket and manually increase the price as the event approaches. 

But pretix also offers two methods for automating this: 
You can offer different pricing tiers based on date, or based on the number of tickets that are still available. 
Regardless of which method you use, the first step is creating one admission ticket for each price tier. 

If you want to offer early bird tickets based on dates for a singular event, edit one of the products and switch to the :btn:Availability: tab. 
Use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased. 
Repeat this step for each product. 

Make sure that the "Available until" option for the first ticket has the same date and time as the "Available from" option for the following ticket. 
This is to ensure that there is no overlap during which more than one pricing tier is available, and no gap during which no tickets are available. 

The method described above does not work for an event series with dates repeating over a large span of time. 
If you want to offer early bird tickets based on dates for a singular event, navigate to :navpath:Your event series → :fa3-calendar: Dates: and edit one of the dates. 
Under "Product settings", use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased for this individual date. 

If you want to set the same availability for multiple dates, navigate to :navpath:Your event series → :fa3-calendar: Dates:, check the box next to each date you want to edit and click the :btn-icon:fa3-edit: Edit selected: button. 
Under "Item prices", use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased for the selected dates. 
Check the boxes labeled "change" next to "Available from" and "Available until" to ensure that the product settings are overridden. 

If you want to offer early bird tickets based on ticket numbers for a singular event, create one quota for each price level. 
For all price tiers except the last one, enter a limited number in the "Total capacity" field and check the box next to "Close this quota permanently once it is sold out". 
This means that once one price tier is sold out, the shop will **not** move back to a previous price tier even if orders are canceled and spots in the quota open up. 
Whether you need to enable these options for the last quota as well depends on your individual use case.

Add only the first product to the first quota. 
Add the first **and** second product to the second quota and set the "Total capacity" so that it includes the capacity of the first quota plus the amount of the second ticket that you want to sell. 
Continue like this until you arrive at the last quota, which should contain all relevant products. 
This quota setup ensures that you can still sell the maximum number of tickets for your event, even if orders for tickets in the earlier quotas are canceled. 

Navigate to :navpath:Event → :fa3-ticket: Products → Products: and edit the second product in the sequence. 
Switch to the :btn:Availability: tab. 
Under "Only show after sellout of", select the first quota. 
Repeat this process for each following product, always selecting the previous quota. 
This means that each price tier is only displayed in the shop after the previous price tier is sold out (the quota is empty). 

If you want to hide the prices for the previous tickets, navigate to :navpath:Your event → :fa3-wrench: Settings → General: and switch to the :btn:Display: tab. 
Under "Product list", check the box next to "Hide all products that are sold out". 

!!! Note 
    There are some rare cases in which prices in your shop may switch back and forth between price tiers. 
    If a customer places the last products of one price tier in their cart but does not buy them yet, these tickets will be marked as "Reserved" and the next price tier will be displayed. 
    If the customer does not actually place the order, the previously reserved tickets will be displayed in the shop again and the tickets of the following price tier will disappear. 

    This behavior is preferable to a situation in which a malicious user would be able to reserve all tickets of a cheaper tier without buying them. 

For illustrative purposes, assume you intend to sell 400 tickets in three price tiers. 
First of all, create three products:

 - "Super early bird ticket"
 - "Early bird ticket"
 - "Regular ticket"

Then, create three quotas:

 - "Super early bird" with a total capacity of 100 and the "Super early bird ticket" product selected. 
 - "Early bird and lower" with a total capacity of 200 and both the "Super early bird ticket" and the "Early bird ticket" products selected. 
 - "All participants" with a total capacity of 400, all three products selected and no additional options.

Next, modify the product "Regular ticket" and switch to the :btn:Availability: tab.
Under "Only show after sellout of", select your quota "Early bird and lower". 
Do the same for the "Early bird ticket" with the quota "Super early bird ticket".

### Discount packages 

Imagine you run a trade show that opens on three consecutive days and you want to have the following pricing:

 - Single day: € 10
 - Any two days: € 17
 - All three days: € 25

In this case, there are multiple different ways you could set this up with pretix.

#### Option A: Combination products

With this option, you just set up all the different combinations someone could by as a separate product. 
In this case, you would need 7 products:

 - Day 1 pass
 - Day 2 pass
 - Day 3 pass
 - Day 1+2 pass
 - Day 2+3 pass
 - Day 1+3 pass
  - All-day pass

Then, you create three quotas, each one with the maximum capacity of your venue on any given day:

 - Day 1 quota, linked to "Day 1 pass", "Day 1+2 pass", "Day 1+3 pass", and "All-day pass"
 - Day 2 quota, linked to "Day 2 pass", "Day 1+2 pass", "Day 2+3 pass", and "All-day pass"
 - Day 3 quota, linked to "Day 3 pass", "Day 2+3 pass", "Day 1+3 pass", and "All-day pass"

This way, every person gets exactly one ticket that they can use for all days that they attend. 
You can later set up check-in lists appropriately to make sure only tickets valid for a certain day can be scanned on that day.

The benefit of this option is that your product structure and order structure stays very simple. 
However, the two-day packages scale badly when you need many products.

We recommend this setup for most setups in which the number of possible combinations does not exceed the number of parts (here: number of days) by much.

#### Option B: Add-ons and bundles

We can combine the two features "product add-ons" and "product bundles" to set this up in a different way. 
Here, you would create the following five products:

 - Day 1 pass in a category called "Day passes"
 - Day 2 pass in a category called "Day passes"
 - Day 3 pass in a category called "Day passes"
 - Two-day pass
 - All-day pass

This time, you will need five quotas:
 - Day 1 quota, linked to "Day 1 pass"
 - Day 2 quota, linked to "Day 2 pass"
 - Day 3 quota, linked to "Day 3 pass"
 - Two-day pass quota, linked to "Two-day pass" (can be unlimited)
 - All-day pass quota, linked to "All-day pass" (can be unlimited)

Then, you open the "Add-On" tab in the settings of the Two-day pass product and create a new add-on configuration specifying the following options:

 - Category: "Day passes"
 - Minimum number: 2
 - Maximum number: 2
 - Add-Ons are included in the price: Yes

This way, when buying a two-day pass, the user will be able to select exactly two days for free, which will then be added to the cart. 
Depending on your specific configuration, the user will now receive two separate tickets, one for each day.

For the all-day pass, you open the "Bundled products" tab in the settings of the All-day pass product and add three new bundled items with the following options:

 - Bundled product: "Day 1/2/3"
 - Bundled variation: None
 - Count: 1
 - Designated price: 0

This way, when buying an all-day pass, three free day passes will automatically be added to the cart. 
Depending on your specific configuration, the user will now receive three separate tickets, one for each day.

This approach makes your order data more complicated, since e.g. someone who buys an all-day pass now technically bought four products. 
However, this option allows for more flexibility when you have lots of options to choose from.

!!! Tip

    Depending on the packages you offer, you might not need both the add-on and the bundle feature, i.e. you only need the add-on feature for the two-day pass and only the bundle feature for the all-day pass. 
    You could also set up the two-day pass like we showed here, but the all-day pass like in option A!

### Group discounts 

This section explains how to give discounts for whole groups attending your event.

#### Automatic discounts

pretix can automatically grant discounts if a certain condition is met, such as a specific group size. 

To set this up, navigate to :navpath:Your event → :fa3-ticket: Products → Discounts: and click the :btn-icon:fa3-plus: Create a new discount: button. 
You can choose a descriptive name such as "Discount for school classes" so you can find this again later. 
You can also optionally restrict the discount to a specific time frame or a specific sales channel.

Next, either select Apply to all products or create a selection of products that are eligible for the discount.

For a percentual group discount similar to “if you buy at least 5 tickets, you get 20 percent off", set Minimum number of matching products to “5" and Percentual discount on matching products to “20.00".

For a buy-X-get-Y discount, e.g. “if you buy 5 tickets, you get one free", set Minimum number of matching products to “5", Percentual discount on matching products to “100.00", and Apply discount only to this number of matching products to “1".

#### Fixed group packages

If you want to sell group tickets in fixed sizes, e.g. a table of eight at your gala dinner, you can use product bundles. 
Assuming you already set up a ticket for admission of individual persons, you then set up a second product Table (8 persons) with a discounted full price. 
Then, head to the Bundled products tab of that product and add one bundle configuration to include the single admission product eight times. 
Next, create an unlimited quota mapped to the new product.

This way, the purchase of a table will automatically create eight tickets, leading to a correct calculation of your total quota and, as expected, eight persons on your check-in list. 
You can even ask for the individual names of the persons during checkout.

#### Minimum order amount

If you want to promote discounted group tickets in your price list, you can also do so by creating a special Group ticket at the reduced per-person price and set the Minimum amount per order option of the ticket to the minimal group size.

For more complex use cases, you can also use add-on products that can be chosen multiple times.

This way, your ticket can be bought an arbitrary number of times – but no less than the given minimal amount per order.
