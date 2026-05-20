# Custom domain

By default, you can access a shop built with pretix at a URL such as `https://pretix.eu/tut/tutcon27`.
This example uses our hosted service, so the domain is `pretix.eu`.
The organizer short form is `tut` and the event short form is `tutcon27`.

You can also use a custom domain for your tickets shops.
This article tells you how to set up a custom domain and how to enable it for your events.

## Prerequisites

You need to own the domain which you want to use as your custom domain.

Custom domains are set up on the organizer level.
You need access to an organizer account if you want to enable a custom domain.
You also need access to each event shop for which you want to use the custom domain.

## How to

The setup of custom domains depends on where your shops are hosted.
If you are using [pretix Hosted](#pretix-hosted), then we are hosting your shops for you at `pretix.eu`.
If you are using [pretix Enterprise or pretix Community]](#pretix-enterprise-and-pretix-community), then pretix is running  on your own server.
Refer to the subsection appropriate to your use case below.

### pretix Hosted

Navigate to :navpath:Your organizer → :fa3-wrench: Settings → Custom domain:.
This page displays a DNS record similar to the following:

**CNAME tut.cname.pretix.eu.**

This DNS record will be different for you.
Create a new **subdomain** with your domain registrar or DNS provider using the DNS record displayed here.
The exact process depends on your domain registrar or DNS provider.
Typically, the user interface will have a menu called "DNS entries", "DNS settings" or something similar.

As an alternative to the subdomain, you can also use your main domain for your pretix shop.
We recommend creating a `www.` subdomain and setting up a redirect from your main domain to that subdomain.

Wait for the changes to take place.
This may take a few minutes to a few hours.

Open the pretix backend and navigate to :navpath:Your organizer → :fa3-wrench: Settings → Custom domain:
In the "Domain name" field, enter the subdomain you just created.
Under "Domain usage", assign the domain one of three roles.

pretix will use the "Organizer main domain" for your organizer page as well as all events with no other domain specified.
pretix will use "Event domain" for a single event.
You can select the "Alternative domain for some of your events individually.
See section [Moving an event to an alternative domain](custom-domain.md#moving-an-event-to-an-alternative-domain) below for further information.

The events assigned to the alternative domain will appear on the alternative domain.
The organizer page will **not** appear on the alternative domain.
If a user attempts to navigate to your organizer account on the alternative domain, their browser will redirect them to the organizer main domain listing all events.

Once you have made your choices, click the :btn:Setup domain: button.
It may take a few minutes for the changes to take place.

### pretix Enterprise and pretix Community

If you are using pretix Enterprise or pretix Community, configure your webserver or reverse proxy to pass requests to the new domain to pretix.
The exact process depends on your setup.

Navigate to :navpath:Your organizer → :fa3-wrench: Settings: and open the :btn:Domains: tab.
Click the :btn-icon:fa3-plus: Add domain: button.
A new empty line will appear on the page.
In that new line, enter the name of the new domain in the "Domain name" field.

Select a mode for the new domain.
pretix will use the "Organizer domain" for your organizer page as well as all events with no other domain specified.
pretix will use the "Event domain" for a single event.
Specify an event in the "Event" field.
You can select the "Alternative organizer domain for a set of events" for some of your events individually.
See section [Moving an event to an alternative domain](custom-domain.md#moving-an-event-to-an-alternative-domain) below for further information.

The events assigned to the alternative domain will appear on the alternative domain.
The organizer page will **not** appear on the alternative domain.
If a user attempts to navigate to your organizer account on the alternative domain, their browser will redirect them to the organizer main domain listing all events.

Once you have made your choices, click the :btn:Setup domain: button.
It may take a few minutes for the changes to take place.

### Moving an event to an alternative domain

If you have set up a domain in "Alternative domain" mode (pretix Hosted) or in "Alternative organizer domain for a set of events" mode (pretix Enterprise and pretix Community), then you will have to move those events to the alternative domain.

In order to do so, navigate to :navpath:Your event → :fa3-wrench: Settings → General:.
On the :btn:Basics: tab, click the "Domain" drop-down menu.
The default setting is `Same as organizer account`.
Select your alternative domain from the list and click the :btn:Save: button.