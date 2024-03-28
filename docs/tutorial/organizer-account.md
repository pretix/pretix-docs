# Organizer account

An organizer account represents an entity that is running events, for example a company, an institution, or you yourself. You have already created an organizer account when you created your personal account - or, if you were invited to pretix by a member of your team, then accepting that invitation has already given you (partial) access to an organizer account. 

This section of the tutorial tells you how to customize your organizer account and add necessary and optional information to it. 

## Navigating to the organizer account settings 

![pretix.eu dashboard, showing upcoming events, a button for creating a new event, the mail address of the account currently logged in, and a sidebar with the following options: Dashboard, Events, Organizers, Search, User settings, Reports, Shipping list](../../assets/screens/account/dashboard.png)

After finishing account creation and logging in to [pretix.eu/control](https://pretix.eu/control/), you are greeted by the dashboard. Click the :btn:Organizers: button in the sidebar to get to the Organizers page. 

![pretix.eu organizers page, showing the list of available organizer accounts which only includes 'Awesome Event Corporation'. There is a filter function for the list of organizers and a button labeled 'Create a new organizer'](../../assets/screens/organizer/organizers.png) 

Clicking your organizer account in the list takes you to a page displaying all events associated with that organizer. 

![pretix.eu organizers page, showing the list of all events associated with 'Awesome Event Corporation'. There is a filter function for the list of events and a button labeled 'Create a new event'](../../assets/screens/organizer/event-list.png) 

Click :btn:Settings: in the sidebar to set up your organizer account. This lands you on the general settings page for the organizer account. 

## General 

![Organizer settings page, on the general tab, showing the following options: Name, Short form, Imprint URL, Contact address, Info text. Not pictured: 'Allow creating a new team during event creation' option, 'Save' button](../../assets/screens/organizer/general-settings.png) 

The fields for "Name" and "Short form" are already filled out. The short form cannot be changed because it is the organizer's unique identifier. 

If you are operating from Germany, it is recommended that you enter the URL to your website's imprint in the "Imprint URL" field. 

Your input into the "Contact address" field will be displayed publicly to allow your customers to contact you. 

You can add an info text to your organizer account. The info text is not displayed anywhere by default, but you can use this in ticket templates if you want to.

Confirm your changes on the "General" tab by clicking the :btn:Save: button on the bottom of the page. 

## Localization

After saving the general settings, switch to the "Localization" tab. We recommend changing localization settings __before__ customizing the organizer page because the localization settings determine which customizations are possible on the organizer page. 

Under "Available languages", you can choose which languages your ticket shop will be made available in. The options officially maintained by the pretix team are English, German, and German (informal). German uses "Sie" to address the user whereas German (informal) uses "Du". You can also choose one of the community translations for your organizer page. They are displayed in the list below along with a percentage of how much of the software is translated. English is used as the fallback langauge for missing translations. 

This setting also determines the default languages when creating new events, though languages can be activated or deactivated for each event individually.

!!! Note 

    pretix offers many settings and customizations where you input your own text, for example, the description on the organizer page, the name of your events, and so on. You will need to provide a translation in every language you choose here for each individual item. This can amount to a lot of work. We recommend not using more than two or three languages at a time unless you are working with a dedicated translators. 


Choose a country or region from  the drop-down "Region" menu. The selection will be used to determine default date, time, address and phone number formatting. The language chosen above will take a higher priority than the region. 

Also choose a "Default timezone" from the drop-down menu with that title. 


## Organizer page 

Switching to the "Organizer page" tab at the top allows you to set customizations for your organizer page. The organizer page is the public profile of your organizer. You can take a look at it by clicking the :btn👁 Public profile: button in the bar at the top. 

![Organizer settings page, on the organizer page tab, showing the following options: Header image, Use header image in its full size, Use header image also for events without an individually uploaded logo, Homepage text (in multiple languages). The "Public profile" button in the top bar is highlighted.](../../assets/screens/organizer/organizer-page-public-profile.png) 

By default, the organizer name will be displayed in the page header of your public profile. The organizer page settings allow you to replace the name with an image. The image should include your logo. It should be a .png or .jpg file with a resolution of 1140 × 120 pixels or smaller. If you want to use a larger header image on your public profile, you should check the "Use header image in its full size" box. This option works best with images of 1170 or more pixels in width. In any case, we recommend not using an image with small details, since it will be resized for smaller screens. You can add the header image by clicking the :btn:Browse...: button next to the "Header image" option and choosing the image file to upload from your computer. You are also given the option to use this header image on pages for events that do not have their own individually uploaded logo. 

In the "Homepage text" fields, you can provide text to be displayed on your public profile. You will have one field for each language you activate in the "Localization" tab (see the next segment of this article). If you have more than one language enabled, your public profile will allow the viewer to switch between those languages via the links in the top right corner. 

You can choose the "Default overview style" for events on your public profile from the drop-down menu. Events will either be displayed in a list, a weekly overview, or a monthly overview. The list overview style is only available if your event series has 50 or less dates in the future. 
