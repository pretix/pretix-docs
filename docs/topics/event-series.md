# Event series

When creating a new event, you can either create a singular event, or you can create an event series. 
This article explains the difference between a singular event and an event series, helps you decide which one to choose, and tells you how to set up an event series. 

## Prerequisites 

This article assumes that you have access to an organizer account, either because you created it yourself when you signed up on pretix.eu, or because you were invited and granted access by a co-organizer. 

## How To 

### When does it make sense to create an event series? 

The individual dates of an event series will always share the same settings, with the following exceptions: 

 - date and time 
 - location
 - text on the shop page 
 - product quotas 
 - check-in rules 

These parameters can be adjusted for each date individually. 

The main benefits of an event series over a singular event are the following: 

 - settings only have to be adjusted once and will apply to every single date in the series 
 - customers can order tickets for multiple dates at the same time via the same shop 

We recommend creating an event series use cases such as the following: 

 - a theater performing the same play on several nights 
 - a touring act playing the same concert in several different locations on different dates 
 - a workshop hosted in several different locations
 - an escape room allowing customers to book one of several time slots throughout the day 
 
We **do not** recommend creating an event series for the following use cases: 

 - events with large gaps of time between the individual dates, such as annual conferences. 
 Many parameters can change over the course of a year and attendees will typically only buy a ticket for the upcoming date. 
 - events that take place over the course of several days, such as conferences or festivals, if customers typically attend more than one day of the event. 
 

### How to create an event series 

Navigate to the dashboard. 
In the list titled "Your upcoming events", click the :btn-icon:fa3-plus:Create a new event: button. 
Under "Event type", select "Event series or time slot booking". 
The rest of the process is the same as the creation of a singular event. 
For more information on creating an event, see the tutorial section on [event creation](../tutorial/event.md). 

![Screenshot of page titled "Create new Event—Step 1", showing options for choosing an organizer account, the event type, and languages to be used.](../assets/screens/event/create-event1.png "Create new event step 1 screenshot" ) 

### Editing dates in the event series 

Navigate to :navpath:Your event series → :fa3-calendar: Dates:. 
This page displays the list of currently existing event dates and allows you to create, edit, clone and delete them.
In order to create a single new date for this event series, click :btn-icon:fa3-plus: Create a new date:. 

In order to create several new dates for this event series, click :btn-icon:fa3-plus: Create many new dates:. 


If “Dates” is missing from the navigation menu, you have insufficient permission or your event has not been set up as an event series and you need to create a new event.

If you click on one of them or create a new one, you will see the following form:

Here, you can make changes to the following fields, most of which are optional:

Name

    This is the public name of your date. It should be descriptive enough to tell the user which date to select in a calendar.
Active

    This date will only show up for customers if you check this box. In this sense, it corresponds to the “live” setting of events.
Event start time

    The date and time that this date starts at.
Event end time

    The date and time this date ends at.
Location

    This is the location of your date in a human-readable format. We will show this on the ticket shop frontpage, but it might also be used e.g. in Wallet tickets.
Admission time

    The admission date and time to show on the ticket shop page or on the tickets.
Frontpage text

    A text to show on the front page of the ticket shop for this date.
Start of presale

    If you set this, no ticket will be sold before the time you set. If you set this on event series level as well, both dates must be in the past for the tickets to be available.
End of presale

    If you set this, no ticket will be sold after the time you set. If you set this on event series level as well, both dates must be in the future for the tickets to be available.
Quotas

    As for all events, no tickets will be available unless there is a quota created for them that specifies the number of tickets available. You can create multiple quotas that are assigned to this date directly from this interface.
Item prices

    This is a table of all products configured for your shop. If you want, you can enter a new price for each one of them in the right column to make them cheaper or more expensive for this date. If you leave a field empty, the price will follow the product’s default price.


## Troubleshooting 

#### The button :fa3-calendar: Dates: does not appear in the sidebar on the left 

If the button :fa3-calendar: Dates: does not appear in the sidebar on the left, there are three possible explanations for this: 

 - you have selected the wrong event (a singular event instead of an event series)
 - the event is set up as a singular event instead of an event series
 - you do not have permission to edit dates for this event 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 
