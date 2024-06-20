# Organizer account

An organizer account represents an entity that is running events, for example a company, an institution, or a person. 
We just created an organizer account when we created your personal account. 
It is also possible to gain (partial) access to an organizer account by being invited to pretix by a team member and accepting that invitation. 

In this section of the tutorial, we will customize our organizer account and add necessary information to it. 
This entails: 

 - navigating to the organizer account settings 
 - adding contact information on the "general" tab
 - choosing language and localization options on the "localization" tab 
 - customizing your organizer page on the "organizer page" and "shop design" tabs
 - enabling customer accounts for certain features on the "customer accounts" tab
 - setting up cookie/privacy information on the "privacy" tab 
 - getting our pretix account activated by providing necessary information in the "billing settings"

Those are the necessary steps for getting our organizer account up and running so that we can use it to host events using pretix. 
It also includes a few optional steps that will save us some work in the long run. 
For instance, organizer-level language and design settings will be used as the default for any events we are going to create in the future. 
We can always come back to the organizer account settings later and adapt them, should our needs change. 

## Navigating to the organizer account settings 

![pretix.eu dashboard, showing upcoming events, a button for creating a new event, the mail address of the account currently logged in, and a sidebar with the following options: Dashboard, Events, Organizers, Search, User settings, Reports, Shipping list](../assets/screens/account/dashboard.png)

