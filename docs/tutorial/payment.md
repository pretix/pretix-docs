# Payment

## Setting up payment providers 

pretix takes care of payment via a wide selection of payment providers. 
For our conference, we are planning to receive payments by credit card through the payment provider Stripe and via bank transfer. 
pretix will log payments coming in through most payment providers, including Stripe. 
An order in our shop will be marked as paid automatically as soon as payment arrives via Stripe. 
Bank transfers are the exception to that rule. 
There is no way for the pretix software to monitor payments arriving at our bank account. 
Thus, we have to notify the pretix software of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 

First of all, we need to enable the plugins for bank transfers and Stripe. 
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
We will check the boxes next to "credit card payments" and "enable payment method", then scroll to the bottom and click the :btn:Save: button. 
Credit card payments via Stripe are now available as a payment method for customers in our shop. 

For more information on using Stripe as a payment provider, see [Stripe (Topic)] (../topics/payment/stripe.md). 
TK Leerzeichen zwischen klammern entfernen, sobald PR Payment providers2 #22 gemerget ist

We will also enable bank transfers by navigating to [Event] → "Settings" → "Payment" and opening the bank transfer settings. 
We are going to choose "SEPA bank account" as our "bank account type". 
We will provide our bank account info, i.e. the name of the account holder, IBAN, BIC and the name of the bank in the fields labeled as such. 
We will then check the box to confirm that we have understood the special conditions that apply to bank transfers when using pretix and the box next to "enable payment method". 
Then, we will click the :btn:Save: button and return to the payment settings. 
Bank transfer, gift card, and Stripe should all have a green :✓ Enabled" tag next to them now. 

For more information on using bank transfers, see [bank transfers (Topic)] (../topics/payment/bank-transfer.md). 
TK Leerzeichen zwischen klammern entfernen, sobald PR Payment providers2 #22 gemerget ist

## Invoices 

The invoicing settings are located at [Event] → "Settings" → "Invoicing". 
On the "invoice generation" tab, we will set the "generate invoices" option to "automatically after payment or when required by payment method."


 - payment, invoicing and taxes
 - what are the options for payment (payment providers)?
 - how do you enable and set up the payment options you want to use?
 - how to set sane default settings for invoicing
 - make it abundantly clear that none of this is legal/financial/tax advice
