# Testing and Going Live

In this final part of the tutorial, we will test our shop, make sure that everything works as intended, and finally take it live. 
Here is a brief overview of the steps we are going to take in this section: 

 - [placing an order](testing.md#testing-and-confirming-orders) in test mode 
 - reviewing the order in the backend and marking it as paid
 - testing the shop in every language we have activated
 - [making final improvements](testing.md#making-final-improvements-to-our-shop) to our shop if necessary 
 - [disabling test mode](testing.md#disabling-test-mode-and-deleting-orders) and deleting test orders 
 - [taking the shop live](testing.md#conclusion)

## Testing and confirming orders 

![Our shop page, titled 'Tutorial conference', listing date and location for our event and a selection of products. There is a box warning that the shop is currently in test mode.](../assets/screens/testing/shop.png "Shop screenshot") 

We will now place an order in our shop. 
We are going to click the :btn-icon:fa3-eye:Go to shop: button in the bar at the top. 

This takes us to the shop which should currently have a red bar at the top stating that it is only visible to us and our team, and a yellow box warning that it is in test mode. 
We will now place an order for a standard ticket and a discount ticket, follow the instructions on the screen, and enter an email address that we have access to when prompted. 

During checkout, we will choose credit card as the payment method, which should currently display a note stating that the Stripe plugin is operating in test mode. 
We will use the credit card data for one of the test cards [listed by Stripe](https://docs.stripe.com/testing#cards) to issue a fake payment for our order. 

We will now open pretix.eu, navigate to our event, and click :btn-icon:fa3-shopping-cart: Orders: in the sidebar. 
This page displays a list of orders. 
If our test has been successful, the list now contains the test order we just placed. 
The order should have the status ":fa3-check: Paid". 

We are going to repeat this process for every language we have activated for the shop. 
This is to make sure that we have provided all the necessary translations and our localization settings are correct. 

## Making final improvements to our shop 

By trying out the shop and getting the same view as our customers, it will become obvious if we have made any mistakes or forgotten anything while setting up our event. 
We may need to add texts, images, new products, questions, checks, or fine-tune the appearance of the shop. 

It is possible to adjust these things when the shop is already live. 
However, we are going to make sure that our shop is exactly in the state we want it to be in before we take it live so that all of our customers have a unified and flawless experience while using it. 

## Disabling test mode and deleting orders 

![Page titled 'Shop status', displaying a box warning about which conditions are not met yet for the shop to go live and options to disable test mode and delete all test mode orders.](../assets/screens/testing/shop-status.png "Shop status screenshot") 

To make sure that only real orders from actual customers appear in our shop from this point onwards, we have to delete the orders we just placed in test mode. 
For that, we will navigate to our event and click the :btn-icon:fa3-exclamation-triangle: TEST MODE: entry in the sidebar which is highlighted in orange. 
We will check the box labeled "Permanently delete all orders created in test mode" and click the :btn:Disable test mode: button. 

## Conclusion 

Once the experience in our shop is satisfactory and all other points have been checked off the list above, we can finally take our shop live. 
In order to do that, we are going to navigate to :navpath:Event → Dashboard:. 

The event dashboard displays a box saying "Your ticket shop is not yet public. Click here to change". 
Clicking that box takes us to the "Shop status" page. 
We are going to click the :btn:Go live: button and our ticket shop will finally go live! 