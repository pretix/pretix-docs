# Stripe

Stripe is one of the many options for handling payments within pretix. 
Stripe allows handling payments via the following methods: 
Affirm, Alipay, Apple Pay, Bancontact, credit card, EPS, giropay, Google Pay, iDEAL, Klarna, Multibanco, Przelewy24, SEPA Direct debit, SOFORT, Swish, and WeChat Pay. 
This article tells you how to connect to your Stripe account and use it to receive payments via pretix. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 
You need to have an active Stripe merchant account. 
A regular Stripe account is **not** enough for integration with pretix. 
You can find [instructions on how to sign up for a Stripe merchant account](https://stripe.com/resources/more/how-to-get-a-merchant-account) on the Stripe website. 

## How To

Setting up Stripe as a payment provider in pretix involves the following steps: 

 1. Enable the Stripe plugin 
 2. Connect to your Stripe merchant account 
 3. Enter mandatory info on the settings page for Stripe
 4. Make optional adjustments
 5. Enable payment via Stripe
 6. Test it 
 7. Switch the Stripe endpoint to "Live" 

This section will guide you through those steps in detail. 

Navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins:.
Switch to the :btn:Payment providers: tab. 
This page displays the Stripe plugin at the top. 
It should be active by default. 
If it is active, it will have a green ":fa3-check: Active" tag, a white "Disable" button, and two drop-down menus. 
If it is **not** active, the tag will be missing and it will have a purple :btn:Enable: button. 
Verify that the plugin is active. . 

![Payment settings page. The 'Payment providers' tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe. Gift card is enabled and all other entries are disabled. All entries have 'Settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

You can jump straight to the Stripe settings by clicking the :btn-icon:fa3-gear: Settings: drop-down menu and then :btn:Payment > Stripe:. 

Alternatively, navigate to :navpath:Your Event → :fa3-wrench: Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
The list should now include an entry for Stripe with a red ":fa3-remove: Disabled" tag. 

The plugin is active, but you have not set up Stripe as a payment provider for the event yet. 
Click the :btn-icon:fa3-gear:Settings: button next to Stripe. 
This takes you to the settings page for Stripe, which currently only includes the :btn:Connect with Stripe: button. 
Click the button and complete the login and authorization process with Stripe. 

![Stripe website with the pretix logo on the left, telling you that 'pretix.eu partners with Stripe for secure payments' and a dialog on the right telling you to 'Get started with stripe'. You can enter the email address for your Stripe account below.](../../assets/screens/payment-providers/stripe-connect-account.png "Connecting to Stripe" )

After you have completed the authorization process with Stripe, the Stripe settings page in the pretix backend will look different. 
Instead of the single button, it will now offer a multitude of settings. 
The page will display your Stripe account near the top. 

There are several checkboxes for activating payment methods such as credit cards, Alipay or KLARNA for handling via Stripe. 
Check the box for each payment method you want to enable. 
You need to enable some of the payment methods offered here explicitly in your Stripe account settings. 
Check your account settings on the Stripe website or app for settings related to the payment methods you want to use and enable them. 

All further settings on this page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box next to "Enable payment method". 
The payment methods you enabled on this page and in your Stripe account settings will now appear as options for customers in your shop during payment. 

Once you take your ticket shop live, you also have to switch the "Endpoint" option on this page from "Testing" to "Live". 
While your event is in test mode, the pretix software will always use Stripe's testing endpoint regardless of the setting here. 
