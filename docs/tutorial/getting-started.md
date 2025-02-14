# Getting Started

Welcome to the pretix tutorial! 
In this tutorial, we will go through all the necessary steps for hosting our very first event using pretix.
For illustrative purposes, we will create a straightforward conference. 
We will use specific examples for our organizer, event, products, as well as the names and prices thereof. 
Feel free to replace these examples with your own as you create your event according to your needs. 

pretix is open source software and can be used either in the cloud or on your own server.
Running pretix on your own server requires in-depth technical knowledge and is described on our [Administrator documentation](https://docs.pretix.eu/en/latest/admin/index.html).
This page focuses on the easier way to use our cloud-based pretix Hosted offering.
If you have pretix installed on your server, you can directly skip to the next chapter.

Here is a brief overview of the steps we are going to take in this tutorial: 

 - creating a personal and [organizer account](getting-started.md#creating-an-account)
 - setting up our [organizer account](organizer-account.md) 
 - creating our [event](event.md) 
 - creating [products](products.md) (tickets and merchandise) for our event 
 - setting up [payment](payment.md) methods
 - [testing](testing.md) our shop and making final adjustments 

## Creating an account

Before we are able to do anything with pretix, we have to create an account. 
Good news: creating an account is __completely free__ of charge and does not come with any obligation to pay money for the use of pretix in the future. 
We are free to play around with the pretix software to our heart's content before deciding whether pretix is the right choice for us. 
Costs will only occur when selling actual tickets.

!!! Note

    If your company, association or institution already has an organizer account, it is not necessary to create a new account. 
    Instead, you can ask your co-organizers to send you an invitation and add you to the team. 
    Instructions on inviting someone to a team can be found  [here](../topics/teams.md#inviting-someone-to-your-team). 

![pretix.eu, a website introducing pretix and its main features. There is a green button labeled 'Create your first ticket shop' on the right.](../assets/screens/account/pretix-eu.png "pretix.eu screenshot" ) 

To create an account, we are going to click the green :btn:Create you first ticket shop: button on the [pretix.eu website](https://pretix.eu/about/en/ "https://pretix.eu/about/en").
This takes us to a site on which we will enter the info for our personal pretix account in the left column, and the name and short form for our organization in the right column. 

<br>

![a website with input fields for account information as well as the name and short form of the organizer](../assets/screens/account/pretix-create-account.png "pretix.eu/about/en/setup screenshot" ) 

For our personal account, we are going to provide our name, email address, and a secure password. 
The field on the top left is meant for the name of the person to whom the account belongs, **not** for a company name. 
We are going to choose a name by which our co-organizers will recognize us and which our support team can use to address us. 
For this tutorial, our name is going to be Jordan Doe.

Everyone should have their own personal login.
If other members of our team should have access to the system as well, we will be able to [invite](../topics/teams.md#inviting-someone-to-your-team) them later in the process.


!!! Warning

    The **short form** is the unique identifier for your company in our website's backend and will also be used in the shop URL. 
    Please put careful consideration into the short form and make sure you are happy with it.

    The short form **cannot be changed** without you contacting customer support. 
    It might no longer be possible to change it at all if you have already set up some parts of the system.

The "Full name" field is meant for the name of the company, association, or institution for which we want to organize events. 
The "Address short form" field is for a short form of the organization's name. 
This short form will be used for the URL under which our events can be found. 

For this tutorial, we are going to create an account for our Tutorial Ltd. 
So we will enter "Tutorial Ltd." into the full name field, and "tut" into the address short form field. 
This means that our organizer's profile and all the events we are going to create will be found at [https://pretix.eu/tut/](https://pretix.eu/tut/) from now on. 

There is no need to create a dedicated test account or use the word "test" anywhere in the short form or name. 
pretix offers a test mode that allows our organizer and events to remain invisible to the public, but still gives us access to all functions and settings. 

By using the official name of our organization for the account right away, we can ensure that we get to use our preferred URL. 
We can also avoid having to make the same adjustments to two different accounts. 
Our events will not be visible to the public, nor will we be charged, until we decide to take them live. 

{% include "note-short-form.md" %}

The [privacy policy](https://pretix.eu/about/en/privacy) and [terms of service](https://pretix.eu/about/en/terms) are both linked on this page. 
Reading them carefully, agreeing with them and checking the boxes to confirm is a requirement for using pretix. 

We will now click the :btn:Continue: button and thus take our first step towards hosting our first event using pretix. 
Next, we are going to set up our [organizer account](organizer-account.md). 
