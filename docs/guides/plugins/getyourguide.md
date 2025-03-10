# GetYourGuide

!!! Note 
    The GetYourGuide integration is currently in beta. 
    Please contact <support@pretix.eu> to enable the integration for your pretix.eu organizer account.

## Introduction

Using third party aggregators, such als GetYourGuide, event organizers can sell tickets to their events not only on their own ticket shop but also on the aggregator's portal. 
While this service is not for free, it allows event organizers to reach a larger audience that would otherwise not have found their way into the organizer's webshop.

Using pretix' integration with GetYourGuide, event organizers can profit from an additional sales and revenue channel, while keeping the effort for setting up and maintaining multiple ticket shops to a minimum.

## Preparing your organizer account

The first step in enabling the GetYourGuide integration is to setup a corresponding Sales Channel, which will be used to properly attribute the sales generated. 
This needs to be done only once per organizer account.

In order to do so, navigate to :navpath:Your Organizer → :fa3-wrench: Settings → Sales channels: and click the :btn-icon:fa3-plus:Add a new channel: button.

On the following page, you will be able to select "GetYourGuide" as the sales channel type and give it a custom name.

## Preparing your event

In order to now sell your events on GetYourGuide, you will need to configure each event in question.

 1. Enabling the plugin

    Navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and switch to the :btn:Integrations: tab. 
    Click the :btn:Enable: button next to the "GetYourGuide" plugin. 

 2. Sell the event on the sales channel

    Navigate to :navpath:Your Event  → :fa3-wrench: Settings → General: 
    Check either the box next to "Sell on all sales channels" or at least one of the boxes next to "Restrict to specific sales channels". 

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