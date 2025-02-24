
# Sessions

Your event may be made up of several smaller events ("sessions") with more limited capacities, with attendees being able to pick and choose which of these sessions they want to attend. 
If you are planning a conference with multiple workshops, a celebration with a variety of activities, or a similar event, you may need a way to control access to those sessions. 
pretix offers you several methods to do this: simply adding a mandatory question to be asked with every order, add-on products with fixed time slots, or a plugin with advanced functions for variable time slots. 
This article will guide you through all three of them. 

If you are not planning sessions that all take place within the scope of one big main event, but for a series of events that can be attended individually, refer to our article on [event series](../event-series.md) instead. 

## Option A: Questions

If you are only offering a limited number of sessions and are not faced with a realistic risk of overcrowding in any of them, you can create a multiple-choice question. 
Customers will be prompted to answer this question while placing their order. 
This has the upside of making it easy for users to change their mind later on. 
It can also be set up fairly quickly. 
However, it will not allow you to restrict the number of attendees signing up for a given session. 
It will also not allow you to charge extra for any of the sessions. 

In order to set up a question, navigate to :navpath:Event → :fa3-ticket: Products → Questions: and click the :btn:fa3-plus:Create a new question: button. 
Under "Question", add text for each language that your shop uses. 
This text will be displayed to the customer while they are making their purchase. 
The "Question" could read something like: "Which workshop do you want to attend in the 10 AM time slot?" 

For "Question type", select "Choose one from a list". 
For "Products", select every product during the purchase of which the question should be asked—typically, this wil apply to any basic admission product for your event. 
If you check the box next to "Required question", then your customers will be forced to make a choice here.
Your ticket shop will not allow them to proceed without making a selection. 
Click :btn-icon:fa3-plus:Add a new option: and add an answer option for each session that is going to be offered at your event. 

## Option B: Add-on products with fixed time slots

If the selection of sessions offered at your event is more complex than described in the previous section, you should use add-on products instead of questions. 
This makes sense if you are working with space constraints at your venue or if you want to charge more for some of the sessions. 
First, create at least one basic admission products for your event and a category for add-on products. 
Then, create new product for your first time slot. 
Add it to the add-on category you just created, select "Product with multiple variations" and set the price to zero. 
Open the "Variations" tab and create one variation for each session taking place within that time slot. 
Repeat these steps for each time slot and session at your event. 

Let's take for example the following conference schedule, in which the lecture can be attended by anyone, but the workshops only have space for 20 persons each:

| Time                | Room A     | Room B                         |
|---------------------|------------|--------------------------------|
| Wednesday morning   | Lecture    |                                |
| Wednesday afternoon | Workshop A | Workshop B                     |
| Thursday morning    | Workshop C | Workshop D (20 € extra charge) |

Assuming you already created one or more products for your general conference admission, we suggest that you additionally create:

 - A category called "Workshops" with the checkbox "Products in this category are add-on products" activated
 - A free product called "Wednesday afternoon" within the category "Workshops" and with two variations:
     - Workshop A
     - Workshop B
 - A free product called "Thursday morning" within the category "Workshops" and with two variations:
     - Workshop C
     - Workshop D with a price of 20 €
 - Four quotas for each of the workshops
 - One add-on configuration on your base product that allows users to choose between 0 and 2 products from the category "Workshops"

## Option C: Add-on products with variable time slots

The above option only works if your conference uses fixed time slots and every workshop uses exactly one time slot. 
If your schedule looks like this, it's not going to work great:

| Time        | Room A                  | Room B                   |
|-------------|-------------------------|--------------------------|
| 09:00-11:00 | Talk 1                  | Workshop 1 (first half)  |
| 11:00-13:00 | Talk 2                  | Workshop 1 (second half) |
| 14:00-16:00 | Workshop 2 (first half) | Talk 3                   |
| 16:00-18:00 | Workshop 2 (second half | Talk 4                   |

This issue can be solved with the "Agenda constraints" plugin. 
In order to activate that plugin, navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and open the :btn:Features: tab. 
Seek out the "Agenda constraints" plugin in the list and click the :btn:Enable: button next to it. 

Then, create a product (without variations) for every single part that should be bookable (talks 1-4 and long workshops 1 and 2) as well as appropriate quotas for each of them.

All of these products should be part of the same category. 
In your base product (e.g. your conference ticket), you can then create an add-on product configuration allowing users to add products from this category.

If you edit these products, you will be able to enter the "Start date" and "End date" of the talk or workshop close to the bottom of the page. 
If you fill in these values, pretix will automatically ensure no overlapping talks are booked.

!!! Note

    This option is currently only available on pretix Hosted. 
    If you are interested in using it with pretix Enterprise, please contact sales@pretix.eu.

