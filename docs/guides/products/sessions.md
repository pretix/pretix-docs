
# Sessions

Your event may be made up of several smaller events ("sessions") with more limited capacities, with attendees being able to pick and choose which of these sessions they want to attend. 
If you are planning a conference with multiple workshops, a celebration with a variety of activities, or a similar event, you may need a way to control access to those sessions. 
pretix offers you several methods to do this: simply adding a mandatory question to be asked with every order, add-on products with fixed time slots, or a plugin with advanced functions for variable time slots. 
This article will guide you through all three of them. 

If your event's schedule is small and straightforward, all sessions are included in the basic admission price, and you do not need to keep track of who attends which session, you should use [questions](sessions.md#option-a-questions). 

If your event's schedule is large, you have deviating prices for some of the sessions, or each session can only be attended by a number of limited people, you should use [add-on products](sessions.md#option-b-add-on-products-with-fixed-time-slots). 

If the conditions above apply and you also have sessions with varying start and end times that cannot be neatly organized into time slots because of overlap, you should use the [agenda constraints plugin](sessions.md#option-c-add-on-products-with-variable-time-slots). 

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

For illustrative purposes, assume you are hosting a conference with workshops that can only be attended by a maximum of 20 people. 
The schedule looks like this: 

| Time                | Room A     | Room B                         |
|---------------------|------------|--------------------------------|
| Wednesday morning   | Lecture    |                                |
| Wednesday afternoon | Workshop A | Workshop B                     |
| Thursday morning    | Workshop C | Workshop D (€20 additional charge) |

In addition to the basic admission products for this conference, you also have to create the following products: 

 - A category called "Workshops" with the box next to "Products in this category are add-on products" checked
 - A free product called "Wednesday afternoon" in the "Workshops" category with two variations:
     - Workshop A
     - Workshop B
 - A product called "Thursday morning" in the "Workshops" category with with two variations:
     - Workshop C (free)
     - Workshop D (€20)
 - One quota for each additional product (workshop), each with a total capacity of 20 

After you have created these categories, products, and quotas, edit your basic admission tickets and open the :btn:Add-ons: tab. 
Add an add-on from the "Workshops" category with "Minimum number" of 0 and a "Maximum number" of 2 and click the :btn:Save: button. 
This enables your customers to choose which of the workshops they want to attend. 
It also allows you to track planned attendance numbers through the quotas for each workshop. 

## Option C: Add-on products with variable time slots

<!-- md:hosted -->

If the sessions at your event have overlapping start and end times and cannot be neatly organized into time slots, you can solve this issue with the "Agenda constraints" plugin. 
One example for a schedule which would necessitate the use of the agenda constraints plugin is the following: 

| Time        | Room A                  | Room B                   |
|-------------|-------------------------|--------------------------|
| 09:00-11:00 | Talk 1                  | Workshop 1 (first half)  |
| 11:00-13:00 | Talk 2                  | Workshop 1 (second half) |
| 14:00-16:00 | Workshop 2 (first half) | Talk 3                   |
| 16:00-18:00 | Workshop 2 (second half | Talk 4                   |

In this example, Workshops 1 and 2 are twice as long as the talks. 
Thus, it makes no sense to implement this schedule with add-on products as described under [option B](sessions.md#option-b-add-on-products-with-fixed-time-slots). 
This would either result in customers having to book each half of the workshops individually, or in allowing them to book combinations of overlapping sessions which they cannot attend. 
You can handle more complicated schedules like this one with the agenda constraints plugin. 

In order to activate that plugin, navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and open the :btn:Features: tab. 
Seek out the "Agenda constraints" plugin in the list and click the :btn:Enable: button next to it. 

Create a category for session tickets and check the box next to "Products in this category are add-on products". 
Create a product for each individual session, add it to the sessions category and switch to the :btn:Additional settings: tab. 
Use the fields "Start date" and "End date" to define the span of time in which the session is taking place. 
Create a quota for each of those products, with the total capacity of the quota reflecting the maximum number of attendants for each session. 

Edit the basic admission tickets for your event and open the :btn:Add-ons: tab. 
Add an add-on from the sessions category with "Minimum number" of 0 and a "Maximum number" equal to or greater than the largest possible number of workshops a guest can attend. 
Click the :btn:Save: button. 

This enables your customers to choose which of the workshops they want to attend. 
The "Start date" and "End date" you defined for each add-on product will restrict which combinations of sessions your customers can book. 
You can track planned attendance numbers through the quotas for each workshop. 
You can also 

!!! Note

    The agenda constraints plugin is currently only available on pretix Hosted. 
    If you are interested in using it with pretix Enterprise, please contact sales@pretix.eu.
