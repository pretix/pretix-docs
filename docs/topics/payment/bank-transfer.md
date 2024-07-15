# Bank transfer

Bank transfers are one of the numerous options for handling payments within pretix. 
Payments made via bank transfer go directly to your bank account. 
By default, the pretix software does not monitor payments arriving at your bank account. 
If you are using pretix Hosted, you can use our integration with [GoCardless](https://gocardless.com) to automatically import bank data. 
The alternatives for notifying the pretix software of incoming payments are: manually approving payments as complete, or regularly importing digital bank statements. 
This article is going to tell you how to set up a bank connection so that you can use it to receive payments via pretix. 
It is also going to tell you how to notify the pretix software of incoming payments. 

## Prerequisites

As setting up payment providers is handled on the event level, you need to create an event first. 
Make sure you have access to the bank account that you want to use. 

## How To 

Setting up bank transfer as a payment provider in pretix requires the following steps: 

 1. Enable the bank transfer plugin. 
 2. Choose the type of bank account (SEPA or other)
 3. Enter mandatory info on the bank transfer settings page 
 4. Make optional adjustments
 5. Enable payment via bank transfer
 6. Set up monitoring via GoCardless **or** mark incoming payments as complete manually **or** regularly import a digital bank statement

This section will guide you through those steps in detail. 

### Setting up bank transfers

Navigate to [Your Event] :fontawesome-solid-arrow-right: "Settings" :fontawesome-solid-arrow-right: "Plugins". 
Switch to the "payment providers" tab. 
The bank transfer plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green ":fontawesome-solid-check: Active" tag and a white :btn:Disable: button. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 
Make sure that the plugin is enabled. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigate to [Your Event] :fontawesome-solid-arrow-right: "Settings" :fontawesome-solid-arrow-right: "Payment". 
The "payment providers" tab on this page displays the list of active payment providers. 
The list should now include an entry for bank transfer with a red ":fontawesome-solid-x: Disabled" tag. 
The plugin is enabled, but bank transfers have not been set up and enabled as a payment provider for the event yet. 
Click on the :btn-icon:fontawesome-solid-gear:Settings: button next to bank transfer.  
This takes you to the settings page for bank transfer.  

The first thing you need to do on this page is choose the "bank account type". 
If you choose "SEPA bank account", you have to provide the name of the account holder, IBAN, BIC and the name of the bank. 
If you choose "other bank account", you have to provide the full details of the bank connection in the "bank account details" fields. 

All settings further down on the page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box confirming that you have understood how bank transfers work in pretix, and the box next to "enable payment method". 
Bank transfers will now appear as a payment option for customers in your shop. 

### Monitoring incoming payments 

There is no way for the pretix software to monitor payments arriving at your bank account. 
Thus, you have to notify the pretix software of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 
This section is going to guide you through all three options. 

**Option A: automatic transaction import using GoCardless**

<!-- md:hosted -->

If you are using pretix Hosted, you can activate the automatic transaction report via pretix's integration with GoCardless. 
Navigate to [Your organizer] :fontawesome-solid-arrow-right: ":material-bank: Bank transfer" :fontawesome-solid-arrow-right: "Automatic import". 

![Page titled Automatic transaction import, containing a lot of information and a button for uploading unmatched transactions for review.](../../assets/screens/payment/automatic-transaction-import.png "Automatic transaction import" )

Choose your region, bank and start date for importing transactions and click the :btn-icon:material-login: Connect with bank: button. 
This takes you to a webpage on ob.gocardless.com which asks you to consent to your data being processed by GoCardless and to provide your bank login. 
Complete the authorization process according to the instructions on the website. 
You will then be redirected to the pretix backend. 
Select the bank connections that you want to process, choose a start date for importing transactions and confirm by clicking the :btn:Connect to bank: button. 
If you now browse back to the "Automatic import" page, It will display the bank connections you selected on the previous page as connected. 

**Option B: importing bank data** 

Acquire an export of your bank account's transaction data. 
The export has to be a file in the CSV or MT940 file format. 
It has to contain the following data: 

 - date 
 - amount 
 - reference 
 - payer 
 - IBAN 	
 - BIC 

IBAN and BIC can be omitted for non-SEPA transactions. 

In the pretix backend, click on "bank transfer" in the sidebar menu. 
This will take you to a page titled "import bank data". 
Click on the :btn:Browse...: button and select the export file for upload. 
Click the :btn:Start upload: button. 
The pretix software will now ask you to specify which column in your file contains which data. 
The screenshot illustrates what such an assignment could look like with a small example CSV file. 

![Import bank data page with a dialog asking the user to assign columns from a CSV file to the data points date, amount, reference, payer, IBAN and BIC.](../../assets/screens/payment-providers/import-bank-data.png "Import bank data CSV" )

Click :btn:Continue:. 
You will be taken to a loading screen while your data is being processed and then to an overview of how many orders were marked as paid, invalid, or ignored. 
Orders will be ignored if the pretix software cannot make a connection between the bank transaction and any order in your shop. 
You can intervene and make manual corrections here on this screen or by navigating to [Your Event] :fontawesome-solid-arrow-right: "Orders". 

**Option C: approving payments manually** 

![Page titled orders, showing a list currently containing one order with status pending, €0.00 out of €250.00 paid.](../../assets/screens/payment/orders.png "Orders" )

Navigate to [Your Event] :fontawesome-solid-arrow-right: "Orders". 
This page displays a list of all orders that have been placed in your shop. 
If orders have been placed and paid via bank transfer, they will be displayed here with the yellow ":fontawesome-solid-money-bill: Pending" status tag. 
Click on the order code of one of the pending orders. 
This takes you to the "order details" page for that order. 
Check the transaction data of your bank account. 
If your bank account's transaction data has a record that matches the order in question, click the :btn-icon:fontawesome-solid-check:Mark as paid: button at the top of the order details page. 

![Page titled Mark order as paid, showing options for changing the payment amount of  €250.00, payment date, and whether or not to notify the customer b email.](../../assets/screens/payment/order-mark-as-paid.png "Orders" )

!!! Warning 

    Before confirming the order as paid, make absolutely sure that you have the correct order, the correct price, and the correct date. 
    Once an order has been marked as paid, it cannot be marked as not paid/pending. 

Adjust the payment amount and date if necessary. 
By default, the customer will be notified about the order being marked as paid via email. 
You can prevent this by unchecking the box next to "notify customer by email". 
Confirm by clicking the :btn:Create payment" button. 
This takes you back to the "order details" page, now with a notification box at the top saying "The payment has been created successfully." and a green tag in the top right saying "✓ Paid". 
Repeat this process for every order that shows up in the list on the "orders" page. 

### Handling unresolved transactions 

Options A and B described above may sometimes yield unresolved transactions. 
The most frequent cause for this is a mistyped or missing order number in the reference line. 
pretix allows you to resolve these transactions manually. 
Navigate to [Your organizer] :fontawesome-solid-arrow-right: ":material-bank: Bank transfer" :fontawesome-solid-arrow-right: "Import bank data". 
If there are unresolved transactions, they will be displayed on this page under a list titled "Unresolved transactions". 
For every transaction in this list, you have two options: 
Either you delete it by clicking the :btn-icon:fontawesome-solid-trash-can:: button, or you search for a matching order and assign the order code to the transaction.
In order to do that, open a new browser tab and navigate to [Your event] :fontawesome-solid-arrow-right: ":fontawesome-solid-cart-shopping: Orders". 
Search the list for an order that matches the parameters of the unresolved transaction. 
Copy the order code, paste it into the "order code" input field on the unresolved transaction, and click the :btn-icon:fontawesome-solid-check:: button to confirm. 
Repeat this process for all unresolved orders. 
Delete them only if they have nothing to do with the event you are hosting and no matching order can be found. 
