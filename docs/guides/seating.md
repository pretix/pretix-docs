# Seating

The seating feature of pretix allows you to sell tickets for individual seats. 
This is useful if, for example. your event is taking place at a theater, a stadium, or a dining hall. 
This article tells you how to create seating plans and how to implement them for your event. 

Customers will be able to look at the seating plan and choose their preferred seat. 

## Prerequisites

Many aspects of seating are handled on the event level, so you need to create an event first. 

## How to

If you want to sell tickets based on individual seats for your event, you need to take the following steps: 

 - [Enabling the plugin](#enabling-the-plugin) 
 - Using the seating plan editor to [create a layout](#creating-a-layout)
 - [Creating an entry for the seating plan](#creating-an-entry-for-a-seating-plan) in your organizer account
 - [Creating products for seating](#creating-products-for-seating)

The following sections will guide you through those steps in detail. 

### Enabling the plugin

In order to enable the "Seating" plugin for your event, navigate to :navpath:Your organizer → :fa3-wrench: Settings → Plugins: and open the :btn:Features: tab. 
The Seating plugin is included as a "Top recommendation" at the top of the page. 
Click the :btn:Enable: button next to it. 
Check the events for which you want to use seating plans in the list labeled "Events with active plugin". 
Now that you have enabled the seating plugin, all settings associated with seating are available for your organizer. 

### Creating a layout 

The central component of any seating plan is the JSON file defining the layout. 
In order to create a new layout, open the editor at [https://seats.pretix.eu/](https://seats.pretix.eu/). 
You can use this editor without being logged in to a pretix account. 

Alternatively, navigate to :navpath:Your organizer → :i-seat: Seating plans: and click the :btn-icon:fa3-plus: Create a new seating plan: button. 
On the next page, click the :btn-icon:fa3-external-link: Go to editor: button. 
This also takes you to [https://seats.pretix.eu/](https://seats.pretix.eu/). 

If you have an image file depicting a plan of your venue, that image can be helpful for creating the layout. 
If you want to do so, set the "Width" and "Height" to the resolution of the image. 
Then, click the :btn:UPLOAD IMAGE: button and select the file. 

In order to zoom in and out of the layout, hold the Ctrl key and move your mouse wheel. 
Alternatively, you can use the buttons :btn-icon:fa3-search-minus:: and :btn-icon:fa3-search-plus:: in the top bar. 

In order to move the view around, hold the Ctrl key, click the layout, and move your mouse. 

In order to edit an existing element, click "Select rows or shapes" in the top bar. 
If you want to select individual seats, click "Select seats" instead. 
Click the element. 
If you want to select multiple elements, hold the Shift key while clicking them. 
Alternatively, hold the left mouse button and move the mouse to draw a selection rectangle around them. 

In order to move selected elements, drag and drop them with the mouse or use the arrow keys. 
Use the Shift key for bigger movements and the Alt key for smaller movements. 
If you want to align elements to the grid, hold the Ctrl key while moving them. 

The editor will validate your layout. 
It will warn you if there are duplicate seat numbers or row numbers. 

Copying rows may create duplicate seat numbers. 
Change the row number of the row you copied. 
Then, activate the "Reversed" toggle and deactivate it again. 
This refreshes seat numbers so that there will be no more duplicates in that row. 

In order to save the layout, click the :btn-icon:fa3-save:: button in the top left. 
This opens a dialog allowing you to save the resulting JSON file on your computer. 

### Creating an entry for a seating plan

Seating plans are handled on the organizer level. 
This allows you to use seating plans for multiple events hosted by the same organizer. 

After you have [created a layout](#creating-a-layout) in the form of a JSON file, you create a corresponding entry for a seating plan in your organizer account. 
In order to do so, navigate to :navpath:Your organizer → :i-seat: Seating plans: and click the :btn-icon:fa3-plus: Create a new seating plan: button. 

On the next page, click the :btn-icon:fa3-upload: Upload layout: button. 
Select the JSON file you created and downloaded in the previous step. 
This fills the "Layout" field with the contents of the file. 

Enter a name for the seating plan in the "Name" field and click the :btn:Save: button. 
You will land on a page titled "Seating plans", displaying a button for creating another new seating plan, and a list including the plan you just created. 

### Creating products for seating 



## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further information

What other media do we have on the subject? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See also 

Link to other relevant guides, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 