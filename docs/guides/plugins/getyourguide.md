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
 2. Creating a sales channel
 3. Enabling the plugin 


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

In order to sell your event via the GetYourGuide sales channel, navigate to :navpath:Your Event  → :fa3-wrench: Settings → General:.  
Check either the box next to "Sell on all sales channels" or the box next to "GetYourGuide". 

 3. Configure one or more products to be sold on GetYourGuide

    Either create a new or edit an existing product that you would like to sell on GetYourGuide. 
    To do so, navigate to :navpath:Your Event → :fa3-ticket: Products: and select the product in question. 
    Switch to the :btn:Availability: tab and either check the box next to "Sell on all sales channels" or at least one of the boxes next to "Restrict to specific sales channels". 
    Then, switch to the :btn:Additional settings: tab and set the GetYourGuide equivalent ticket category. 
    Within your event, there can be only one product per ticket category. 
    Depending on your further configuration, you must at least select one product to be in the "Adult" or "Group" category.

 4. Configuring the GetYourGuide plugin

    Once you have configured one or more products to be eligible to be sold on GetYourGuide, you'll need to configure a few basic settings within the event. 
    Navigate to :navpath:Your Event → :fa3-wrench: Settings → GetYourGuide: and open the :btn:Configuration: tab. 
    The most important settings, such as the location of the event on sale, can be found here. 

## Ticket Categories

While pretix only uses the ticket category term loosely to group together multiple products for nicer display, GetYourGuide is relying on the ticket categories to price the tickets.

First of all, you need to make the decision on how you are planning on selling your tickets on GetYourGuide - in most cases, this will reflect your current sales strategy within your pretix shop.

 - Individual tickets
   Every single person attending will need to purchase their own ticket. 
   A family of two adults and two children will have to purchase and pay for a total of 4 tickets. 
   In this case, you will need to offer *at least* a ticket of the "Adult" type, but may offer any other ticket category type (Child, Youth, Senior, ...) in addition. 
   But you cannot offer a "Group" ticket.

 - Group tickets

   Two groups, consisting of 10 and 20 participants respectively, won't need to purchase a total of 30 tickets, but rather two group tickets. 
   It is up to you to configure the group size limits within the GetYourGuide-settings of your product. 
   Choosing this option, you cannot offer any other ticket categories besides "Group".

## Setting up event dates and quotas

Of course, in addition to creating products, you will also need to add them to a quota for them to be available for sale. 
The process for doing this is the very same as for any regular event or event series.
If you want to learn more on how to handle taxes in pretix, refer to our guide on [products](../products.md). 

!!! Note 
    When selling individual tickets through GetYourGuide, you will not be able to offer differing quantities for individual ticket categories.
    GetYourGuide will always default to the smallest relevant quota, except if that quota is exhausted and another one is available. 

For this reason, we recommend placing all GetYourGuide-eligible products into the same quota. 
Should you however opt to create multiple quotas which create an imbalance, pretix will report only the available number of tickets for the lowest relevant quota.

## Connecting your event to GetYourGuide

Once you have set up your event and products and performed all necessary configuration, you may want to use the Analyzer feature of the GetYourGuide plugin. 
If you want to do so, navigate to :navpath:Your Event → :fa3-wrench: Settings → GetYourGuide: and open the :btn:Analyzer: tab. 

The Analyzer should not display any blocking error messages and at least one event date that is ready for publishing on the GetYourGuide platform.

At this point, you will need to setup your event (called "product" in the GetYourGuide universe) on their [Supplier Portal](https://suppliers.getyourguide.com/) and connect it with your pretix shop. 
To do so, please follow the instructions for [Connecting a new product to your Reservation System](https://supply.getyourguide.support/hc/en-us/articles/18008029689373-Connecting-a-new-product-to-your-Reservation-system) on the GetYourGuide Supply Partner Help Center.

Select "pretix.eu" as your reservation system; the required "product ID" can be found in the "Configuration" tab of the GetYourGuide plugin settings page.

From this point on, GetYourGuide will automatically import the availabilities and products and offer them for sale.