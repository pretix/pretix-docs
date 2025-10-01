# Resources and scheduling

The resources and scheduling feature allows you to manage resources such as guides, rooms, or equipment, and schedule events accordingly. 
This article tells you how to do that.  

## Prerequisites

You need to have at least one event or event series with which you want to use resources and scheduling. 

## How To 

Using resources and scheduling involves the following steps: 

 1. Enabling the plugin on the organizer level
 2. Enabling the plugin on the event level
 3. Creating resource types
 4. Creating properties for resource types
 5. ????
 6. Profit

### Enabling the plugin 

In order to enable the plugin for your organizer, navigate to :navpath:Your organizer → :fa3-wrench: Settings → Plugins:. 
Search the "Resources and Scheduling" plugin in the list and click the :btn:Enable: button. 
If the "Resources and Scheduling" plugin is already active, then it will have a green ":fa3-check: Active" tag next to it. 
In that case, click the :btn:Manage events: button. 

Both buttons take you to a page listing the organizer's events. 
Check the events with which you want to use the plugin and click the :btn:Save: button. 

Alternatively, in order to enable the plugin for an individual event, navigate to :navpath:Your event → :fa3-wrench: Settings → Plugins:. 
Search the "Resources and Scheduling" plugin in the list and click the :btn:Enable: button. 
If the plugin is already active, then it will have a green ":fa3-check: Active" tag next to it. 

### Creating resource types

Before you can create and manage individual resources, you have to create resource types. 
A resource type may, for example, represent the following: 

 - personnel such as guides, instructors, supervisors, etc. 
 - facilities such as specialized rooms, sports courts, theater halls, etc. 
 - equipment such as audio guides, film screening equipment, pedal boats, etc. 

You can use pretix to manage any kind of resource and create a resource type for it. 
You should create **exactly one** resource type for every type of resource that you want to manage. 

In order to create a new resource type, navigate to :navpath:Your organizer → :fa3-briefcase: Resources → Types:. 
Enter a "Name" for the resource. 

If you do not enter a "Plural name", then pretix will append an `s` to the "Name" for the plural. 
If the plural of your resource type's name is not formed by appending an `s` to the end, specify a "Plural name". 
For instance, if your resource type is named `person`, enter `people` in the "Plural name" field. 

pretix will send the email under "Booking pending confirmation" to you if a customer books a resource of the type. 
pretix will send the email under "Booking confirmed" to a customer after you have confirmed a booking through the previous email. 
Adapt the subject and message text of both emails to your liking. 

### Managing properties 

On the page "Create a new resource type", under the headline "Properties", you can manage properties. 
A property is any property that varies between individual resources and which may be relevant for booking your resource. 

Assume, for example, you are creating a property type for conference rooms. 
These conference rooms differ as to how many people they seat and whether or not they have a projector for presentations. 
The projectors also vary in terms of display resolution. 

In this case, you click the :btn-icon:fa3-plus: Add property: button. 
Under "Name", enter `Seats`. 
Under "value", enter `8`. 
Click the :btn-icon:fa3-plus: Add new value: button and enter `12` in the new field. 
Click the same button again and enter `20` in the new field. 
Your resource type "conference room" now has the "Seats" property which can be `8`, `12`, or `20`. 

Click the :btn-icon:fa3-plus: Add property: button. 
Under "Name", enter `Projector`. 
Under "value", enter `1080p`. 
Click the :btn-icon:fa3-plus: Add new value: button and enter `720p` in the new field. 
Click the same button again and enter `None` in the new field. 
Your resource type "conference room" now has the "Projector" property which can be `1080p`, `720p`, or `None`. 


## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the subject? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant guides, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 