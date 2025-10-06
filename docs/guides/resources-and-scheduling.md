# Resources and scheduling

Your event schedule may not be based on time alone. 
It may also depend on the availability of guides, rooms, equipment, or other resources. 
The "Resources and scheduling" plugin allows you to manage those resources and schedule dates in your [event series](event-series.md) accordingly. 
This article tells you how to use it. 

## Prerequisites

You need to have at least one event series with which you want to use resources and scheduling. 
The plugin offers no useful features for singular events. 

## How To 

Using resources and scheduling involves the following steps: 

 1. Enabling the plugin on the organizer level
 2. Enabling the plugin on the event series level
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
Check the event series with which you want to use the plugin and click the :btn:Save: button. 

Alternatively, in order to enable the plugin for an individual event series, navigate to :navpath:Your event series → :fa3-wrench: Settings → Plugins:. 
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

Click the :btn:Save: button. 

### Managing properties 

Most resources are not interchangeable. 
They usually have one or multiple properties that vary from one to the next and which are relevant for booking. 
You can use the properties feature to keep track of these properties within pretix. 

In order to edit properties on a resource type, navigate to :navpath:Your organizer → :fa3-briefcase: Resources → Types:. 
Click the :btn-icon:fa3-edit:: edit button next to the resource type in the list. 
Under the headline "Properties", you can manage properties. 
Alternatively, you can add properties while creating a new resource type. 

Assume, for example, you are creating a property type for conference rooms. 
These conference rooms differ as to how many people they seat and whether or not they have a projector for presentations. 
The projectors also vary in terms of display resolution (either 1080p or 720p). 

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

If you are using the properties feature to keep track of guides, you could create properties such as language skills, expertise, or target audiences. 

### Managing individual resources 

After you have created a resource type and added properties to it, you can create individual resources. 
Every resource type you create adds a new submenu under :navpath:Your organizer → :fa3-briefcase: Resources:. 
Navigate to the submenu for the resource type you created in the previous step. 
For instance, if you created a resource type named "Guide", navigate to  :navpath:Your organizer → :fa3-briefcase: Resources → Guide:. 

Click the :btn-icon:fa3-plus: Add a Guide: button. 
If your resource has a different name, then the button will have a different label, too. 

If the resource you are creating represents a person, enter their name under "Name". 
Under "Locale", select the language spoken by the person. 
Under "Notification email address", enter their email address. 
Check the "Require confirmation" field. 

If the resource represents an inanimate object, enter the room number, inventory number, or another unique identifier. 
Select the "Locale" and Notification email address corresponding to the person or team in charge of the resource. 

Once you are happy with your choices, click :btn:Save and continue with more settings:. 

### Creating a product for scheduling 

Navigate to :Navpath:Your event series → :fa3-ticket:Products: and create or edit a personalized admission product. 
Do **not** add the product to any quotas. 
Open the :btn:Requirements: tab. 

In the "Default duration (minutes)" field, enter the time resources will typically be booked for. 
For instance, if a tour usually takes 45 minutes, enter `45`. 
In the "Default quota size" field, enter the maximum number of people that can use the resource at the same time. 
For instance, if a tour guide can accommodate no more than 30 people at a time, enter `30`. 

Click the :btn-icon:fa3-plus: Add a new requirement: button. 
Select the "Resource type" that this necessary for this date. 
Under "Property values", check all values that are required for this type of date. 

For instance, assume you are offering a tour of the Ancient Egypt for English-speaking children. 
In this case, you select the "Resource type" `Guide` and the "Property values" `Children`, `Egypt`, and `English`. 

Click the :btn:Save: button. 

### Creating dates for scheduling 

Navigate to :Navpath:Your event series → :fa3-calendar:Products: and click the :btn-icon:fa3-plus: Create many new dates: button. 
Set up the dates according to your preferences. 
For general information on creating dates, see [Creating and editing dates in the event series](event-series.md#creating-and-editing-dates-in-the-event-series). 

Under the heading "Quotas", in the field labeled "Products", select the product you created in the [previous step](resources-and-scheduling.md#creating-a-product-for-scheduling). 
Do **not** select any other products. 
