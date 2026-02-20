# Event series

When creating a new event, you can either create a singular event, or you can create an event series. 
This article explains the difference between a singular event and an event series, helps you decide which one to choose, and tells you how to set up an event series. 

An event series allows you to create multiple dates that are all part of the event series. 
You should create an event series if you want your customers to book time slots, or if you want them to be able to buy tickets for multiple different dates by placing a single order. 
In all other cases, creating singular events should suffice. 

!!! Note 
    You do **not** need to create an event series for the following use cases: 

     - events that last more than one day, such as conferences or festivals
     - events with large gaps of time between the individual dates, such as annual conferences 
     - events with very little overlap in terms of name, schedule, and venue

    We recommend creating singular events in these cases because they are less complex to set up. 

## Prerequisites 

This article assumes that you have access to an organizer account, either because you created it yourself when you signed up on pretix.eu, or because you were invited and granted access by a co-organizer. 

## How to 

The question whether you are hosting one single event, multiple events, or an event series does not always have a clear-cut answer. 
It is possible that there is more than one sensible solution for your use case. 
The next section tells you how an event series behaves compared to singular events. 
It will help you decide whether you should create an event series, or if singular events are more appropriate for your situation. 

### When does it make sense to create an event series? 

Creating an event series makes sense if you are hosting many events in quick succession. 
You should create an event series if you want your customers to be able to buy tickets for multiple dates by placing a single order. 
You should also create an event series if you want your customers to book time slots. 

If you create an event series with multiple dates, then any setting you adjust will apply to every single date in the series. 
All dates that are part of the series will be displayed to customers on a single shop page. 

The individual dates of an event series will always share the same settings, with the following exceptions: 

 - event title 
 - date and time 
 - location
 - front page text
 - prices 
 - seating plan
 - product quotas 
 - check-in rules 

These settings can be adjusted for each individual date, but you can also create several dates with unified settings in a single step. 
For more information, see [Creating and editing dates in the event series](#creating-and-editing-dates-in-the-event-series). 

We recommend creating an **event series** in use cases such as the following: 

 - a theater performing different plays multiple times in the same venue 
 - a touring act playing the same concert in several different locations
 - workshops with limited capacity hosted several times
 - an escape room allowing customers to book a time slot 
 - a museum offering guided tours

There are some situations in which an event series is not the most straightforward solution. 
We recommend creating **singular events** for the following use cases: 

 - events that take place over the course of several days, such as conferences or festivals, if customers typically attend more than one day of the event. 
 This can be solved more easily using different products and check-in rules.
 - events with large gaps of time between the individual dates, such as annual conferences 
 - events with very little overlap in terms of organizational parameters 

### How to create an event series 

Navigate to the dashboard. 
In the list titled "Your upcoming events", click the :btn-icon:fa3-plus:Create a new event: button. 
Under "Event type", select "Event series or time slot booking". 
The rest of the process is the same as the creation of a singular event. 
For more information on creating an event, see the tutorial page on [event creation](../tutorial/event.md). 

![Page titled "Create new Event—Step 1", showing options for choosing an organizer account, the event type, and languages to be used.](../assets/screens/event/create-event1.png "Create new event step 1 screenshot" ) 

### Creating and editing dates in the event series 

Navigate to :navpath:Your event series → :fa3-calendar: Dates:. 
This page displays the list of currently existing event dates and allows you to create, edit, clone and delete them.

![Page titled "Dates", displaying buttons for creating a single or multiple new dates. ](../assets/screens/event-series/dates.png "Dates screenshot" ) 

In order to create a single new date for this event series, click :btn-icon:fa3-plus: Create a new date:. 
Choose a name, an event start time, and at least one product for the date. 
Once you are happy with your choices for the mandatory settings and the many optional settings on the page, click the :btn:Save: button. 
You will be taken back to the dates overview page titled "Dates". 
The date you just created is now displayed in the list on this page. 

In order to create several new dates for this event series, click :btn-icon:fa3-plus: Create many new dates:. 
The process is very similar to creating a single date. 
It is illustrated in the example below. 

![Page titled "Create multiple dates", displaying options for a repetition rule and times, as well as a preview of dates about to be created. ](../assets/screens/event-series/create-multiple-example.png "Create multiple dates example" ) 

As a practical example, let us assume you are offering an event titled "Sales workshop" every Monday and Wednesday at 10 AM in the second half of the year 2025. 
In the box titled "Repetition rule", you would make the following choice: 
"Repeat every 1 week(s), starting at 2025-07-01." 
Check the boxes next to the day of the week when the dates take place, "Monday" and "Wednesday" for example. 
Select the radio button next to "Repeat until" and choose a date such as 2025-12-31. 

The "Preview" on the right side of the page is useful for double-checking the repetition rule. 
It will display the first ten and last ten dates you are about to create. 

Under "Times", click the :btn-icon:fa3-plus: Add a single time slot: button. 
Choose the start time for your event, for example, 10:00:00. 
Optionally, you may choose an event end time such as 12:00:00 and an admission time such as 09:30:00. 

Under "General information", enter a name descriptive name for these dates in the "Name" field, "Sales workshop" for example. 
Under "Quotas", choose the product that shall grant admission to these dates in the "Products" field. 

Once you have taken these steps and made your optional choices, click the :btn:Save: button. 
You will be taken back to the dates overview page titled "Dates". 
If your venue closes on Christmas Eve and New Year's Eve, check the boxes next to those dates, scroll to the bottom of the page and click the :btn-icon:fa3-trash: Delete selected (2): button. 

## Troubleshooting 

### The button :fa3-calendar: Dates: does not appear in the sidebar on the left 

If the button :btn-icon:fa3-calendar: Dates: does not appear in the sidebar on the left, there are three possible explanations for this: 

 - you have selected the wrong event (a singular event instead of an event series)
 - the event is set up as a singular event instead of an event series
 - you do not have permission to edit dates for this event 

### Date names are not displayed 

If date names are not displayed in your shop's date overview, then that means that all dates names are the same. 
Create an additional date or set of dates with a different name. 
Date names will be displayed in the overview if there are dates with at least two different names. 