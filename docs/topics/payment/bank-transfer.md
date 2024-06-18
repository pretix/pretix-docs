# Bank transfer

Bank transfers are one of the many options for handling payments within pretix. 
Payments made via bank transfer go directly to your bank account. 
There is no way for the pretix software to monitor payments arriving at your bank account. 
Thus, you have to notify the pretix software of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 
This article is going to tell you how to set up a bank connection so that you can use it to receive payments via pretix. 
It is also going to tell you how to notify the pretix software of incoming payments. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 
Make sure you have access to the appropriate bank account. 

## How To 

Setting up bank transfer as a payment provider in pretix involves the following steps: 

 1. Enable the bank transfer plugin. 
 2. Choose the type of bank account (SEPA or other)
 3. Enter mandatory info on the bank trasnfer settings page 
 4. Make optional adjustments
 5. Enable payment via bank transfer
 6. Monitor incoming payments and mark them as complete manually **or** regularly import a digital bank statement

This section will guide you through those steps in detail. 

### Setting up bank transfers

Navigate to [Your Event] → "Settings" → "Plugins". 
Switch to the "payment providers" tab. 
The bank transfer plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green "✓ Active" tag and a white :btn:Disable: button. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 
Make sure that the plugin is enabled. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigate to [Your Event] → "Settings" → "Payment". 
The "payment providers" tab on this page displays the list of active payment providers. 
The list should now include an entry for bank transfer with a red "❌ Disabled" tag. 
The plugin is enabled, but bank transfers have not been set up and enabled as a payment provider for the event yet. 
Click on the :btn:⚙ Settings: button next to bank transfer.  
This takes you to the settings page for bank transfer.  

The first thing you do on this page is choose the "bank account type". 
If you choose "SEPA bank account", you have to provide the name of the account holder, IBAN, BIC and the name of the bank. 
If you choose "other bank account", you have to provide the full details of the bank connection in the "bank account details" fields. 

All settings further down on the page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box confirming that you have understood how bank transfers work in pretix, and the box next to "enable payment method". 
Bank transfers will now appear as a payment option for customers in your shop. 

### Monitoring incoming payments 

There is no way for the pretix software to monitor payments arriving at your bank account. 
Thus, you have to notify the pretix software of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 
This section is going to guide you through both options. 

**Option A: importing bank data** 

Acquire an export of your bank account's transaction data. 
The export has to be a file in the CSV or MT940 file format. 
It has to contain the following data: 

 - date 
 - amount 
 - reference 
 - payer 
 - IBAN 	
 - BIC 

IBAN and BIC can be ommitted for non-SEPA transactions. 

In the pretix backend, click on "bank transfer" in the sidebar menu. 
This will take you to a page titled "import bank data". 
Click on the :btn:Browse...: button and select the export file for upload. 
Click the :btn:Start upload: button. 
The pretix software will now attempt to parse your uploaded file automatically. 
If this does not work, you will be asked to specify which column in your file contains which data. 

![Import bank data page with a dialog asking the user to assign columns from a CSV file to the data points date, amount, reference, payer, IBAN and BIC.](../../assets/screens/payment-providers/import-bank-data.png "Import bank data" )