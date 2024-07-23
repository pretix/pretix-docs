# Gift Cards

Gift cards are a type of product you sell in one of your shops, which customers can then use as a payment method for another purchase in one of your shops.
Gift cards are a payment method and can be enabled or disabled like any other payment provider.
The only difference is that there is no dedicated plugin for gift cards since gift cards are part of the core functionality of the pretix software.

Gift cards are not to be confused with [vouchers](vouchers.md).
Unlike vouchers, gift cards always represent a fixed amount of money that is subtracted from the total of the order.
Also unlike vouchers, gift cards can be used across different events and organizers and do not affect the availability and visibility of certain products. 

!!! Note 
    pretix treats gift cards as "multi-purpose vouchers" within the meaning of EU Council Directive 2016/1065 of 27 June 2016. 
    pretix does not support charging taxes on the sale of gift cards. 
    Instead, taxes will always be charged on the purchase for which gift cards are used. 

## Prerequisites

In order to use gift cards as a payment method for an event, they have to be enabled for that event.
Gift cards are enabled by default.
If they are not enabled, you can change that by browsing to [Your event] :fontawesome-solid-arrow-right: ":fontawesome-solid-wrench: Settings" :fontawesome-solid-arrow-right: "Payment", clicking the :btn-icon:fontawesome-solid-gear:Settings: button next to "Gift cards" and checking the box next to " Enable payment method" at the top of the page.

pretix only supports selling gift cards at a tax rate of 0%.
Sales tax is applied to the purchase that is made using the gift card—not to the purchase of the gift card itself.
This is the procedure prescribed by tax law in Germany and in some other countries. 
You have to create a tax rule with a rate of 0% before you can create a gift card.
You can do that by browsing to [Your event] :fontawesome-solid-arrow-right: ":fontawesome-solid-wrench: Settings" :fontawesome-solid-arrow-right: "Tax rules", clicking the :btn-icon:fontawesome-solid-plus:Create a new tax rule: button, setting the "tax rate" field to 0.00% and saving the rule under a distinct internal name.

{% include "warning-tax.md" %}

## General usage

The following two subsections tell you how to do the basic setup for gift cards. 
These steps are needed regardless of your individual use case. 

### Gift card validity and code length

General settings for gift cards can be found on your organizer page. 
Settings on the organizer level only apply to gift cards issued **after** these settings have been saved. 
They do **not** apply retroactively to previously created gift cards. 
It is therefore advisable to read this subsection and finalize your decisions on these settings before selling or manually issuing any gift cards. 

![Organizer settings page, on the gift cards tab, showing options for how many years gift cards are valid for, and for how many digits gift card codes have.](../assets/screens/organizer/gift-cards.png)

Navigate to [Your organizer] :fontawesome-solid-arrow-right: ":fontawesome-solid-wrench: Settings" :fontawesome-solid-arrow-right: "General" and switch to the "Gift cards" tab. 
Organizer-level settings for gift cards can be adjusted on this page.
The "Validity of gift card codes in years" field allows you to specify for how many years your gift cards should be valid. 
The field accepts whole numbers as input. 
The exact expiry date is always the end of the calendar year. 
For example, if you enter 0 into the field and then create a gift card in the year 2025, then the gift card will be valid until midnight of December 31st, 2025. 
This field is empty by default, meaning gift cards will remain valid indefinitely. 
If you issue gift cards manually, you can set an individual date of expiration before or after the end of the period you chose here. 

This page also lets you choose how long gift card codes issued in your shop will be. 
The default is 12 digits, the minimum length is 6 digits, and the maximum length is 64 digits. 

### Accepting gift cards as a payment method 

Any gift card issued through your organizer account will be valid for every event created by that organizer account. 
The gift card payment method is enabled by default for any newly created event. 
In your shops, the option for paying via gift card is hidden by default. 
This changes as soon as the first gift card is issued through your organizer account, be it manually or automatically. 

![Page titled Payment settings: Payment provider: Gift card, the box next to Enable payment method is checked.](../assets/screens/payment/gift-cards.png)

You can find the settings for gift cards as a payment method by navigating to [Your event] :fontawesome-solid-arrow-right: ":icon:fontawesome-solid-wrench:  Settings" :fontawesome-solid-arrow-right: "Payment" and clicking the :btn-icon:fontawesome-solid-gear:Settings: button next to "Gift cards". 
Here, you can restrict the availability of the payment method by date, sales channel, and territory, just like you can with any other payment method. 
If you do not want to accept gift cards as payment for a certain event at all, you have to uncheck the box next to "Enable payment method" at the top of the page.
Note that these settings apply on the event level, so they have to be changed for each event individually. 

## Applications 

There are three methods for giving your customers access to gift cards: selling them in your shop, using them for refunds, and issuing them manually. 
These methods will be described in the following subsections. 

### Creating a gift card for selling it in your shop

