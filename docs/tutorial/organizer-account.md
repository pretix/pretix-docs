# Organizer account

An organizer account represents an entity that is running events, for example a company, an institution. or you yourself. You have already created an organizer account when you created your personal account - or, if you were invited to pretix by a co-organizer, then accepting that invitation has already given you (partial) access to an organizer account. 


![pretix.eu dashboard, showing upcoming events, a button for creating a new event, the mail address of the account currently logged in, and a sidebar with the following options: Dashboard, Events, Organizers, Search, User settings, Reports, Shipping list](../../assets/screens/account/dashboard.png)

After finishing account creation and logging in to [pretix.eu/control](https://pretix.eu/control/), you are greeted by the dashboard. Click the :btn:Organizers: button in the sidebar to get to the Organizers page. 

![pretix.eu organizers page, showing the list of available organizer accounts which only includes 'Awesome Event Corporation'. There is a filter function for the list of organizers and a button labeled 'Create a new organizer'](../../assets/screens/organizer/organizers.png) 

Clicking your organizer account in the list takes you to a page displaying all events associated with that organizer. 

![pretix.eu organizers page, showing the list of all events associated with 'Awesome Event Corporation'. There is a filter function for the list of events and a button labeled 'Create a new event'](../../assets/screens/organizer/event-list.png) 

The basis of all your operations within pretix is your organizer account. It represents an entity that is running
events, for example a company, yourself or any other institution.
Every event belongs to one organizer account and events within the same organizer account are assumed to belong together
in some sense, whereas events in different organizer accounts are completely isolated.

If you want to use the hosted pretix service, you can create an organizer account on our [Get started](https://pretix.eu/about/en/setup) page. Otherwise,
ask your pretix administrator for access to an organizer account.

You can find out all organizer accounts you have access to by going to your global dashboard (click on the pretix logo
in the top-left corner) and then select "Organizers" from the navigation bar on the left side. Then, choose one of the
organizer accounts presented, if there are multiple of them:

![Organizer list](../../assets/screens/organizer/list.png)

This overview shows you all event that belong to the organizer and you have access to:

![Event list](../../assets/screens/organizer/event_list.png)

With the "Edit" button at the top, next to the organizer account name, you can modify properties of the organizer
account such as its name and display settings for the public profile page of the organizer account:

![Edit organizer](../../assets/screens/organizer/edit.png)

!!! tip

    The profile page will be shown as ``https://pretix.eu/slug/`` where ``slug`` is to be replaced by the short form of
    the organizer name that you entered during account creation and ``pretix.eu`` is to be replaced by your
    installation's domain name if you are not using our hosted service.

    Instead, you can also use a custom domain for the profile page and your events, for example
    ``https://tickets.example.com/`` if ``example.com`` is a domain that you own.  Head to :ref:`custom_domain` to learn
    more.
