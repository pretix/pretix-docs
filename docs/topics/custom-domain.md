# Custom domain 

By default, a shop built with pretix can be accessed at an URL such as `https://pretix.eu/tut/tutcon27`. 
This example uses our hosted service, so the domain is `pretix.eu`. 
The organizer short form is `tut` and the event short form is `tutcon27`. 

You can also use a custom domain for your tickets shops. 
This article tells you how to set up a custom domain and how to enable it for your events. 

## Prerequisites

You need to own the domain which you want to use as your custom domain. 

Custom domains are set up on the organizer level. 
You need access to an organizer account if you want to enable customer accounts. 
You also need access to each event shop for which you want to use the custom domain. 

## How To 

The setup of custom domains depends on whether you are using pretix Hosted and your shops are hosted at pretix.eu; or you have installed pretix on your own server (pretix Enterprise or pretix Community). 
Please refer to the subsection appropriate to your use case below. 

### pretix Hosted 

Create a new subdomain with your domain registrar or DNS provider. 
Use the following DNS record: 

`CNAME  tut.cname.pretix.eu` 

Wait for the changes to take place. 
This may take a few minutes or a few hours. 
The exact process on your domain registrar or DNS provider. 

Navigate to :navpath:Your organizer → :fa3-wrench: Settings → Custom domain:. 
In the "Domain name" field, enter the subdomain you just created. 
Under "Domain usage", assign the domain one of three roles. 

The "Organizer main domain" will be used used for your organizer page as well as all events with no other domain specified.
The "Event domain" will be used for a single event. 
The "Alternative domain" can be selected for some of your events individually.
The events assigned to the alternative domain will be displayed on the alternative domain. 
The organizer page will not be displayed on the alternative domain. 

Once you have made your choices, click the :btn:Setup domain: button. 
It may take a few minutes for the changes to take place. 

### pretix Enterprise and pretix Community 

If you use pretix Enterprise or pretix Community, configure your webserver or reverse proxy to pass requests to the new domain to pretix. 
The exact process depends on your setup. 

Navigate to :navpath:Your organizer → :fa3-wrench: Settings: and open the :btn:Domains: tab. 
Click the :btn-icon:fa3-plus: Add domain: button. 
A new empty line will appear on the page. 
In that new line, enter the name of the new domain in the "Domain name" field. 

Select a mode for the new domain. 
The "Organizer domain" will be used used for your organizer page as well as all events with no other domain specified.
The "Event domain" will be used for a single event. 
You will have to specify an event in the "Event" field. 
The "Alternative organizer domain for a set of events" can be selected for some of your events individually.
The events assigned to the alternative domain will be displayed on the alternative domain. 
The organizer page will not be displayed on the alternative domain. 

### Moving an event to a different domain 

In order to move an event to a different domain, navigate to :navpath:Your event: → :fa3-wrench: Settings → General:. 
On the :btn:Basics: tab, click the "Domain" drop-down menu. 
The default setting is "Same as organizer account". 
Select your preferred domain from the list and click the :btn:Save: button. 