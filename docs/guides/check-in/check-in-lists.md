# Check-In Lists 

This article tells you how to create, configure, and use check-in lists. 
Check-in lists keep track of who attends your event. 
In most cases, you need one check-in list for every separate entrance at your event. 
If there is one venue with multiple entrances, then one shared check-in list is enough. 
If you have separate entrances for separate products, such as fast lane access or VIP tickets, then you will need one check-in list for every entrance. 

Check-in lists operate independently from one another. 
A ticket is valid once on every check-in list that includes it. 
If you are hosting subevents with more exclusive attendance, then each of those subevents will need its own check-in list. 

We recommend using the pretixSCAN app running on dedicated devices for your check-in. 
It is by far the most convenient method. 
You can also do a manual check-in through the backend, or you can print your lists and check people in with a pen and paper. 

## Prerequisites 

Check-in lists are handled on the event level, so you have to create an event first. 

## General usage 

This section explains how to set up and configure check-in lists. 

## Applications

This section explains how you can use check-in lists to manage the check-in at your event. 

### Check-in via pretixSCAN

The most convenient and powerful method for checking in customers is using the pretixSCAN app. 
Acquire a device with a scanner or camera, install pretixSCAN on it, connect it to your organizer account, and place it at the entrance to your event. 
We will cover the specifics of using pretixSCAN in a dedicated article. 

### Paper check-in 

!!! Note 
    This method is slow and only feasible if you are dealing with a low volume of customers. 
    We recommend using pretixSCAN instead. 

If you want to print a check-in list, navigate to :navpath:Your event: → :fa3-check-square-o: Check-in → Check-in lists:. 
In the list, click the check-in list you want to print. 
On the next page, click the :btn-icon:fa3-download: PDF: button. 

Alternatively, navigate to :navpath:Your event: → :fa3-shopping-cart: Orders → Export: and click :btn:Check-in list (PDF):. 

Regardless of which path you take, you will land on a page titled "Data export – Check-in List (PDF)". 
Under "Check-in list", select the list you want to export. 
You can use the settings on this page to filter and sort the file export by certain parameters. 
If you want to use the export for manual check-in, then you probably want an alphabetical list of all ticket holders. 
Select the "Check-in status" "All attendees" and "Sort by" one of the attendee name options. 

Under "Include questions", select any questions that are relevant for check-in. 
Once you are satisfied with your settings, click the :btn-icon:fa3-download: Start export: button. 
Your browser will now download a PDF of the list or open it in a new tab. 
The list includes the following columns: 

 - a column containing a double exclamation mark ‼ for products that require special attention. 
 This cell is empty for products that do **not** have the "Requires special attention" setting activated. 
 - a box for checking off tickets. 
 This box will be checked for tickets that were already checked in before you exported the list. 
 - "Paid" contains a check for orders that have been paid. 
 - "Order" contains the order code. 
 - "Name" contains the attendee's name. 
 - "Product / Price" contains the name of the product and the price in parentheses. 
 - optional columns for questions you chose to include in the export 

Print the exported list, place it at your check-in, and check entries off the list manually as visitors appear. 
This method is slow and only feasible if you are dealing with a low volume of customers. 
We recommend using pretixSCAN instead. 

### Manual check-in via backend 

!!! Note 
    This method is slow and only feasible if you are dealing with a low volume of customers. 
    We recommend using pretixSCAN instead. 

If you want to perform manual checks using the pretix backend, place a computer at the check-in. 
You will need a stable internet connection and the ability to access the pretix backend from that computer. 
Take appropriate security measures so that only authorized personnel can use the computer. 

On that computer, open the pretix backend and navigate to :navpath:Your event: → :fa3-check-square-o: Check-in → Check-in lists:. 
In the list, click the check-in list on which you want to record check-ins. 
The next page displays a list with all issued tickets. 

Ask attendees their name, email address, ticket code, or order code. 
Use the "Search attendee" function or browse the list to locate the corresponding entry. 
Check the box next to that entry and click the :btn-icon:fa3-sign-in: Check-In selected attendees (#): button. 
It is possible to select multiple attendees and check them all in at once. 