After finishing account creation and logging in to [pretix.eu/control](https://pretix.eu/control/), you are greeted by the dashboard. 
Click the :btn:Organizers: button in the sidebar to get to the Organizers page. 

![pretix.eu organizers page, showing the list of available organizer accounts which only includes 'Example Organizer'. 
There is a filter function for the list of organizers and a button labeled 'Create a new organizer'](../assets/screens/organizer/organizers.png) 

Clicking your organizer account in the list takes you to a page displaying all events associated with that organizer. 

![pretix.eu organizers page, showing the list of all events associated with 'Example Organizer'. 
There is a filter function for the list of events and a button labeled 'Create a new event'](../assets/screens/organizer/event-list.png) 

Click :btn:Settings: in the sidebar to set up your organizer account. 
This lands you on the general settings page for the organizer account. 

## General 

![Organizer settings page, on the general tab, showing the following options: Name, Short form, Imprint URL, Contact address, Info text. 
Not pictured: 'Allow creating a new team during event creation' option, 'Save' button](../assets/screens/organizer/general-settings.png) 

The fields for "name" and "short form" are already filled out. 
It is not possible to change the short form since it is the organizer's unique identifier. 

If you are operating from Germany, it is recommended that you enter the URL to your website's imprint in the "Imprint URL" field. 

Enter a valid email address into the "contact address" field. 
This email address will be displayed publicly to allow your customers to contact you. 

Confirm your changes by clicking the :btn:Save: button on the bottom of the page. 

## Localization 

![Organizer settings page, on the localization tab, showing the official language options English, German, and German (informal) as well as a list of community translations from Arabic to Polish](../assets/screens/organizer/localization.png) 

After saving the general settings, switch to the "localization" tab. 
We recommend changing localization settings __before__ changing any settings on the "organizer page" tab because the localization settings determine which customizations are available there. 

Under "available languages", you can choose which languages your ticket shop will be published in. 
The options officially maintained by the pretix team are English, German, and German (informal). 
German uses "Sie" to address the user whereas German (informal) uses "du". 
You can also choose one of the community translations for your organizer page. 
They are displayed in the list below along with a percentage of how much of the software is translated. 
English is used as the fallback language for missing translations. 

This setting also determines the default languages when creating new events, though languages can be activated or deactivated for each event individually.

{% include "note-translations.md" %}

Choose a country or region from  the drop-down "region" menu. 
The selection will be used to determine default date, time, address and phone number formatting. 
The language chosen above will take a higher priority than the region. 

Also choose a "default timezone" from the drop-down menu with that title. 

## Organizer page 

![Organizer settings page, on the organizer page tab, showing an upload button and options for the header image as well as fields for the homepage text in English and German](../assets/screens/organizer/organizer-page.png) 

Switching to the "organizer page" tab at the top allows you to add content to the public profile of your organizer. 
You can take a look at the public profile by clicking the :btn:👁 Public profile: button in the bar at the top. 
Our public profile is located at https://pretix.eu/ex-org/. 
You can find yours by replacing "ex-org" with your organizer short form in that URL. 

![Organizer settings page, on the organizer page tab, showing the following options: Header image, Use header image in its full size, Use header image also for events without an individually uploaded logo, Homepage text (in multiple languages). 
The "public profile" button in the top bar is highlighted.](../assets/screens/organizer/organizer-page-public-profile.png) 

By default, the name of the organizer  will be displayed in the page header of your public profile. 
The organizer page settings allow you to replace the name with an image that tells your customers who is hosting the event (e.g., by means of your company name, logo, or recognizable design). 
It should be a .png or .jpg file with a resolution of 1140 × 120 pixels or smaller. 
You can add the header image by clicking the :btn:Browse...: button next to the "header image" option and choosing the image file to upload from your computer. 

In the "homepage text" fields, you can provide text to be displayed on your public profile. 
You will have one field for each language you activate in the "localization" tab (see the "localization" segment of this article). 
If you have more than one language enabled, your public profile will allow the viewer to switch between those languages via the links in the top right corner. 

You can choose the "default overview style" for events on your public profile from the drop-down menu. 
Events will either be displayed in a list, a weekly overview, or a monthly overview. 
The list overview style is only available if your event series has 50 or less dates in the future. 

## Shop design 

![Organizer settings page, on the shop design tab, showing options for colors and fonts to be used on the public profile of the organizer](../assets/screens/organizer/shop-design.png) 

Switch to the "shop design" tab. 
Here, you can customize the colors and font used for your public profile and the ticket shops you are going to create. 
You can change the colors so that they're in line with the palette you use for your other media. 
Please heed the notice underneath the input fields and pick a different color if contrast is too low. 

You can also choose your preferred font from the list. 
If you're creating a ticket shop in a language that doesn't use the Latin alphabet, you should choose a font that supports the writing system you need. 
All available fonts support the Latin alphabet. 
The preview should give you an idea which writing systems each font supports. 
So for example, if you're creating a ticket shop in a language that uses the Cyrillic alphabet, you should pick a font such as DejaVu Sans or Noto Sans. 

The shop design you set here will be the default for all shops you create for your events in the future. 
You can make individual adjustments to the event shops. 

## Privacy 

![Organizer settings page, on the privacy tab, showing input fields for the URLs to a privacy policy in different languages, a large blue box with legal info, and prefilled text fields for the privacy settings dialog](../assets/screens/organizer/privacy.png) 

On the "privacy" tab, please provide an URL pointing to your privacy policy for each language you activated. 
The default dialog text and button labels for the cookie consent banner should already be filled out. 
Feel free to edit or replace these as you see fit. 

pretix itself only ever sets cookies that are required to provide the service requested by the user or to maintain an appropriate level of security. 
Therefore, cookies set by pretix itself do not require consent in all jurisdictions that we are aware of. 
The settings on the "privacy" tab will only have an effect if you use plugins that require additional cookies and participate in our cookie consent mechanism.

Ultimately, it is your responsibility to make sure you comply with all relevant laws. 
We try to help by providing these settings, but we cannot assume liability since we do not know the exact configuration of your pretix usage, the legal details in your specific jurisdiction, or the agreements you have with third parties such as payment or tracking providers.

## Activation

Before any of your ticket shops can go live, your organizer account has to be activated. 
Your account is reviewed manually by our team as soon as you have provided all necessary information for correspondence and billing.

Navigate to [Your Organizer]→"Settings"→"Billing settings". 
The topmost field on the "general" tab is labeled "primary contact person". 
Enter the name of a real person (e.g. you or a coworker) we can contact if there is an issue with your account. 
Enter their email address and phone number in the fields below.

Enter the full contact details of your company further down on the page. 
If your company is located in the EU but outside of Germany, we recommend entering a VAT ID. 
If you do not provide your VAT ID here, we will need to charge you VAT on our services and we will not be able to issue reverse charge invoices. 
Again, this only applies if your company is located in the EU but outside of Germany. 

You can choose a preferred language of correspondence. 
We offer service in English and German.

Choose your preferred method of payment. 
You may pay by SEPA direct debit, by invoice, or by credit card. 
If you want to pay by SEPA direct debit, fill out your bank details in the form below and approve the mandate. 
If you want to pay by credit card, fill out your credit card information and authorize credit card payments to rami.io GmbH. 
If you are planning on only offering free tickets, you don't have to provide any further information here.

Once you are happy with your choices, click the :btn:Save: button. 
The page will notify you if any required information is still missing. 
If you have provided all required information, a green checkmark will appear at the top of the page with the message "Your changes have been saved." This means that your organizer account has been submitted to our team for review and will be activated shortly.

The "billing contact" and "privacy contact" tabs allow you to provide different contacts within your organization for billing and privacy matters. 
This is completely optional. 
You only need to fill out the information on the "general" tab of the billing settings to get your account approved. 