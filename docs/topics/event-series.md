# Event series

When creating a new event, you can either create a singular event, or you can create an event series. 
This article explains the difference between a singular event and an event series, helps you decide which one to choose, and tells you how to set up an event series. 
An event series allows you to create multiple dates that are all part of the event series. 
You should create an event series if you are offering the same experience more than once at several different times. 
In all other cases, creating singular events should suffice. 

## Prerequisites 

This article assumes that you have access to an organizer account, either because you created it yourself when you signed up on pretix.eu, or because you were invited and granted access by a co-organizer. 

## How To 

### When does it make sense to create an event series? 

The question whether you are hosting one single event, multiple events, or an event series does not always have a clear-cut answer. 
pretix offers multiple solutions for each use case. 
This segment tells you how an event series behaves compared to singular events. 
It will help you decide whether you should create an event series, or if one or more singular events are more appropriate for your situation. 

An event series is useful if you are planning the same event to take place several times, with at most small variations. 

The individual dates of an event series will always share the same settings, with the following exceptions: 

 - date and time 
 - location
 - text on the shop page 
 - product quotas 
 - check-in rules 

These parameters can be adjusted for each date individually. 
The main benefits of an event series over several separate singular events are the following: 

 - settings only have to be adjusted once and will apply to every single date in the series 
 - customers can order tickets for multiple dates at the same time via the same shop 
 
We recommend creating an **event series** in use cases such as the following: 

 - a theater performing the same play on several nights 
 - a touring act playing the same concert in several different locations on different dates 
 - a workshop hosted in several different locations
 - an escape room allowing customers to book one of several time slots throughout the day 
 
We recommend creating **multiple independent** events for the following use cases: 

 - events with large gaps of time between the individual dates, such as annual conferences. 
 Many parameters can change over the course of a year and attendees will typically only buy a ticket for the upcoming date. 
 - events with no or only very little overlap in content 

 We recommend creating **one singular event** for the following use cases: 

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

## Troubleshooting 

#### The button :fa3-calendar: Dates: does not appear in the sidebar on the left 

If the button :fa3-calendar: Dates: does not appear in the sidebar on the left, there are three possible explanations for this: 

 - you have selected the wrong event (a singular event instead of an event series)
 - the event is set up as a singular event instead of an event series
 - you do not have permission to edit dates for this event 
