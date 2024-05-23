# Event 

## Event creation 

After setting up your organizer account, the next step is creating an event. 
In order to create an event, you must be logged in to your [pretix](https://pretix.eu/control/) account. 
Click the :btn:pretix.eu: button in the top left corner of the website. 
This takes you to the dashboard, which includes an overview of your upcoming events. 
Click the :btn:⊕ Create a new event: button. 

![Screenshot of page titled "Create new Event–Step 1", showing options for choosing an organizer account, the event type, and languages to be used.](../assets/screens/event/create-event1.png "Create new event step 1 screenshot" ) 

Choose the organizer account that is hosting this event—most likely the one you just set up in the previous step of this tutorial. 
This selection cannot be changed after the event has been created, so make sure that you pick the right organizer account here. 

Next, choose the event type. 
You have two options: "Singular event or non-event shop" and "Event series or time slot booking". 
Creating an event series only makes sense if you're planning on hosting the same conference several times or if you're planning for your customers to participate in a series of conferences that they buy tickets for in a single purchase. 
Creating a singular event is the appropriate choice for most use cases, so we recommend you choose that option. 

After that, choose which languages to use for the event. 
By default, the languages you chose while setting up the organizer account should already be checked here. 
Simply activate and deactivate the languages as needed.

{% include "note-translations.md" %}

Once you are happy with your choices, click :btn:Continue: at the bottom right of the page. 

![Screenshot of page titled "Create new Event–Step 2", showing options for choosing name, short form, date, location, and geo coordinates for the event. 
Not pictured: currency, sales tax rate, time zone, start and end date of presale.](../assets/screens/event/create-event2.png "Create new event step 2 screenshot" ) 

You are now asked to provide a name and a short form for the event. 
Our example is a conference on xylology in the year 2027. 
We therefore choose "International Xylology Conference 2027" for the "event name" field, and "ixc27" for the "short form" field. 
The short form will be appended to your organizer's URL, resulting in an URL such as [https://pretix.eu/isx/ixc27], where "isx" is the name of your organizer account you chose during account creation and ixc27 is the name of the event you're choosing right now. 

{% include "note-short-form.md" %}

You also have to pick a start time and a currency for your event. 

An optional step on this page is choosing a location for your event. 
Your input into the "location" field will be used to search OpenStreetMap for that location. 
If the location can be found, the "geo coordinates" fields will be filled out automatically and the map preview will center on that location. 
If no results can be found for your input, you can manually drag the marker on the map to your event location. 
This will automatically update the "geo coordinates" fields. 
Alternatively, you can go to  [OpenStreetMap.org](https://www.openstreetmap.org), use the more advanced search function there to find your location, and then copy the address over to the "location" field. 

This page also allows you to set a sales tax rate for your event. 
If the taxation laws that apply to your event can be covered by a single percentage rule, you can enter that percentage here. 
If your tax situation is more complicated, you can set specific rules __after__ event creation is finished by navigating to [Your Event] → "Settings" → "Tax rules". 

{% include "warning-tax.md" %}

![Screenshot of page titled "Create new Event–Step 3", showing an infobox saying 'Please make sure to review all settings extensively. 
You will probably still need to change some settings manually, e.g. 
date and time settings and texts that contain the event name' and the option to import settings from a previously created event.](../assets/screens/event/create-event3.png "Create new event step 3 screenshot" ) 

You are then asked if you want to copy information from a previously created event. 
This step can save you a lot of work from your second event onwards. 
But since this is the first event you're organizing using pretix, simply leave the default (_"Do not copy"_) and click :btn:Continue: 

![Screenshot of page titled "Congratulations! You just created an event!", showing options for creating ticket types and enabling a few basic features for the event. 
Not pictured: setting up payment options and providing contact information.](../assets/screens/event/create-event4.png "Create new event step 4 screenshot" ) 

The next page congratulates you on creating your event. 
It also gives you a quick overview for products and basic settings for the event. 
We will take a closer look at products (tickets, gift cards, etc.) in the next section of this tutorial. 

Fill out the contact address and imprint URL in the "getting in touch with you" section near the bottom of the page. 
Provide a general email address at which your customers can contact you in the "contact address" field. 
Provide a URL to legal imprint information for your organization in the "imprint URL" field. 
These two pieces of information are mandatory for your ticket shop to go live. 

Once you click :btn:Save: at the bottom of the page, you will be taken to an overview of the event, which gives you its name, the timeline of tickets sales and presale, the status of your ticket shop (most likely in test mode by this point). 

## Dashboard

Now that you have created your event, you have access to all possible options for the event. 
You can visit the dashboard for your event by clicking the :btn:pretix.eu: button in the top left and then selecting the event you just created in the list titled "your upcoming events". 
The dashboard for your event gives you an overview of the event's basic information and status. 
It allows you to leave an internal comment for yourself and your team and it logs recent changes. 

![Screenshot of dashboard for a demo event titled International Xylology Conference 2027, showing the title, buttons for sharing the event, the timeline, an overview of orders, payments and tickets left, as well as a field for internal comments. 
Not pictured: event logs for recent changes.](../assets/screens/event/event-dashboard.png "Event dashboard screenshot") 

## Customer and attendee data 

If you need to issue certificates of participation to your attendees, then you have to record their name and affiliation during purchase. 
This section tells you how to do that. 
Navigate to [Your Event] → "Settings" → "General" and open the "customer and attendee data" tab. 
Here, under the "attendee data (once per personalized ticket)" subheading, you have options for asking for attendee names, addresses per ticket, and company per ticket. 
We will set those three questions to "ask, but do not require input". 
By not making the input mandatory, it is still possible for attendees to not give you their data if they do not require a certificate of participation. 
 In the text fields labeled "attendee data explanation", add an explanation as to why you're collecting the data in question. 
An explanation such as "this information is necessary for issuing each attendee a certificate of participation" should suffice. 

Under "other settings", you can choose the format in which pretix will ask attendees for names and titles. 
We recommend that you finalize your choice here before taking your ticket shop live because changing this after already having received orders can lead to issues when sorting or changing names. 

## Account activation 

The overview will probably display a warning that your organizer account is not yet active. 
If you see that warning, please click the link and fill out the necessary information in the form. 
Activating an account is a manual process and may take some time depending on the availability of our team. 

## Texts 

Open the "texts" tab. 
Type a text for welcoming your customers to your store page and guiding them through the process of purchasing a ticket into the "front page text" field. 
If you have set time constraints for the presale, then you should add an "end of presale text". 
This text will be displayed at the top of your ticket shop when the presale time has run out. 
If you are making use of vouchers, e.g. 
inviting speakers to your event by sending them voucher codes, then you should add a "voucher explanation" telling them how to obtain a voucher code. 
This text will be displayed next to the input field for a voucher code. 

The "texts" tab lets you define a lot of text messages for other purposes. 
Every field comes with an explanation as to where the text will be used. 
All fields support simple and human-readable formatting via Markdown. 
Whenever you define a text, make sure you also provide a translation for each language you selected in the localization tab. 

## Shop design 

![Screenshot of "shop design" tab, showing options for the header image and social media image, as well as a locked section at the bottom.](../assets/screens/event/shop-design.png "Event shop design tab screenshot") 

Switching to the "shop design" tab at the top allows you to add content to your event shop. 
You can see what the shop looks like from the customer's perspective if you click the :btn:👁 Go to shop: button in the bar at the top. 
The demo we are creating for this tutorial is located at https://pretix.eu/awesome-corp/ixc27/. 
Replacing "awesome-corp" with the short form of your organizer and "ixc27" with the short form of your event in that URL will take you to your shop. 

By default, the name of the event will be displayed in the page header of your shop. 
The shop design settings allow you to replace the name with a header image that tells your customers about the event (e.g., by means of the event name, logo, or recognizable design). 
It should be a .png or .jpg file with a resolution of 1140 × 120 pixels or slightly smaller. 
You can add the header image by clicking the :btn:Browse...: button next to the "Header image" option and choosing the image file to upload from your computer. 
The header image will replace the name of the event at the top of the page unless you check the box next to "show event title even if a header image is present". 
You have the option to use the image in its full size, in which case it should be at least 1170 pixels in width. 

The "social media image" option lets you upload a .png  or .jpg file that will be used as a preview if you post links to your ticket shop on social media. 
If you do not upload a file here, the header image will be used for previews instead. 

!!! Warning

    Unlocking the color and font settings is not reversible. 
Only click the :btn:🔓 Unlock: button if you are absolutely positive that your event shop should have different color and font settings than your organizer's public profile. 
Once the settings have been unlocked, they have to be adjusted independently for this event. 

By default, the section with color and font settings is locked and you can only change them on the on organizer level. 
This way, you can easily change them for all of your events at the same time. 
You can either go to the organizer settings to change them for all your events or you can unlock them to change them for this event individually. 
If you wish to make individual adjustments to the shop design of the event, click the :btn:🔓 Unlock: button. 
This will allow you to adjust colors and fonts for the event shop independently of any settings you choose for the public profile on the organizer level. 

We recommend that you leave the settings here locked since that makes it easier to keep the shop designs consistent. 
If you want to change the design globally, click the :btn:Go to organizer settings: button and make your adjustments there. 

## Timeline 

By default, tickets will be available for purchase from the moment your ticket shop goes live until the end of your event. 
If you want to restrict availability of your tickets to a certain time period, you can do that by switching to the "timeline" tab. 
With the options available here, you can set a start and end date and time for the sale of tickets and other products in your shop. 
If you set a start of presale, no products will be able to be sold before that date and time. 
If you send an end of presale, no products will be able to be sold before that date and time. 
If you have enabled box office sales (pretixPOS) during event creation or on the "basics" tab of the general settings, you will still be able to sell products via pretixPOS outside the presale period you set here. 

This page also lets you set restrictions on when and how your customers can make modifications to the details of their orders. 
The restrictions you set up on the "timeline" tab apply to all products in your shop. 
You can also restrict availability for individual products by navigating to [Your event] → "Products" → "Products", clicking the product in question, and switching to the "availability" tab. 


## Tax rules 

Navigate to [Your event] → "Settings" → "Tax rules". 
Click the :btn:+ Create a new tax rule: button. 
The "official name" fields are already filled out with "VAT" (English), "MwSt." (German) and, if  available, the appropriate translations in any languages you have selected. 
Choose an internal name if needed. 
This will only be used for the backend and helps you distinguish tax rules if you use more than one. 
Set the tax rate to the appropriate level, e.g. 
19% for Germany and click the :btn:Save: button. 
