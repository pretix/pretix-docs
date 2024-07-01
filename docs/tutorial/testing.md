# Testing and Going Live

In this final part of the tutorial, we will test our shop, make sure that everything works as intended, and finally take it live. 

## Activating the fake payment provider for testing

!!! Warning 
    The fake payment provider is for test purposes only. 
    Make absolutely sure that it is disabled before taking the shop live. 
    Otherwise, it will allow your customers to place orders without paying for them. 
    Do not enable the fake payment provider while your ticket shop is live. 

We want to test the functionality that is central to our shop: placing an order. 
We first need to activate the fake payment method by navigating to [Event] → "Settings" → "Plugins" and opening the "payment providers" tab. 
We will search for the "fake payment providers" plugin in the list and enable it. 
We will then browse to [Event] → "Settings" → "Payment". 
The list should now contain the entry "FAKE PAYMENT Credit card FOR DEMONSTRATION ONLY". 
We will click the :btn:⚙ Settings: button next to that entry, check the boxes next to "I have understood that this payment method is fake and doesn't actually collect payments" and "enable payment method" and click :btn:Save:. 

## Testing and confirming orders 

We will now place an order in our shop using the fake payment method. 
We are going to click the :btn:👁 Go to shop: button in the bar at the top. 
This takes us to the shop which should currently have a red bar at the top stating that it is only visible to us and our team, and a yellow box warning that it is in test mode. 
This is the way it is intended. 
We would not want to activate the fake payment provider while the shop is already live and accessible to the public. 
We will now place an order for a standard ticket and a discount ticket and follow the instructions on the screen. 

During checkout, the option to pay by credit card will appear twice. 
One of these credit cards is our fake payment provider. 
The fake payment provider has the credit card number already filled out with repeating sequences of "42". 
We are going to use this to place our order. 
We will also place an order of a speaker ticket. 

We will now open pretix.eu and navigate to [Event] → "Orders". 
This page should display a list containing the two test orders we just placed. 
The first order should have the status "paid" and the second order, which includes the speaker ticket, should have the status "approval pending". 

We will click the code for the second order, then the :btn:Approve: button and confirm our choice. 
This will send an email to the address we used to place the order containing a link under which any pending payment can be completed. 
The order will now display the "pending" tag in the overview. 
If we open the link in the email and use the fake payment provider, that status will change to "paid". 

We are going to repeat this process for every language we have activated for the shop. 
This is to make sure that we have provided all the necessary translations and our localization settings are correct. 

## Making final improvements to our shop 

By trying out the shop and getting the same view as our customers, it will become obvious if we have made any mistakes or forgotten anything while setting up our event. 
We may need to add texts, images, new products, questions, checks, or fine-tune the appearance of the shop. 
It is possible to adjust these things when the shop is already live. 
However, we are going to make sure that our shop is exactly in the state we want it to be in before we take it live so that all of our customers have a unified and flawless experience while using it. 

## Deactivating the fake payment provider 

It is absolutely vital to deactivate the fake payment provider before going live. 
In order to do that, we will navigate to [Event] → "Settings" → "Payment" and click on the  :btn:⚙ Settings: button next to "FAKE PAYMENT Credit card FOR DEMONSTRATION ONLY". 
We will uncheck the "enable payment method" box and click :btn:Save:. 
If we now visit our shop and place an order, the "credit card" payment option corresponding to the fake payment provider will not appear anymore. 

## Disabling test mode and deleting orders 

To make sure that only real orders from actual customers appear in our shop from this point onwards, we have to delete the orders we just placed in test mode. 
For that, we will navigate to [Event] → "TEST MODE". 
We will check the box labeled "permanently delete all orders created in test mode" and click the :btn:Disable test mode: button. 

## Checklist before going live 

We should be able to confidently answer the following questions with "yes" before the shop can go live: 

 - Does the shop look and function the way we want it to? 
 - Have the contact details under "billing settings" been filled out? 
 - Has the organizer account been activated by the pretix team? 
 - Has the fake payment provider been disabled? 
 - Have all test mode orders been deleted? 

## Conclusion 

Once the experience in our shop is satisfactory and all other points have been checked off the list above, we can finally take our shop live. 
In order to do that, we are going to browse to [Event] → "Dashboard". 
The event dashboard displays a box saying "Your ticket shop is not yet public. Click here to change". 
Clicking that box takes us to the "shop status" page. 
We are going to click the :btn:Go live: button and our ticket shop will finally go live! 
