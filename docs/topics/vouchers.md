# Vouchers

Vouchers are codes which can be redeemed for certain products in your shop. 
pretix allows you to automatically generate these codes as well as associated URLs and send them out via email. 
Vouchers have several useful applications. 
You can use them to:

 - make products available at a reduced price for voucher holders
 - make a product available only to a select group of people (such as speakers at a conference or invited guests)
 - reserve a certain quantity of a product quota for voucher holders
 - make sure that voucher holders still have access to a product even if it is sold out
 - make products in your shop visible only to voucher holders

Vouchers are not to be confused with [gift cards](gift-cards.md). 
Gift cards essentially function like an additional method of payment for your customers. 
They always represent a fixed amount of money that is subtracted from the total of the order. 
Gift cards can be used across different events and organizers and do not affect the availability and visibility of certain products. 

## Prerequisites

Vouchers are handled on the event level, so you first need to create the event for which you want to create vouchers. 
Your account needs to be activated before you can send out vouchers via email. 

## General usage

The settings page for vouchers is located at [Your Event] :fontawesome-solid-arrow-right: ":fontawesome-solid-tags: Vouchers". 
It gives you an overview of all vouchers that have already been created as well as options to search and filter vouchers. 

![Page titled Vouchers, showing an overview of all vouchers that have already been created, options to search and filter vouchers, and buttons for creating or importing vouchers.](../assets/screens/vouchers/vouchers-all.png)

Clicking the :btn-icon:fontawesome-solid-plus: Create a new voucher: button takes you to a dialog for creating a single new voucher code. 
This is useful for when you are planning to publish a single voucher code that can then either be used by a single person or by multiple people. 

The :btn-icon:fontawesome-solid-plus: Create multiple new vouchers: button takes you to a dialog for creating multiple new vouchers. 
This dialog also gives you access to the email settings, allowing you to instantly send out vouchers via email after creating them. 

The :btn-icon:fontawesome-solid-download: Download: button lets you download a .csv file of the full list of vouchers you have created. 
It is generally advisable to download and save your vouchers using this button whenever you create a set of vouchers. 
The .csv export can serve as a backup archive for your voucher codes, lets you to distribute the codes by methods other than the pretix-native emailer, and allows you to re-use the same codes for a different event. 

The :btn-icon:fontawesome-solid-upload: Import vouchers: button lets you upload such a list after saving it from a different event. 
This function is meant for importing a set of vouchers that have all been created using the same settings.
If you have saved the full list of vouchers from a different event and it includes more than one type of voucher, then it is advisable to split the .csv file according to type and import each part individually. 

Whenever you generate one or more vouchers, it is recommended that you copy them and save them, for example in a plain text file on your computer. 

If you have checked the box next to "Send vouchers via email" and entered email addresses in the Recipients field, make sure that you are happy with the subject line and message text previews before you click :btn:Save:. 
The emails will be sent out as soon as you click the :btn:Save: button. 

Whenever you create more than one type of voucher for an event, it is recommended that you enter a descriptor in the "Tag" field. 
This can make it easier to find, edit and clone certain sets of vouchers in the list. 
A useful entry in the "Tag" field could be the date and time at which the vouchers were created, the purpose for which they were created, or both. 
For example, "2024-07-08 09:45 Limited Time Offer" would be a very useful tag if there is a large total number of vouchers for the event in question. 

As described in the introduction, vouchers have several useful applications. 
Those applications will be explained in the following subsections. 

## Applications 

### Offering a limited discount 

This subsection explains how to create a voucher code for a limited time discount to attract more customers to your shop. 

![Page titled Voucher, showing options for creating a single voucher code.](../assets/screens/vouchers/create-single.png)

Clicking the :btn-icon:fontawesome-solid-plus: Create a new voucher: button takes you to a dialog for creating a single new voucher code. 
The voucher code has already been filled out automatically, but you can change it and provide your own as long as it is at least 5 and no more than 255 characters in length. 
Since this code is supposed to be able to be used more than once, set "Maximum usages" to 9999999. 
Set the "Valid until" option to the end of the limited time offer, for example the end of the following day. 
The "Price effect" option offers several different possibilities as to what effect the voucher should have on the price of the product. 
As an example, you could set "Price effect" to "Reduce product price by (%)" and set "Voucher value" to "10" for a 10% discount upon use of the voucher. 

