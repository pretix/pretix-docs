# Dates

An event series contains dates.
Dates behave similar to individual events, but they are all part of an overarching event series.
This article explains how to add dates to an event series.

We will navigate to our personal dashboard by clicking :btn-icon:i-pretix: pretix.eu: in the top left corner of the website.
We will then select our event in the list of "Your upcoming events" and click :btn-icon:fa3-calendar: Dates: in the sidebar.
There are no dates in our event series yet.
Thus, this page displays the text "You haven't created any dates for this event series yet".
It also displays two buttons: one for creating a single new date, and one for creating many new dates.

## Creating a date for regular opening hours

First, we are going to create a date that represents our regular opening hours.
In order to do so, we will click the :btn-icon:fa3-plus: Create a new date: button.

In the "Name" field, we will enter `Regular admission`.
Under "Event start time", we will enter `2027-01-01`, `08:00:00`.
Under "Event end time", we will enter `2027-12-31`, `18:00:00`.

In the first field under "Quotas", we will enter "Regular admission".
We will leave the "Total capacity" field empty.
It makes no sense to limit the sale of tickets that attendees will use throughout an entire year.

Under "Products", we will not make a selection yet because we have not yet created any products.
We will then click the :btn:Save: button.

## Creating dates for special events

Next, we want to offer recurring guided tours for our museum.
Our guided tour takes place every Monday and Wednesday at 10 AM in the first half of 2027.
For that, we are going to create multiple new dates for this event series.
We will click the :btn-icon:fa3-plus: Create many new dates: button.

In the box titled "Repetition rule", we will choose the following:
"Repeat every `1` `week(s)`, starting at `2027-01-01`."
We will then check the boxes next to "Monday" and "Wednesday".
We will select the radio button next to "Repeat until" and choose the date `2027-06-30`.

![Page titled "Create multiple dates", displaying options for a repetition rule and times, as well as a preview of dates about to be created.](../assets/screens/event-series/create-multiple-example3.png "Create multiple dates example" )

The "Preview" on the right side of the page is useful for double-checking our repetition rule.
It will display the first ten and last ten dates we are about to create.

Under "Times", we will click the :btn-icon:fa3-plus: Add a single time slot: button.
We will choose the start time `10:00:00`, the end time `12:00:00` and the admission time `09:30:00`.

Under "General information", we will enter `Guided tour` as the name for these dates.

Finally, we will click the :btn: Save: button, which takes us back to the dates overview page.

## Conclusion

Now that we have added dates to our event series, we can move on to [creating products](products.md) to sell in our shop.