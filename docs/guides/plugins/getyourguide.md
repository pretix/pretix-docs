# GetYourGuide

You can use third-party aggregators such als GetYourGuide to sell tickets not only through your own own ticket shop, but also through the aggregator's website. 
Using GetYourGuide entails costs, but it allows you to reach a larger audience that would otherwise not have found their way to your shop. 
pretix offers an integration with GetYourGuide that allows you to profit from an additional sales and revenue channel, while keeping the effort for setting up and maintaining multiple ticket shops at a minimum. 
This article is going to tell you how to do that. 

## Prerequisites

If you want to use the GetYourGuide integration for pretix, then you need to have access to an active GetYourGuide supplier account. 
The GetYourGuide integration is handled on the event level, so you have to create an event first. 

## How to 

Setting up the GetYourGuide integration involves the following steps: 

 1. Ask pretix support to unlock the GetYourGuide plugin on your account. 
 2. Create a sales channel
 3. Enable the plugin 
 4. Configure products

### Setting up your organizer account for GetYourGuide

The following actions need to be taken once for every organizer account that you want to integrate with GetYourGuide. 

The pretix integration with GetYourGuide is currently in beta. 
The pretix team has to activate it once for your organizer account before you can use it. 
Contact support via [email](support@pretix.eu) or [phone](tel:+4962213217750) and ask them to activate the GetYourGuide plugin. 

Before you can use GetYourGuide for any of your events, you need to create a corresponding sales channel on your organizer account. 
pretix will use the sales channel to properly attribute sales via GetYourGuide. 
Navigate to :navpath:Your organizer → :fa3-wrench: Settings → Sales channels:. 
Click the :btn-icon:fa3-plus: Add a new channel: button. 
On the page titled "Add sales channel", select :btn:GetYourGuide:. 
Click the :btn:Save: button. 

### Setting up your event for GetYourGuide

The following actions need to be taken once for every event account that you want to sell via GetYourGuide. 

In order to enable the GetYourGuide plugin, navigate to :navpath:Your event → :fa3-wrench: Settings → Plugins: and open the :btn:Integrations: tab. 
Seek out the plugin labeled "GetYourGuide" in the list and click the :btn:Enable: button next to it. 
Repeat this step for every event that you want to offer via GetYourGuide. 

In order to sell your event via the GetYourGuide sales channel, navigate to :navpath:Your Event → :fa3-wrench: Settings → General:. 
Under "Sales channels", check the box next to "GetYourGuide" or the box next to "Sell on all sales channels". 

### Setting up tickets for GetYourGuide 

Configure at least one product to be sold via GetYourGuide. 
In order to do so, navigate to :navpath:Your Event → :fa3-ticket: Products: and create or edit a product. 
Switch to the :btn:Availability: tab and under "Sales channels", check the box next to "GetYourGuide" or the box next to "Sell on all sales channels". 

Then, switch to the :btn:Additional settings: tab and set the GetYourGuide equivalent ticket category. 
There can only be one product per GetYourGuide ticket category for each one of your events. 
Depending on your configuration, you have to add at least one product to be in the "Adult" or "Group" GetYourGuide ticket category.

GetYourGuide relies on pretix product categories for ticket pricing. 
For each one of your pretix events, you can only either sell individual tickets or group tickets via GetYourGuide—not both. 
If you want to sell individual tickets, then you will have to offer at least one ticket of the GetYourGuide ticket category "Adult". 
In addition to that, you can also offer tickets of an of the other GetYourGuide ticket categories ("Child", "Youth", "Senior", etc.). 
Customers will have to buy one ticket for every attendee. 

If you want to sell group tickets, then you have to offer at least one product of the GetYourGuide ticket category "Group". 
If you are offering group tickets, then it is not possible to offer any other GetYourGuide ticket categories (single tickets). 
Customers will only have to purchase one ticket for their whole group of attendees. 
You can limit the configure the size limit of the group for every ticket. 

Just like with any other product, you also have to add the tickets you intend to sell via GetYourGuide to a quota in pretix before they become available in your shop. 
If you want to learn more on how to handle categories in pretix, refer to the section on [categories](../products.md#creating-and-editing-categories). 

You cannot offer more than one quantity for individual ticket categories sold through GetYourGuide.
GetYourGuide will always default to the smallest applying quota, except if that quota is exhausted and another one is available. 
pretix will only report the available number of tickets for the lowest applying quota.
Thus, you should add all products that you are selling through GetYourGuide to the same quota. 

### Configuring the GetYourGuide plugin

In order to configure the GetYourGuide integration, navigate to :navpath:Your Event → :fa3-wrench: Settings → GetYourGuide: and open the :btn:Configuration: tab. 
Supply the required information and click the :btn:Save: button. 
If you want to use the analyzer feature of the GetYourGuide plugin, open the :btn:Analyzer: tab and set it up. 

The GetYourGuide backend refers to your pretix event as a "product". 
Open the GetYourGuide [Supplier Portal](https://suppliers.getyourguide.com/) and connect it with your pretix shop. 
In order to do so, follow the instructions for [Connecting a new product to your Reservation System](https://supply.getyourguide.support/hc/en-us/articles/18008029689373-Connecting-a-new-product-to-your-Reservation-system) in the GetYourGuide Supply Partner Help Center.
Select "pretix.eu" as your "reservation system". 
You can find the required "product ID" by navigating to :navpath:Your Event → :fa3-wrench: Settings → GetYourGuide: and opening the :btn:Configuration: tab. .

From this point on, GetYourGuide will automatically import products along with their availability status and offer them for sale. 