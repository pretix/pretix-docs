# Custom check-in rules

You can use custom check-in rules to place restrictions on the validity of tickets based on time, number of previous entries, ticket type, gate, and other conditions. 
pretixSCAN will interpret these custom rules when scanning the ticket and arrive at the correct result automatically. 


## Prerequisites

This article assumes that you have read [check-in lists](check-in-lists.md) and set up one or more basic check-in lists. 

## General usage

In order to add custom rules to a check-in list, navigate to :navpath:Your event → :fa3-check-square-o: Check-in:. 
Click the change button :btn-icon:fa3-wrench:: next to the check-in list you want to edit. 

By default, pretixSCAN will recognize any ticket on the check-in list as valid as long as the ticket has been paid for and either the ticket has not been scanned before, or the ticket has been scanned and then scanned for exit. 
The exact behavior depends on your settings on the :btn:General: and btn:Advanced: tabs on this page. 

If you want to place additional restrictions on a ticket being recognized as valid by pretixSCAN, set up a custom check-in rule. 
In order to do so, under "Custom check-in rule", on the :btn-icon:fa3-edit: Edit: tab, click the :btn-icon:fa3-plus-circle: Add condition: button. 
A dropdown menu appears, listing types of conditions. 

### Organizing conditions with AND- and OR-brackets

The most important types of conditions are `All of the conditions below (AND)` and `At least one of the conditions below (OR)`. 
What separates these two from all other conditions is that they allow you to organize conditions into a complex logic for the check-in. 
Adding one of these two conditions creates an AND-bracket or an OR-bracket to which you can add more conditions. 

If you select `All of the conditions below (AND)` from the dropdown menu and add conditions to the resulting AND-bracket, then all of those conditions must be fulfilled for pretixSCAN to recognize the ticket recognized as valid. 

If you select `At least one of the conditions below (OR)` and add conditions to the resulting OR-bracket, then at least one of those conditions must be fulfilled for pretixSCAN to recognize the ticket as valid. 
If multiple or even all conditions within the OR-bracket are fulfilled, then the ticket will still be recognized as valid. 

This may be counter-intuitive. 
The condition `At least one of the conditions below (OR)` in this feature is an [inclusive or](https://en.wikipedia.org/wiki/Logical_disjunction). 
This is distinct from an [exclusive or](https://en.wikipedia.org/wiki/Exclusive_or), also known as XOR ("either one or the other"). 
The custom check-in rule feature does not offer an "exclusive or" condition because its use would be very limited. 

You can create an AND- or an OR-bracket around an existing condition by clicking :btn:OR: or :btn:AND: next to the condition. 
When hovering the mouse over several nested brackets, AND-brackets will be highlighted in red, OR-brackets in green, and other conditions in purple. 

### Adding a simple condition 

All conditions **except** `All of the conditions below (AND)` and `At least one of the conditions below (OR)` are simple conditions. 
Your custom check-in rule could consist of only a single of these simple conditions. 
If you need to set up more than one condition, then you need to organize these conditions using AND- and OR-conditions. 

Select a condition from the dropdown menu, for instance, `Current day of the week (1 = Monday, 7 = Sunday)`. 
The page now displays an additional dropdown menu listing mathematical symbols for "equals", "greater than", "smaller than or equal to" and so on. 
Select a symbol, for example, `<`. 
The page now displays an additional field in which you can enter a number. 
Enter a number, for example, `6`. 
Click the :btn:Save: button. 

If you set up a condition as described in the example, then pretixSCAN will only recognize a ticket as valid if the current day of the week is less than 6, or in other words, only Monday through Friday. 
Tickets will be rejected if scanned on Saturday or Sunday. 

## Applications 

This section guides you through some useful applications of custom check-in rules. 

### Allowing multiple entries per ticket 

If you are offering tickets that can be used multiple times, then you need to set up a custom check-in rule that allows multiple entries. 

Create an AND-bracket and add a condition within that bracket. 
Select `Product`, then `is one of`, and then choose the products in question. 
Add another condition, select `Number of previous entries` and then `<`.
Enter the number of total entries you want to allow, for instance, `10`. 

If your check-in list also contains products that the condition above does not include, then the page will now display an information box listing those products. 
The logic now only allows entry for one type of product. 

![Custom check-in rule allowing entry if 'Product' 'is one of' 'Season ticket' AND 'Number of previous entries' '<' '9'. There is a blue infobox saying: 'Your rule always filters by product or variation, but the following products or variations are not contained in any of your rule parts so people with these tickets will not get in: Standard ticket, Discount ticket. Please double-check if this was intentional.](../../assets/screens/check-in/multiple-infobox.png "Custom check-in rule for multiple entries with infobox")

In order to solve this problem, you need to add conditions that include the other tickets. 
Click the :btn:OR: button in the top right. 
This creates an OR-bracket around the conditions you previously created. 

Click the :btn-icon:fa3-plus-circle: Add condition: button that is located within the OR-bracket, but not within the AND-bracket. 
Select `All of the conditions below (AND)` and add another condition directly below. 
Select `Product`, then `is one of`, and then choose those products that the rule above does not cover. 
Add another condition immediately below. 
Select `Number of previous entries`, then `=`, and then `0`.

![Custom check-in rule allowing entry if 'Product' 'is one of' 'Season ticket' AND 'Number of previous entries' '<' '9', or if 'Product' 'is one of' 'Standard ticket' or 'Discount ticket' AND 'Number of previous entries' '=' '0'. ](../../assets/screens/check-in/multiple-full.png "Full custom check-in rule for multiple entries")

With this setup, pretixSCAN will recognize a product called "Season ticket" as valid as long as it has been used to enter less than ten times. 
This allows up to ten uses of the ticket. 
pretixSCAN will recognize the products "Standard ticket" and "Discount ticket" if they have been used 0 times, so only once in total. 

![Visualization of custom check-in rule with two paths. The first path has 'Product: Season ticket' and 'Number of previous entries < 10'. The second path has 'Product: Standard ticket, discount ticket' and 'Number of previous entries = 0'. Both paths end with green checkmarks.](../../assets/screens/check-in/multiple-visualization.png "Visualization of full custom check-in rule for multiple entries")

