# Payment

## Setting up a payment provider

For our conference, we are planning to receive payments via bank transfer and a few other methods that are going to be handled through the payment provider Stripe. 
We are going to navigate to [Event] → "Settings" → "Plugins" and open the "payment providers" tab. 
By default, the plugins for bank transfer, PayPal, Stripe and SEPA Direct debit will be activated. 
Since we are not planning on using PayPal or SEPA Direct debit, we are going to click on the :btn:Disable: buttons for those two plugins. 

We will then navigate to [Event] → "Settings" → "Payment", which displays a list of payment providers. 
The list should now include bank transfer, gift card, and Stripe. 
By default, gift card will be enabled and all other payment providers will be disabled. 

We will first enable Stripe by clicking on the :btn:⚙️ Settings: button next to it. 
This takes us to the payment settings for Stripe, which currently only contains a purple :btn:Connect with Stripe: button. 
Clicking that button takes us to a dialog on stripe.com, where we will input our mail address and go through the process of connecting our Stripe merchant account to our pretix account. 
We will then return to pretix.eu, navigate to [Event] → "Settings" → "Payment" and open the Stripe settings. 
Instead of the single button, the page will now display a multitude of settings. 


## Invoices 

The invoicing settings are located at [Event] → "Settings" → "Invoicing". 
On the "invoice generation" tab, we will set the "generate invoices" option to "automatically after payment or when required by payment method."


 - payment, invoicing and taxes
 - what are the options for payment (payment providers)?
 - how do you enable and set up the payment options you want to use?
 - how to set sane default settings for invoicing
 - make it abundantly clear that none of this is legal/financial/tax advice
