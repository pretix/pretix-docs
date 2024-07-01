# Payment

We do not just want to offer tickets in our shop; we also want to get paid for them. 
That is what we will take care of in this part of the tutorial. 
We will set up payment via bank transfer and credit card. 
We will also set up invoices to be sent automatically with every order. 

## Setting up payment providers 

pretix takes care of payment via a wide selection of payment providers. 
For our conference, we are planning to receive payments by credit card through the payment provider Stripe and by bank transfer. 
The prerequisites for this are an active Stripe merchant account and a bank account. 
pretix will log payments coming in through most payment providers, including Stripe. 
An order in our shop will be marked as paid automatically as soon as Stripe records a corresponding payment. 
Bank transfers are the exception to that rule because the pretix software would need to monitor payments arriving at our bank account.
A connection to your bank account is possible to set up on pretix Hosted, but it is also possible to manually approve payments as thex come in, or by regularly importing digital bank statements. 

First of all, we need to enable the plugins for bank transfers and Stripe. 
We are going to navigate to [Event] → "Settings" → "Plugins" and open the "payment providers" tab. 
By default, the plugins for bank transfer, PayPal, Stripe and SEPA Direct debit will be activated. 
Since we do not intend to use PayPal or SEPA Direct debit, we are going to click on the :btn:Disable: buttons for those two plugins. 

We will then navigate to [Event] → "Settings" → "Payment", which displays a list of payment providers. 
The list should now include bank transfer, gift card, and Stripe. 
By default, gift card will be enabled and all other payment providers will be disabled. 

We will first enable Stripe by clicking the :btn:⚙️ Settings: button next to it. 
This takes us to the payment settings page for Stripe, which currently only contains a purple :btn:Connect with Stripe: button. 
Clicking that button takes us to a dialog on stripe.com, where we will input our email address and go through the process of connecting our Stripe merchant account to our pretix account. 
We will then return to pretix.eu, navigate to [Event] → "Settings" → "Payment" and open the Stripe settings. 
Instead of the single button, the page will now display a multitude of settings. 
We will check the boxes next to "credit card payments" and "enable payment method", then scroll to the bottom and click the :btn:Save: button. 
Credit card payments via Stripe are now available as a payment method for customers in our shop. 

For more information on using Stripe as a payment provider, see [Stripe](../topics/payment/stripe.md). 

We will also enable bank transfers by navigating to [Event] → "Settings" → "Payment" and opening the bank transfer settings. 
We are going to choose "SEPA bank account" as our "bank account type". 
We will provide our bank account info, i.e. the name of the account holder, IBAN, BIC and the name of the bank in the fields labeled as such. 
We will then check the box to confirm that we have understood the special conditions that apply to bank transfers as a payment provider in pretix and the box next to "enable payment method". 
Then, we will click the :btn:Save: button and return to the payment settings. 
Bank transfer, gift card, and Stripe should all have a green :✓ Enabled" tag next to them now. 

!!! Warning 
    By default, the pretix software is not able to monitor payments arriving at your bank account.
    On pretix Hosted, you can set up automated bank imports.
    Otherwise, you have to notify the pretix software of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 
    Read our guide on [monitoring incoming payments] (../topics/payment/bank-transfer.md#monitoring-incoming-payments) before using bank transfer as a payment method in your shop. 

For more information on using bank transfers, see [bank transfers](../topics/payment/bank-transfer.md). 

## Setting up invoices 

We will browse to the invoicing settings  at [Event] → "Settings" → "Invoicing". 
On the "invoice generation" tab, we will set the "generate invoices" option to "automatically after payment or when required by payment method."
We will then switch to the "issuer details" tab and provide the name and full address of our organization. 
If we now click the :btn:Save and show preview: button, our browser is going to download a PDF preview of the invoice with our or organization's address, the invoice number EX-CONF-2027-PREVIEW and an example listing of purchases with a partially received payment. 

## Conclusion

Now that we have given our customers two options for making payments in our shop and set up the automatic dispatching of invoices, we can move on to testing our shop before finally taking it live. 
