# PayPal

PayPal is one of the many options for handling payments within pretix. 
This article is going to tell you how to connect to your PayPal account and use it to receive payments via pretix. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 
Make sure you have an active PayPal business account. 
A regular PayPal account is not enough for integration with pretix. 
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

Navigate to [Your Event] → "Settings" → "Plugins". 
Switch to the "payment providers" tab. 
The PayPal plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green "✓ Active" tag and a white :btn:Disable: button. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 
Make sure that the plugin is enabled. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them. The settings button for PayPal is highlighted.](../../assets/screens/payment-providers/payment-settings-paypal.png "Payment settings PayPal" )

Navigate to [Your Event] → "Settings" → "Payment". 
The "payment providers" tab on this page displays the list of active payment providers. 
The list should now include an entry for PayPal with a red "❌ Disabled" tag. 
The plugin is enabled, but PayPal has not been set up and enabled as a payment provider for the event yet. 
Click on the :btn:⚙ Settings: button next to PayPal. 
This takes you to the settings page for PayPal, which currently only includes the :btn:Connect with PayPal: button. 
Click the button and complete the the login and authorization process with PayPal. 

![PayPal website with the pretix logo in the top right and a dialog in the center telling you to 'Connect a PayPal account to start accepting payments on rami.io GmbH'. You can enter your email and country or region below.](../../assets/screens/payment-providers/paypal-connect-account.png "Connecting to PayPal" )

After you have completed the authorization process with PayPal, the PayPal settings page in the pretix backend will look different. 
Instead of the single button, it will now offer a multitude of settings. 
Your PayPal merchant ID will be displayed at the top of the page. 
All settings here are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box next to "enable payment method". 
PayPal will now appear as a payment option for customers in your shop. 

## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 