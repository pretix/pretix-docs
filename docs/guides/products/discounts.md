# Discounts 

pretix has several different methods for offering your customers discounts on their purchase under certain conditions. 
This article explains several different types of discounts as well as common use cases: 
 - [different price levels](discounts.md#different-price-levels) 
 - [early bird prices](discounts.md#early-bird-tickets)
 - [discount packages](discounts.md#discount-packages)
 - [group discounts](discounts.md#group-discounts-and-discounts-for-large-orders). 

## Prerequisites 

Most of the methods described here are handled on the event level, so you have to create an event first. 
This article assumes some general knowledge on how to create and edit products, so it makes sense to take a look at the guide on [products](index.md) first. 

## How To 

pretix allows you to create as many different products with different price levels as you need. 
This approach is explained under the section [different price levels](discounts.md#different-price-levels). 
The sections after that will guide you through some more advanced methods for offering discounts based on certain conditions, such as [early bird prices](discounts.md#early-bird-tickets), [discount packages](discounts.md#discount-packages), and [group discounts](discounts.md#group-discounts-and-discounts-for-large-orders). 

### Different price levels

The most straightforward way to offer a discount is to create two or more admission products with different price levels. 
This makes sense if, for example, you are selling discount tickets for pensioners or students. 
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
pretix will subtract from both quotas whenever a discount ticket is sold, and subtract from the general quota only when a regular ticket is sold. 

### Group discounts and discounts for large orders

pretix gives you several methods for offering discounts on large orders regardless of which products are purchased. 
This can also be useful for offering group discounts. 
You can offer cheaper tickets tied to a minimum order amount; set up a rule for discounts that is applied automatically if a purchase meets certain conditions; or offer fixed group packages at reduced prices. 
The following subsections will explain each method. 

#### Minimum order amount

You can use the minimum order amount feature to promote discounted group tickets. 
In order to do so, create a single-person ticket at a reduced price. 
Use the "Minimum amount per order" option to define the minimal group size for which you want to grant the discount. 

For illustrative purposes, assume that your basic admission ticket is priced at €20.00. 
Clone that ticket, give it a name such as "Reduced ticket for groups of five or more", and set the price to €15.00. 
Save the ticket and edit it. 
Switch to the :btn:Availability: tab and set the "Minimum amount per order" to 5. 
This way, customers can purchase 5 or more of the tickets at the discounted price. 

#### Automatic discounts

You can use pretix to automatically grant a discount on an order if a certain condition is met, such as a certain group size. 

To set this up, navigate to :navpath:Your event → :fa3-ticket: Products → Discounts: and click the :btn-icon:fa3-plus: Create a new discount: button. 
Choose an "Internal name" for the discount. 
For a percentage discount such as "25 percent off if you buy 5 tickets", set the "Minimum number of matching products" to 5 and the "Percentual discount on matching products" to 25.00. 

For a discount such as “buy 5, get one free", set the "Minimum number of matching products" to 5, "Percentual discount on matching products" to 100.00, and "Apply discount only to this number of matching products" to 1. 

#### Fixed group packages

You can use bundles to sell group tickets for fixed numbers, for example a table of eight at your gala dinner. 

First, create a basic admission ticket for a single person and a corresponding quota. 
Then, create a non-admission product with a price lower than the full price for eight individual tickets. 
Open the :btn:Bundled products: tab of that product and click the :btn-icon:fa3-plus: Add a new bundled product: button. 
Choose your basic admission ticket as the "Bundled product", set "Quantity" to 8 and click the :btn:Save: button. 

Create a quota that includes only the eight person bundle. 
This quota can have an unlimited capacity. 

This configuration means that whenever one of the bundles is purchased, pretix creates eight individual tickets. 
This results in the proper number being subtracted from the basic product quota and eight new entries for attendees on your check-in list. 
If you need each individual attendee's personal data, navigate to :navpath:Your Event → :fa3-wrench: Settings → General:, open the :btn:Customer and attendee data: tab and edit the settings under "Attendee data (once per personalized ticket)". 


### Early bird tickets

This section explains how to offer early bird tickets that can only be bought far in advance of the event and which become unavailable in favor of more expensive tickets at some point. 
It is possible to create a ticket and manually increase the price as the event approaches. 

But pretix also offers two methods for automating this: 
You can offer different pricing tiers based on date, or based on the number of tickets that are still available. 
Regardless of which method you use, the first step is creating one admission ticket for each price tier. 

#### Early bird tickets based on time for singular events

If you want to offer early bird tickets based on the current time for a singular event, edit one of the products and switch to the :btn:Availability: tab. 
Use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased. 
Repeat this step for each product. 

Make sure that the "Available until" option for the first ticket has the same date and time as the "Available from" option for the following ticket. 
This is to ensure that there is no overlap during which more than one pricing tier is available, and no gap during which no tickets are available. 

#### Early bird tickets based on time for dates within an event series

The method described above does not work for an event series with dates repeating over a large span of time. 
If you want to offer early bird tickets based on the time for a date within an event series, navigate to :navpath:Your event series → :fa3-calendar: Dates: and edit one of the dates. 
Under "Product settings", use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased for this individual date. 

If you want to set the same availability for multiple dates, navigate to :navpath:Your event series → :fa3-calendar: Dates:, check the box next to each date you want to edit and click the :btn-icon:fa3-edit: Edit selected: button. 
Under "Item prices", use the "Available from" and "Available until" fields to define the period of time in which the product can be purchased for the selected dates. 
Check the boxes labeled "change" next to "Available from" and "Available until" to ensure that the product settings are overridden. 

#### Early bird tickets based on ticket numbers 

If you want to offer early bird tickets based on the number of tickets already sold for a singular event, create one quota for each price level. 
For all price tiers except the last one, enter a limited number in the "Total capacity" field and check the box next to "Close this quota permanently once it is sold out". 
This means that once one price tier is sold out, the shop will **not** move back to a previous price tier even if orders are canceled and spots in the quota open up. 
You do **not** need to enable the "Close this quota permanently once it is sold out" option for the last quota for this approach. 

If you are planning to sell only a limited amount of tickets, for instance due to space constraints at your venue, limit the "Total capacity" of the last quota. 
The sum of the "Total capacity" of all quotas combined should not exceed the total number of tickets you are planning to sell. 

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
First of all, create three products with different prices:

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

This section explains how to offer combinations of several products at lower prices than the sum of the prices of each individual product. 
This is useful whenever you are offering several products, expect customers to purchase different combinations of those products, and want to offer lower prices for larger combinations. 
You can apply this, for example, to any of the following use cases: 

 - a trade fair or festival opening on three consecutive days with different pricing for single-day, two-day, and three-day passes
 - different levels of merch packages with larger packages offered at reduced rates 
 - different offers such as in-person workshops, online content, and a networking event, which are offered at a cheaper price if purchased in combination 

There are two methods of implementing this in pretix: 
One method uses [combination products](discounts.md#option-a-combination-products). 
It has the advantage of keeping your products and possible orders fairly straightforward. 
However, this method is only feasible if there are no more than three or four basic products. 

The other method uses [add-ons and bundles](discounts.md#option-b-add-ons-and-bundles). 
This option starts out relatively complex, but the complexity does not grow exponentially with an increasing number of basic products, as it does in the first method. 

Generally speaking, the first option makes more sense if you have a small number of basic products, and the second option makes more sense if that number is larger than four or five. 
Both methods will be explained in the following subsections. 

If you want to offer a discount for large orders regardless of which products are purchased, refer to the section on [group discounts and discounts for large orders](discounts.md#group-discounts-and-discounts-for-large-orders) instead. 

#### Option A: Combination products

One option is to create the basic products and quotas, and to then create separate products for all possible combinations of basic products. 
This has the advantage of keeping your products and possible orders fairly straightforward. 
It can be implemented without touching the add-ons or bundles features. 

However, this method is only feasible if the total number of possible combinations is rather small. 
The number of products you need to offer in your shop is `2ⁿ-1`, where `n` is the number of basic products. 
This number grows exponentially with every additional basic product. 
If you have three basic products, it results in seven products having to be offered in your shop. 
If you have four basic products, it results in fifteen products. 
For this level of complexity and beyond, the [method using bundles](discounts.md#option-b-add-ons-and-bundles) described below may be more suitable. 

For illustrative purposes, assume you are hosting a three-day trade fair. 
Create a basic ticket for each day of the trade fair, three combination tickets for two days, and one combination ticket for all three days: 

 - Day 1 ticket
 - Day 2 ticket
 - Day 3 ticket
 - Day 1 + day 2 ticket  
 - Day 1 + day 3 ticket 
 - Day 2 + day 3 ticket
 - Ticket for all three days

Then, create three quotas, each one with a total capacity equal to your venue's maximum capacity on any given day:

 - Day 1 quota, linked to "Day 1 ticket", "Day 1 + day 2 ticket", "Day 1 + day 3 ticket", and "Ticket for all three days"
 - Day 2 quota, linked to "Day 2 ticket", "Day 1 + day 2 ticket", "Day 1 + day 2 ticket", and "Ticket for all three days"
 - Day 3 quota, linked to "Day 3 ticket", "Day 1 + day 3 ticket", "Day 2 + day 3 ticket", and "Ticket for all three days"

This way, every attendee can order exactly one ticket that they can use for all days that they are going to attend. 
Finally, navigate to :navpath:Your event → :fa3-check-square-o: Check-in:, edit your check-in list and switch to the :btn:Advanced: tab. 
Define custom check-in rules so that the tickets in the first quota are valid on the first day of the event; the tickets in the second quota are valid on the second day; and the tickets in the third quota are valid on the third day. 

You can do this either using the "Current day of the week" or the "Current date and time" condition. 
The check-in rule could look similar to the one in the screenshot below. 
The logic looks like this: 

At least one of the conditions below (OR)

 - All of the conditions below (AND)
    - Product is one of "Day 1 ticket", "Day 1 + day 2 ticket", "Day 1 + day 3 ticket", or "Ticket for all three days"
    - Current day of the week = 1 (Monday)
 - All of the conditions below (AND)
    - Product is one of "Day 2 ticket", "Day 1 + day 2 ticket", "Day 1 + day 2 ticket", or "Ticket for all three days"
    - Current day of the week = 2 (Tuesday)
 - All of the conditions below (AND)
    - Product is one of "Day 3 ticket", "Day 1 + day 3 ticket", "Day 2 + day 3 ticket", or "Ticket for all three days"
    - Current day of the week = 3 (Wednesday)

![Custom check-in rule with three sets of AND-conditions. The first one demands that the product is one of the products for day one AND that the current day of the week is Monday. The second and third set do the same thing, but for day 2 and Tuesday as well as day 3 and Wednesday respectively. The three sets of AND-conditions are all included in one OR-condition.](../../assets/screens/products/check-in-rules-combination-products.png "Custom check-in rule") 

#### Option B: Add-ons and bundles

Another option is to create the basic products and quotas, and to then create products with mandatory add-ons for all possible combinations. 
An exception can be made for the combination product containing **all** basic products. 
The full combination product can either be set up as described above in the section [Option A: Combination products](discounts.md#option-a-combination-products), or as a bundle. 
The approach using the bundle will also be described in this section. 

This option has the advantage that the number of products needed does not grow exponentially with the number of basic products. 
The main disadvantage is that orders become more complex because every order containing a product with mandatory add-ons will contain at least three products. 

For illustrative purposes, assume you are hosting a three-day trade fair. 
First, create a category for "Day tickets". 
Then, create a basic admission ticket for each day of the trade fair, one non-admission product for any two days, and one non-admission product for all three days: 

 - Day 1 ticket
 - Day 2 ticket
 - Day 3 ticket
 - Ticket for two days
 - Ticket for all three days

Add the tickets for day 1, 2 and 3 to the "Day tickets" category. 
Do **not** add any other tickets to that category. 
Then, create one quota for each of the admission tickets. 
When creating the quotas for each single day ticket, set the "Total capacity" to a number equal to the capacity of your venue for each day. 
The quotas for the two-day and three-day ticket can be unlimited. 

Edit the "Ticket for two days", switch to the :btn:Add-on: tab and click the :btn-icon:fa3-plus: Add a new add-on: button. 
Select the category "Day tickets", set the minimum and maximum number to 2 and check the box next to "Add-ons are included in the price". 
Click the :btn:Save: button. 
With this configuration, a customer purchasing the "Ticket for two days" will be prompted to add two tickets from the "Day tickets" category to their purchase as add-ons. 
The customer will receive two tickets: one for each day of the event that they selected. 

It does not make sense to set up the "Ticket for all three days" the same way because then the customer would have to select all three day tickets manually. 
If you want to set up the "Ticket for all three days" as a bundle, edit it and open the :btn:Bundled products: tab. 
Click the :btn-icon:fa3-plus: Add a new bundled product: button. 
For the "Bundled product, choose the "Day 1 ticket". 
Leave the "Quantity" at 1 and the "Designated price part" at 0.00. 
Repeat the same process for "Day 2 ticket" and "Day 3 ticket". 

This configuration means that when a customer purchases the "Ticket for all three days", the three day tickets will be added to their cart automatically for free. 
The customer will receive three tickets: one for each day of the event. 

Finally, navigate to :navpath:Your event → :fa3-check-square-o: Check-in:, edit your check-in list and switch to the :btn:Advanced: tab. 
Define custom check-in rules so that the "Day 1 ticket" is only valid on the first day of the event; the "Day 2 ticket" is only valid on the second day; and the "Day 3 ticket" is only valid on the third day. 
If you have set up the "Ticket for all three days" as a combination product, define the rule so that it is also valid on each day. 
You can do this either using the "Current day of the week" or the "Current date and time" condition. 
The logic looks like this: 

At least one of the conditions below (OR)

 - All of the conditions below (AND)
    - Product is one of "Day 1 ticket" or "Ticket for all three days"
    - Current day of the week = 1 (Monday)
 - All of the conditions below (AND)
    - Product is one of "Day 2 ticket" or "Ticket for all three days"
    - Current day of the week = 2 (Tuesday)
 - All of the conditions below (AND)
    - Product is one of "Day 3 ticket"
    - Current day of the week = 3 (Wednesday)

!!! Note 
    You can also set up the "Ticket for all three days" as described in the section [Option A: Combination products](discounts.md#option-a-combination-products). 
    If you decide to do so, also include this ticket in each condition starting with "Product is one of". 
