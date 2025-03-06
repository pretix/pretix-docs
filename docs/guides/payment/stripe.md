# Stripe

Stripe is one of the many options for handling payments within pretix. 
Stripe allows handling payments via the following methods: 

Affirm, Alipay, Apple Pay, Bancontact, credit card, EPS, giropay, Google Pay, iDEAL, Klarna, Multibanco, Przelewy24, SEPA Direct debit, SOFORT, Swish, and WeChat Pay. 

This article tells you how to connect to your Stripe account and use it to receive payments via pretix. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 
Make sure you have an active Stripe merchant account. 
A regular Stripe account is not enough for integration with pretix. 
You can find [instructions on how to sign up for a Stripe merchant account](https://stripe.com/resources/more/how-to-get-a-merchant-account) on the Stripe website. 

## How To 

Setting up Stripe as a payment provider in pretix involves the following steps: 

 1. Enable the Stripe plugin 
 2. Connect to your Stripe merchant account 
 3. Enter mandatory info on the settings page for Stripe
 4. Make optional adjustments
 5. Enable payment via Stripe
 6. Test it 
 7. Switch the Stripe endpoint to "live" 

This section guides you through those steps in detail. 

![Plugins settings page. The "Payment providers" tab is open, displaying the plugins for bank transfer, Mollie, PayPal, and Stripe, all of which are active.](../../assets/screens/payment-providers/plugins-top.png "Available plugins")

Navigate to :navpath:Your Event → Settings → Plugins:.
Switch to the :btn:Payment providers: tab. 
The Stripe plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green ":fa3-check: Active" tag and a white :btn:Disable: button. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 
Make sure that the plugin is enabled. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigate to :navpath:Your Event → Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
The list should now include an entry for Stripe with a red ":fa3-times: Disabled" tag. 
The plugin is enabled, but Stripe has not been set up and enabled as a payment provider for the event yet. 
Click on the :btn-icon:fa3-cog:Settings: button next to Stripe. 
This takes you to the settings page for Stripe, which currently only includes the :btn:Connect with Stripe: button. 

From this point on, the process is different depending on whether you are using pretix Hosted or a self-hosted edition of pretix (Community or Enterprise). 

### Connecting to Stripe with pretix Hosted 

<!-- md:hosted -->

Click the button and complete the the login and authorization process with Stripe. 

![Stripe website with the pretix logo on the left, telling you that 'pretix.eu partners with Stripe for secure payments' and a dialog on the right telling you to 'Get started with stripe'. You can enter the email address for your Stripe account below.](../../assets/screens/payment-providers/stripe-connect-account.png "Connecting to Stripe" )

After you have completed the authorization process with Stripe, the Stripe settings page in the pretix backend will look different. 
Instead of the single button, it will now offer a multitude of settings. 
Your Stripe account will be displayed near the top of the page. 
There are several checkboxes for activating payment methods such as credit cards, Alipay or KLARNA for handling via Stripe. 
Check the box for each payment method you want to enable. 
Some of the payment methods offered here need to be enabled in your Stripe account settings. 
Check your account settings on the Stripe website or app for settings related to the payment methods you want to use and enable them. 

All further settings on this page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box next to "enable payment method". 
The payment methods you enabled on this page and in your Stripe account settings will now appear as options for customers in your shop during payment. 

Once you take your ticket shop live, you also have to switch the "endpoint" option on this page from "testing" to "live". 
While your event is in test mode, the pretix software will always use Stripe's testing endpoint regardless of the setting here. 

### Connecting to PayPal with a self-hosted edition of pretix 

<!-- md:community --> 
<!-- md:enterprise -->

If you are using pretix Community or pretix Enterprise and you have not connected your account to Stripe yet, the settings page for Stripe will display two fields labeled "Stripe account". 
Go to [https://developer.paypal.com](https://developer.paypal.com) and log in to your account. 
Create a new REST API app and switch it from "Sandbox" to "Live". 
Copy the Client ID and Secret from the PayPal REST API app page to the settings page for PayPal in pretix. 
For further information, refer to the PayPal documentation page on [PayPal REST APIs](https://developer.paypal.com/api/rest/). 

You also need to create a webhook so that Stripe can update pretix with information such as payment cancellations. 
Copy the webhook URL from the Stripe settings page in pretix. 
Open [https://developer.paypal.com](https://developer.paypal.com) and edit the REST API app you created for this event. 
Add a webhook and paste the webhook URL into the corresponding field. 
Check the box next to "All events" and save your settings. 

After you have set up the connection between pretix and PayPal, the PayPal settings page in the pretix backend will now offer a multitude of settings. 
All settings here are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box next to "enable payment method". 
PayPal and the other payment methods you enabled on this site will now appear as a payment option for customers in your shop. 
