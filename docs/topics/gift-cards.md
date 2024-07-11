# Gift Cards

Gift cards are a type of product you sell in one of your shops, which customers can then use as a payment method for another purchase in one of your shops.
Gift cards are a payment method and can be enabled or disabled like any other payment provider.
The only difference is that there is no dedicated plugin for gift cards since gift cards are part of the core functionality of the pretix software.

Gift cards are not to be confused with vouchers.
Unlike vouchers, gift cards always represent a fixed amount of money that is subtracted from the total of the order.
Unlike vouchers, gift cards can be used across different events and organizers and do not affect the availability and visibility of certain products

## Prerequisites

Gift cards have to be enabled as a payment method for an event.
They are enabled by default.
If they are not enabled, you can change that by browsing to [Your event] → "Settings" → "Payment", clicking the :btn-icon:fontawesome-solid-gear:Settings: button next to "Gift cards" and checking the box next to " Enable payment method" at the top of the page.

Gift cards must be sold at a tax rate of 0%.
Sales tax is applied to the purchase that is made using the gift card—not to the purchase of the gift card itself.
That means you have to create a tax rule with a rate of 0% before you can create a gift card.
You can do that by browsing to [Your event] → "Settings" → "Tax rules", clicking the :btn-icon:fontawesome-solid-plus:Create a new tax rule: button, setting the "tax rate" field to 0.00% and saving the rule under an distinct internal name.

## How To

### Gift card settings

The organizer page has general settings for gift cards. 
Both of these settings only apply to gift cards issued **after** these settings have been saved. 
They do not apply retroactively to previously created gift cards. 
It therefore makes sense to finalize your decisions on these settings before you sell or manually issue any gift cards. 

![Organizer settings page, on the gift cards tab, showing options for how many years gift cards are valid for, and for how many digits gift card codes have.](../assets/screens/organizer/gift-cards.png)

Navigate to [Your organizer] :fontawesome-solid-arrow-right: "Settings" :fontawesome-solid-arrow-right: "General" and open the "Gift cards" tab.
This page allows you to make organizer-level settings for gift cards. 
You can choose how many years gift cards are valid for. 
If you enter a number here, then gift cards will expire after the specified period has passed at the end of the calendar year. 
For example, if you enter 0 into the field and then create a gift card in the year 2024, then the gift card will be valid until midnight of December 31st, 2024. 
This field is empty by default, meaning gift cards will remain valid indefinitely. 

This page also lets you choose how long gift card codes issued in your shop will be. 
The default is 12 digits, the minimum length is 6 digits, and the maximum length is 64 digits. 

### Accepting gift cards across different organizers

It is possible for other organizer accounts to accept gift cards issued by you. 
By default, gift cards issued by your organizer account will also only be accepted by your organizer account. 
However, you can invite an organizer to accept your gift cards. 
You can do that by navigating to [Your organizer] :fontawesome-solid-arrow-right: "Gift cards" :fontawesome-solid-arrow-right: "Acceptance" and clicking the :btn:Invite new organizer: button. 
Enter the organizer's short form into the field and click :btn:Save:. 
The organizer will then be listed on the acceptance settings page with the status "invited". 
The organizer can navigate to same settings page and "Accept" or "Decline" the invitation via the corresponding buttons. 
If they accept your invitation, the page will display their status as "active". 
You can retract the invitation or remove their ability to accept your gift cards via the :btn:Remove: button. 

### Manually issuing gift cards

You may want to manually issue a single gift card, for example as accommodation for an individual customer. 
You can do that by navigating to [Your organizer] :fontawesome-solid-arrow-right: "Gift cards" and clicking the :btn-icon:fontawesome-solid-plus:Manually issue a gift card: button. 

!!! Warning 
    Once a gift card has been created, it cannot be deleted. 
    If you are just trying out this feature, make sure to check the box next to "Test mode card". 
    This makes the gift card only valid in test mode of your shop. 
    Do not issue gift cards with secrets that can be easily guessed outside of test mode. 

The "Gift card code" field will already be filled out with a randomly generated code, but you can change that code to your liking. 
Any code you enter here manually must be between 2 and 190 digits in length and may only contain Latin letters, numbers, dots and dashes.
Diacritic symbols such as umlauts and accents are not supported. 
You have to specify a "Gift card value" larger than zero in the currency of your choice. 
If you want to create a gift card for test mode, check the box next to "Test mode card". 
If you want to create a gift card for the live shop, do not check that box. 
A test mode card will only work in test mode and a non-test mode card will only work when the shop is live. 

 - gift card acceptance
   - Other organizers you accept gift cards from
   - Other organizers accepting gift cards from you :btn:Invite new organizer:

### Products (event level)

 - creating a new gift card product

### Payment (event level)

 - settings for gift cards as a payment method

## Troubleshooting

What are common problems that could be encountered here? How do you solve them?

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information.
