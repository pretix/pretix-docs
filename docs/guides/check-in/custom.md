# Custom check-in rules

You can use custom check-in rules to place restrictions on the validity of tickets based on time, number of previous entries, ticket type, gate, and other conditions. 
pretixSCAN will interpret these custom rules when scanning the ticket and arrive at the correct result automatically. 


## Prerequisites

This article assumes that you have read [check-in lists](check-in-lists.md) and set up one or more basic check-in lists. 

## How To 

In order to add custom rules to a check-in list, navigate to :navpath:Your event → :fa3-check-square-o: Check-in:. 
Click the change button :btn-icon:fa3-wrench:: next to the check-in list you want to edit. 

By default, pretixSCAN will recognize any ticket on the check-in list as valid as long as the ticket has been paid for and either the ticket has not been scanned before, or the ticket has been scanned and then scanned for exit. 
The exact behavior depends on your settings on the :btn:General: and btn:Advanced: tabs on this page. 

If you want to place additional restrictions on a ticket being recognized as valid by pretixSCAN, set up a custom check-in rule. 
In order to do so, under "Custom check-in rule", on the :btn-icon:fa3-edit: Edit: tab, click the :btn-icon:fa3-plus-circle: Add condition: button. 
A dropdown menu appears, listing types of conditions. 

### AND- and OR-brackets

The most important types of conditions are "All of the conditions below (AND)" and "At least one of the conditions below (OR)". 
What separates these two from all other conditions is that they allow you to organize conditions into a complex logic for the check-in. 
Adding one of these two conditions creates an AND-bracket or an OR-bracket to which you can add more conditions. 

If you select "All of the conditions below (AND)" from the dropdown menu and add conditions to the resulting AND-bracket, then all of those conditions must be fulfilled for pretixSCAN to recognize the ticket recognized as valid. 

If you select "At least one of the conditions below (OR)" and add conditions to the resulting OR-bracket, then at least one of those conditions must be fulfilled for pretixSCAN to recognize the ticket as valid. 
If multiple or even all conditions within the OR-bracket are fulfilled, then the ticket will still be recognized as valid. 

This may be counter-intuitive. 
The condition "At least one of the conditions below (OR)" in this feature is an [inclusive or](https://en.wikipedia.org/wiki/Logical_disjunction). 
This is distinct from an [exclusive or](https://en.wikipedia.org/wiki/Exclusive_or), also known as XOR ("either one or the other"). 
The custom check-in rule feature does not offer an "exclusive or" condition because its use would be very limited. 