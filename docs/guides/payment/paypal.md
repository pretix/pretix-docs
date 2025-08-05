# PayPal

PayPal is one of the many options for handling payments within pretix. 
Stripe allows handling payments via the following methods: 
real-time payment via PayPal account, "Buy Now Pay Later" via PayPal account, SEPA direct debit, and alternative payment methods such as SOFORT, giropay, iDEAL, and others. 
This article tells you how to connect to your PayPal account and use it to receive payments via pretix. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 
Make sure you have an active PayPal business account. 
A regular PayPal account is **not** enough for integration with pretix. 
You can find [instructions on how to sign up for a PayPal business account](https://www.paypal.com/c2/webapps/mpp/how-to-guides/sign-up-business-account) on the PayPal website. 

## How To

Setting up PayPal as a payment provider in pretix involves the following steps: 

 1. Enable the PayPal plugin. 
 2. Connect to your PayPal business account 
 3. Enter mandatory info on the settings page for PayPal
 4. Make optional adjustments
 5. Enable payment via PayPal
 6. Test it 

This section will guide you through those steps in detail. 

Navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins:. 
Switch to the :btn:Payment providers: tab. 
This page displays the PayPal plugin at the top. 
It should be active by default. 
If it is active, it will have a green ":fa3-check: Active" tag, a white "Disable" button, and two drop-down menus. 
If it is **not** active, the tag will be missing and it will have a purple :btn:Enable: button. 
Verify that the plugin is active. 

![Payment settings page. The 'Payment providers' tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe. Gift card is enabled and all other entries are disabled. All entries have 'Settings' buttons next to them. The settings button for PayPal is highlighted.](../../assets/screens/payment-providers/payment-settings-paypal.png "Payment settings PayPal" )

You can jump straight to the PayPal settings by clicking the :btn-icon:fa3-gear: Settings: drop-down menu and then :btn:Payment > PayPal:. 

Alternatively, navigate to :navpath:Your Event → :fa3-wrench: Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
The list should now include an entry for PayPal with a red ":fa3-remove: Disabled" tag. 

The plugin is active, but you have not set up PayPal as a payment provider for the event yet. 
Click the :btn-icon:fa3-gear:Settings: button next to PayPal. 
This takes you to the settings page for PayPal, which currently only includes the :btn:Connect with PayPal: button. 
Click the button and complete the login and authorization process with PayPal. 

![PayPal website with the pretix logo in the top right and a dialog in the center telling you to 'Connect a PayPal account to start accepting payments on pretix GmbH'. You can enter your email and country or region below.](../../assets/screens/payment-providers/paypal-connect-account.png "Connecting to PayPal" )

After you have completed the authorization process with PayPal, the PayPal settings page in the pretix backend will look different. 
Instead of the single button, it will now offer a multitude of settings. 
The page will display your PayPal Merchant ID near the top. 

All settings here are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box next to "Enable payment method". 
PayPal and the other payment methods you enabled on this site will now appear as a payment option for customers in your shop. 
