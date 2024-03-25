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

Your input into the Contact address field will be displayed publicly to allow your customers to contact you. 

You can add an info text to your organizer account. The info text is not displayed anywhere by default, but you can use this in ticket templates if you want to.

## Organizer page 



Switching to the 'Organizer page' tab at the top lets you set a Header image, Homepage text, Default overview style for events, and Footer links for your organizer page. 

## Localization

On the Localization tab, you can choose which languages to make the shop available in. The options officially maintained by the pretix team are English, German, and German (informal). German uses "Sie" to address the user whereas German (informal) uses "Du". You can also choose one of the community translations for your organizer page. They are displayed in the list below along with a percentage of how much of the software is translated. English will be used as the fallback langauge for missing translations. Please choose a country or region from  the drop-down Region menu. We will use this to determine default date, time, address and phone number formatting. Please also choose a Default timezone from the drop-down menu with that title. 



!!! tip

    The profile page will be shown as ``https://pretix.eu/slug/`` where ``slug`` is to be replaced by the short form of
    the organizer name that you entered during account creation and ``pretix.eu`` is to be replaced by your
    installation's domain name if you are not using our hosted service.

    Instead, you can also use a custom domain for the profile page and your events, for example
    ``https://tickets.example.com/`` if ``example.com`` is a domain that you own.  Head to :ref:`custom_domain` to learn
    more.
