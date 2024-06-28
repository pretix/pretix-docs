# Event 

After setting up an organizer account, the next step is creating an event. 
This article describes the creation and basic setup of an event. 
In this article, we will: 

 - create an event in four steps 
 - get an overview of the event's status on the dashboard
 - enable the collection of customer and attendee data 
 - add images to the ticket shop 

This includes all the necessary steps for creating an event and setting up the ticket shop so that we can add products to it in the next article of this tutorial. 

## Event creation 

In order to create an event, we must be logged in to our [pretix](https://pretix.eu/control/) account. 
Clicking the :btn:pretix.eu: button in the top left corner of the website takes us to the dashboard and an overview of our upcoming events. 
We will now click the :btn:⊕ Create a new event: button. 

![Screenshot of page titled "Create new Event—Step 1", showing options for choosing an organizer account, the event type, and languages to be used.](../assets/screens/event/create-event1.png "Create new event step 1 screenshot" ) 

An event in pretix is always associated with an organizer account, so we have to choose one here. 
We will choose the organizer that is hosting this event—that is, the one we just set up in the previous step of this tutorial. 
This selection cannot be changed after the event has been created, so it is important to pick the correct organizer account here. 

Next, we have to choose the event type. 
There are two options: "Singular event or non-event shop" and "Event series or time slot booking". 
For this tutorial, we want to create a simple conference that takes place on a single weekend, so we are going to choose the option "Singular event or non-event shop". 

We are going to choose which languages to use for the event. 
By default, the languages chosen while setting up the organizer account should already be checked here. 
We will simply activate and deactivate the languages as needed.

{% include "note-translations.md" %}

![Screenshot of page titled "Create new Event—Step 2", showing options for choosing name, short form, date, location, and geo coordinates for the event. 
Not pictured: currency, sales tax rate, time zone, start and end date of presale.](../assets/screens/event/create-event2.png "Create new event step 2 screenshot" ) 

After clicking :btn:Continue:, we are now asked to provide a name and a short form for the event. 
We are going to create a simple example conference for this tutorial. 
Therefore, we will choose "Example Conference" for the "event name" field, and "ex-conf-2027" for the "short form" field. 
The short form is appended to the organizer's URL. 
In our case, this results in the following URL: [https://pretix.eu/ex-org/ex-conf-2027](https://pretix.eu/ex-org/ex-conf-2027). 

{% include "note-short-form.md" %}

Just like the name and short form, the start time and the currency for our event are mandatory information. 
We're going to enter the fourth of June, 2027, into the start time field and we're going to choose the Euro in the currency drop-down menu. 

Since we already know the location for our event, we're going to put that location into pretix now. 
This information is optional and can still be changed later. 
Our input into the "location" field will be used to search OpenStreetMap for that location. 
If the location can be found, the "geo coordinates" fields will be filled out automatically and the map preview will center on that location. 
If no results can be found for the input, the marker on the map can be dragged to the event location manually. 
This will automatically update the "geo coordinates" fields. 
Alternatively, we can use the more advanced search function on [OpenStreetMap.org](https://www.openstreetmap.org) and copy the address over to the "location" field. 

This page also allows us to set a sales tax rate for our event. 
Taxation rules can also be changed after event creation is finished. 
We are holding our event in Germany and a single percentage rule applies to all of our products. 
Thus, we are going to add a 19% tax rule here. 

{% include "warning-tax.md" %}

![Screenshot of page titled "Create new Event—Step 3", showing an infobox asking the user to review all settings extensively and the option to import settings from a previously created event.](../assets/screens/event/create-event3.png "Create new event step 3 screenshot" ) 

We are then asked if we want to copy information from a previously created event. 
This step can save us a lot of work from our second event onwards. 
But since this is the first event we're organizing using this organizer account, we will simply leave the default (_"Do not copy"_) and click :btn:Continue: 

![Screenshot of page titled "Congratulations! You just created an event!", showing options for creating ticket types and enabling a few basic features for the event. 
Not pictured: setting up payment options and providing contact information.](../assets/screens/event/create-event4.png "Create new event step 4 screenshot" ) 

The next page congratulates us on creating our event and gives us a quick overview of products and basic settings for the event. 
We will take a closer look at products (tickets, gift cards, etc.) in the next section of this tutorial. 
All we are going to do on this page is to add two more pieces of information that are mandatory for our ticket shop to go live. 
We will provide a general email address at which our customers can contact us in the "contact address" field. 
This email address will be displayed in the page footer of our shop with the label "contact event organizer". 
We will provide a URL to legal imprint information for our organization's online presence in the "imprint URL" field. 

Once we click :btn:Save: at the bottom of the page, we are taken to an overview of the event, which gives us its name, the timeline of tickets sales and presale, and the status of our ticket shop, which should be in test mode by this point. 

## Event-level Dashboard

Now that we have created our event, we have access to all possible options for the event. 
We can visit the event-level dashboard by clicking the :btn:pretix.eu: button in the top left corner and then selecting the event we just created in the list titled "your upcoming events". 
The event-level dashboard gives us an overview of the event's basic information and status. 
It allows us to leave an internal comment for ourselves or our team and it logs recent changes. 

![Screenshot of dashboard for a demo event titled Example Conference, showing the title, buttons for sharing the event, the timeline, an overview of orders, payments and tickets left, as well as a field for internal comments. 
Not pictured: event logs for recent changes.](../assets/screens/event/event-dashboard.png "Event dashboard screenshot") 

At this point, the overview will probably display a warning that our organizer account is not yet active. 
The first time we see this warning, we are going to click the link and fill out the necessary information in the form. 
Activating an account is a manual process and may take some time depending on the availability of the pretix team. 
Thus, this warning may persist for a while even if all necessary information has already been provided. 

## Customer and attendee data 

We want to to issue certificates of participation to the people who attend our conference. 
That means we have to record their name and affiliation during purchase. 
We are going to navigate to [Event] → "Settings" → "General" and open the "customer and attendee data" tab. 
Here, under the "attendee data (once per personalized ticket)" subheading, there are options for asking for attendee names, addresses per ticket, and company per ticket. 
We will set those three questions to "ask, but do not require input". 
By not making the input mandatory, it is still possible for attendees to not give us their data if they do not require a certificate of participation. 
In the text fields labeled "attendee data explanation", we will add an explanation as to why we're collecting the data in question. 
Our explanation reads as follows: 
"Information for each individual attendee for whom you are buying a ticket. Without this information, we cannot issue certificates of participation."

Under "form settings", we can choose the format in which pretix will ask attendees for names and titles. 
We are going to select "ask for given name, + family name, display like John Doe" for names and "free text input" for titles. 
We will finalize our choice here before taking the ticket shop live.
This is important because changing this after already having received orders can lead to issues when sorting or changing names.

## Shop design 

![Screenshot of "shop design" tab, showing options for the header image and social media image, as well as a locked section at the bottom.](../assets/screens/event/shop-design.png "Event shop design tab screenshot") 

Switching to the "shop design" tab at the top allows us to add images to our event shop and customize its colors. 
Clicking the :btn:👁 Go to shop: button in the bar at the top takes us to a preview of the shop from the customers' perspective. 
A shop created with pretix Hosted will always be located at https://pretix.eu/[OrganizerShortForm]/[EventShortForm]/. 
The shop we are creating for this tutorial is located at [https://pretix.eu/ex-org/ex-conf-2027/](https://pretix.eu/ex-org/ex-conf-2027/). 

By default, the name of the event will be displayed in the page header of our shop. 
The shop design settings allow us to replace the name with a header image that tells our customers about the event (e.g., by means of the event name, logo, or recognizable design). 
We are going to add a header image by clicking the :btn:Browse...: button next to the "Header image" option and choosing a .png file with a resolution of 1140 × 120 pixels to upload from our computer. 
By default, the header image will replace the name of the event at the top of the page. 
We still want to include the name of the event though, so we are going to check the box next to "show event title even if a header image is present". 

We are also going to upload a .png file for the "social media image" option. 
This will be used as a preview for any links to our ticket shop we post on social media. 
Not uploading a file here would mean that the header image will be used for previews instead. 

!!! Warning

    Unlocking the color and font settings is not reversible. 
    Only click the :btn:🔓 Unlock: button if you are absolutely positive that your event shop should have different color and font settings than your organizer's public profile. 
    Once the settings have been unlocked, they have to be adjusted independently for this event. 

By default, the section with color and font settings is locked and we can only change them on the organizer level. 
We are going to leave the settings here locked since that makes it easier to keep the shop designs consistent. 

## Conclusion 

We have gone through the four-step event creation process, gotten an overview of the event's status on the event dashboard, enabled the collection of customer and attendee data, and added images to the ticket shop. 
We can now move on to creating products to be sold in our shop. 