You can use the "Maximum discount budget" to limit the usage of the voucher. 
Another option of limiting potential losses in case of unexpectedly high usage of the voucher is limiting the number of "Maximum usages". 
Simply set that number to a reasonable limit. 
Uncheck the box next to "Show hidden products that match this voucher". 
Leaving this option checked while issuing vouchers for "All products" would mean that all hidden products are visible to a customer who is using the voucher. 
Click :btn:Save: once you are happy with your choices. 

### Exclusive product availability

This subsection explains how to use vouchers to make a product (or multiple products) only available to a select group of invited guests. 
This option is appropriate for cases in which you know the group of recipients beforehand and have a full list of their email addresses, e.g. members of a club, speakers at a conference, or VIPs who get an invitation. 

Navigate to  [Your event] → ":fontawesome-solid-ticket: Products" → "Products" and create or edit the admission product for which you want to restrict availability. 
While you are doing that, open the :btn:Availability: tab and check the box next to "This product can only be bought using a voucher".
If you set the visibility toggle next to this option to "Hide product if unavailable", then the product will be hidden in your shop. 
I will only be displayed to customers who entered one of the voucher codes into the voucher field, or who landed in the shop by following one of the voucher links. 
Repeat these steps for each product that you want to make available through this voucher. 

Next, create a quota, add only the products in question to it, and set the "Total capacity" so that it covers the number of emails you are planning to send out. 

![Page titled Create multiple vouchers, showing options for creating multiple voucher codes.](../assets/screens/vouchers/create-multiple.png)

Then, navigate to [Your Event] :fontawesome-solid-arrow-right: ":fontawesome-solid-tags: Vouchers" and click the :btn-icon:fontawesome-solid-plus: Create multiple new vouchers: button. 
Generate the same number of voucher codes as people you are planning to invite. 
The number of vouchers does not have to be equivalent to the number of emails you are sending out. 
You can send multiple vouchers to the same email address using the "number" column in the list of "Recipients". 

Under "Product", choose the product for which you want to restrict availability (or the quota, if there is more than one product). 
If you have set the visibility toggle of the product to hidden, check the box next to "Shows hidden products that match this voucher" at the bottom of the page. 
This option has no effect if the visibility toggle is set to "Show product with info on why it's unavailable". 
An optional step that can be useful if e.g. you are inviting VIPs is checking the box next to "Offer all add-on products for free when redeeming this voucher". 
This allows voucher holders to freely choose as many add-on products as they like on top of their tickets. 

![Page titled Create multiple vouchers, showing options for sending out emails.](../assets/screens/vouchers/send-emails.png)

Check the box next to "Send vouchers via email" in order to display the email settings. 
You can save your invited guests the step of opening your shop and then entering the voucher code by including the placeholder {voucher_url_list} in the "Message" text. 
Opening that link will take them to the shop with the voucher code preselected and all associated products visible. 
Enter the mail addresses into the "Recipients" field. 
The software will display an error message if the number of recipients and generated vouchers do not match up. 

### Reserving tickets for a certain group

This subsection explains how to use vouchers to ensure that a certain group of people gains access to an event, for example, guests invited to a concert by the performing artists. 
Navigate to [Your Event] :fontawesome-solid-arrow-right: ":fontawesome-solid-tags: Vouchers", click the :btn-icon:fontawesome-solid-plus: Create multiple new vouchers: button, and set the number of codes to generate one voucher per member of the group in question. 
Optionally, you may choose a descriptive prefix such as "guest-list-". 
Set "Product" to your event's basic admission ticket, set "Price effect" to "Set product price to" and the voucher value to 0.00. 
This means that the voucher will entitle each holder to one basic admission ticket for free. 

![Page titled Create multiple vouchers, highlighted are the options for reserving tickets from a quota and bypassing quotas.](../assets/screens/vouchers/create-multiple-reserve.png)

There are two methods for ensuring access to tickets for the voucher holders: reserving tickets from a quota or allowing them to bypass quotas. 
For the first option, check the box next to "Reserve ticket from quota". 
You may have to increase the total capacity of the quota, particularly if the quota is already sold out. 
This method has the advantage that you can still keep track of products purchased using this voucher via quotas, just like all other products. 
The disadvantage is that this method does not give voucher holders reliable access to products if you selected one of the "Any product in quota" options under "Product" and the products are part of more than one quota with limited capacity. 
You can still use this method without worrying about that if you select a specific product under "Product", or if the products in question are only part of one quota. 

For the other method, check the box next to "Allow to bypass quota" instead. 
This gives voucher holders access to tickets even if all corresponding quotas are already sold out. 
You should choose this method over the other one if you selected one of the "Any product in quota" options under "Product" and the products are part of more than one quota with limited capacity. 