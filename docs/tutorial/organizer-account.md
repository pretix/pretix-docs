# Organizer account

An organizer account represents an entity that is running events, for example a company, an institution, or yourself. You have already created an organizer account when you created your personal account—or, if you were invited to pretix by a member of your team, then accepting that invitation has already given you (partial) access to an organizer account. 

This section of the tutorial tells you how to customize your organizer account and add necessary information to it. 

You may not yet be able to make a final decision for every single question that comes up in this section of the tutorial. Some of the questions will only become relevant once you have created your first event with pretix. But that's not a problem at all. You can always go back to these settings and change them later. 

We still recommend reading this article and going through the organizer account settings before doing anything else because it will save you some work in the long run. For example, organizer-level language and design settings will be used as the default for any events you create in the future. 

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

After saving the general settings, switch to the "Localization" tab. We recommend changing localization settings __before__ changing any settings on the "Organizer page" tab because the localization settings determine which customizations are available there. 

Under "Available languages", you can choose which languages your ticket shop will be published in. The options officially maintained by the pretix team are English, German, and German (informal). German uses "Sie" to address the user whereas German (informal) uses "Du". You can also choose one of the community translations for your organizer page. They are displayed in the list below along with a percentage of how much of the software is translated. English is used as the fallback langauge for missing translations. 

This setting also determines the default languages when creating new events, though languages can be activated or deactivated for each event individually.

!!! Note 

    pretix offers many settings and customizations where you input your own text, for example, the description on the organizer page, the name of your events, and so on. You will need to provide a translation in every language you choose here for each individual item. This can amount to a lot of work. We recommend using no more than two or three languages at a time unless you are working with dedicated translators. 

Choose a country or region from  the drop-down "Region" menu. The selection will be used to determine default date, time, address and phone number formatting. The language chosen above will take a higher priority than the region. 

Also choose a "Default timezone" from the drop-down menu with that title. 

## Organizer page 

Switching to the "Organizer page" tab at the top allows you to add content to the public profile of your organizer. You can take a look at the public profile by clicking the :btn👁 Public profile: button in the bar at the top. It is located at https://pretix.eu/awesome-corp/, where "awesome-corp" is replaced with your organizer short form. 

![Organizer settings page, on the organizer page tab, showing the following options: Header image, Use header image in its full size, Use header image also for events without an individually uploaded logo, Homepage text (in multiple languages). The "Public profile" button in the top bar is highlighted.](../../assets/screens/organizer/organizer-page-public-profile.png) 

By default, the name of the organizer  will be displayed in the page header of your public profile. The organizer page settings allow you to replace the name with an image, that is, your logo. It should be a .png or .jpg file with a resolution of 1140 × 120 pixels or smaller. You can add the header image by clicking the :btn:Browse...: button next to the "Header image" option and choosing the image file to upload from your computer. 

In the "Homepage text" fields, you can provide text to be displayed on your public profile. You will have one field for each language you activate in the "Localization" tab (see the next segment of this article). If you have more than one language enabled, your public profile will allow the viewer to switch between those languages via the links in the top right corner. 

You can choose the "Default overview style" for events on your public profile from the drop-down menu. Events will either be displayed in a list, a weekly overview, or a monthly overview. The list overview style is only available if your event series has 50 or less dates in the future. 

## Shop design 

Switch to the "Shop design" tab. Here, you can customize the colors and font used for your public profile and the ticket shops you're going to create. You can change the colors so that they're in line with the palette you use for your other media. Please heed the notice underneath the input fields and pick a different color if contrast is too low. 

You can also choose your preferred font from the list. If you're creating a ticket shop in a language that doesn't use the Latin alphabet, you should choose a font that supports the writing system you need. All available fonts support the Latin alphabet. The preview should give you an idea which writing systems each font supports. So for example, if you're creating a ticket shop in a language that uses the Cyrillic alphabet, you should pick a font such as DejaVu Sans or Noto Sans. 

## Customer accounts 

Switch to the "Customer accounts" tab. By default, all boxes on this page should be unchecked. If you don't plan for your customers to create accounts, you can leave them unchecked and you don't have to take any action on this tab. 

pretix offers some features that only work with customer accounts. If you want to offer your customers memberships that give them access to reduced price offers or members-only products, then you have to enable customer accounts. If you expect your customers to repeatedly log in to your shop and make purchases through the same account, then you have to enable customer accounts. You can enable customer accounts by checking the "Allow customers to create accounts" box at the top of the page. 

Checking that box makes another box appear that is checked by default: "Allow customers to log in with email address and password". Keep this box checked if you want customers to log in to your pretix ticket shop directly. Uncheck it if you want them to log in via an external sign-on service. You'll have to enable the corresponding plugin on the event level. 

## Gift cards 

The gift cards tab lets you make organizer-level settings for gift cards. You can choose how many years gift cards are valid for. This field is empty by default, meaning gift cards will be valid in your shop indefinitely. You can also choose how long the gift card codes are. The default is 12 digits and you can leave this as it is unless you have a specific reason. 

## Privacy 

On the "Privacy" tab, please provide an URL pointing to your privacy policy for each language you activated. The default dialog text and button labels for the cookie consent banner should already be filled out. Feel free to edit or replace these as you see fit. 

pretix itself only ever sets cookies that are required to provide the service requested by the user or to maintain an appropriate level of security. Therefore, cookies set by pretix itself do not require consent in all jurisdictions that we are aware of. The settings on the "Privacy" tab will only have an effect if you use plugins that require additional cookies and participate in our cookie consent mechanism.

Ultimately, it is your responsibility to make sure you comply with all relevant laws. We try to help by providing these settings, but we cannot assume liability since we do not know the exact configuration of your pretix usage, the legal details in your specific jurisdiction, or the agreements you have with third parties such as payment or tracking providers.

## Reusable media 

Reusable media are currently an experimental feature. We recommend that you do not enable reusable media unless you have a specific use case in mind. Please contact us if you intend to use reusable media for your event. 

## Invoices 

On the "Invoices" tab, you can choose whether you want to "Allow to update existing invoices". By default, invoices are immutable once they have been issued. For most jurisdictions, we recommend leaving this option turned off and always issuing a new invoice if a change needs to be made. Please seek legal advice regarding this issue before you check the "Allow to update existing invoices" box. 