![Page titled Modify product: Gift card, on the Additional settings tab, the box next to This product is a gift card is checked.](../assets/screens/products/gift-card.png)

If you want to sell gift cards in your shop, you can create them just like any other product. 
Navigate to [Your event] :fontawesome-solid-arrow-right: "Products" and click the :btn-icon:fontawesome-solid-plus:Create a new product: button. 
Choose "Non-admission product" as the "Product type" and a 0.00% tax rule as the "Sales tax" option. 
After clicking :btn:Save and continue with more settings:, switch to the "Additional settings" tab, check the box next to "This product is a gift card" and click :btn:Save:. 
If you check the box next to "Free price input", the value of the gift card will be the same as the price that the customer chooses to pay for it. 

Create a new quota, add the gift card to it and check the box next to "Ignore this quota when determining event availability". 

### Using gift cards for refunds 

![Page titled Cancellation settings, on the Paid orders tab, highlighted are the settings for Refund method, offering four options, two of them involving gift cards.](../assets/screens/gift-cards/refund.png)

pretix can automatically issue gift cards as a method for refunds. 
If you want to use this feature, navigate to [Your event] :fontawesome-solid-arrow-right: "Settings" :fontawesome-solid-arrow-right: "Cancellation" and open the "Paid orders" tab. 
Under "Refund method", choose either "Customers can choose between a gift card and a refund to their payment method" or "All refunds are issued as gift cards". 

### Manually issuing gift cards

![Page titled Create a new gift card featuring text input fields for code, value, expiry date as well as special terms and conditions, plus choices for currency and whether or not the card is for test mode.](../assets/screens/gift-cards/create.png)

You may want to manually issue a single gift card, for example as accommodation for an individual customer. 
You can do that by navigating to [Your organizer] :fontawesome-solid-arrow-right: ":fontawesome-regular-credit-card: Gift cards" and clicking the :btn-icon:fontawesome-solid-plus:Manually issue a gift card: button. 

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

The default value in the "Expiry date" fields is determined by the "Validity of gift card codes in years" setting on the organizer settings page. 
If you clear the contents of the "Expiry date" fields, the gift card you are creating will remain valid indefinitely regardless of the organizer-level settings. 
The gift card is created once you click :btn:Save:. 

### Accepting gift cards across different organizers

It is possible for other organizer accounts to accept gift cards issued by you. 
By default, gift cards issued by your organizer account will also only be accepted by your organizer account. 
However, you can invite another organizer to accept your gift cards. 

![Page titled Invite organizer, showing a text input for the organizer's short form and a checkbox for allowing access to reusable media, both empty.](../assets/screens/gift-cards/invite-organizer.png)

You can do that by navigating to [Your organizer] :fontawesome-solid-arrow-right: ":fontawesome-regular-credit-card: Gift cards" :fontawesome-solid-arrow-right: "Acceptance" and clicking the :btn:Invite new organizer: button. 
Enter the organizer's short form into the field and click :btn:Save:. 
The organizer will then be listed on the acceptance settings page with the status "invited". 
The organizer can navigate to same settings page and "Accept" or "Decline" the invitation via the corresponding buttons. 
If they accept your invitation, the page will display their status as "active". 
You can retract the invitation or remove their ability to accept your gift cards via the :btn:Remove: button. 

If you want to accept another organizer's gift cards in your shops, you will have to ask them to send you an invitation and accept it as described above. 
Either way, it is your own responsibility to handle the exchange of money to offset the transactions between you and the other organizers. 

## Troubleshooting

### Devaluing gift cards 

Once a gift card has been issued, be it automatically or manually, it cannot be deleted. 
If you have erroneously created a gift card and want to make sure that it cannot be used for payment, you have to manually devalue it. 
In order to do that, navigate to [Your organizer] :fontawesome-solid-arrow-right: ":fontawesome-regular-credit-card: Gift cards" and click the gift card in question in the list. 

![Page titled Gift card: gift card code, showing a gift card that has been created through an order with a value of €92.00 and a manual transaction of minus €92.00, leaving the gift card at a value of €0.00.](../assets/screens/gift-cards/devalue.png)

Note down the reason for the devaluing in the text field in the "Information" column.
The gift card's "Current value" is displayed in the "Details" box. 
Enter the current value's negative in the "Value" field. 
For example, for an erroneously created gift card worth €92.50, enter "-92.50" and click the :btn-icon:fontawesome-solid-plus:: button. 
That will add a new entry to the list of transactions and change the current value of the gift card to €0.00, meaning it cannot be used for payment. 

The same process can be used for increasing or decreasing the value of a gift card if it has been created with the wrong value. 

## Further Information

 - [pretix Tutorial: Geschenkgutscheine (German) on YouTube](https://www.youtube.com/watch?v=ZEnXy2SXNsc)

## See Also

 - [Payment](payment/index.md) 