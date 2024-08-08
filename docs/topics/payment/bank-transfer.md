# Bank transfer

Bank transfers are one of the numerous options for handling payments within pretix. 
Payments made via bank transfer go directly to your bank account. 
By default, pretix does not monitor payments arriving at your bank account. 
If you are using pretix Hosted, you can set up a connection to your bank account for automatic imports of bank data. 
This works with most European banks. 

The alternatives for notifying pretix of incoming payments are: manually approving payments as complete or regularly importing digital bank statements. 
This article is going to tell you how to set up a bank connection so that you can use it to receive payments via pretix. 
It is also going to tell you how to notify pretix of incoming payments. 

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
 6. Set up automatic transaction import **or** regularly import a digital bank statement **or** mark incoming payments as complete manually

This section will guide you through those steps in detail. 

### Setting up bank transfers

If you want to use bank transfers to receive payments in pretix, the "Bank transfer" plugin needs to be enabled. 
In order to make sure that the plugin is enabled, navigate to :navpath:Your Event → Settings → Plugins:. 
Switch to the :btn:Payment providers: tab. 

The bank transfer plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green ":fa3-check: Active" tag and a white :btn:Disable: button. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 

![Payment settings page. The "Payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

Navigate to :navpath:Your Event → Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
The list should now include an entry for bank transfer with a red ":fontawesome-solid-x: Disabled" tag. 
The plugin is enabled, but bank transfers have not been set up and enabled as a payment provider for the event yet. 
Click on the :btn-icon:fa3-gear:Settings: button next to bank transfer. 
This takes you to the settings page for bank transfer.  

The first thing you need to do on this page is choose the "Bank account type". 
If you choose "SEPA bank account", you have to provide the name of the account holder, IBAN, BIC and the name of the bank. 
If you choose "Other bank account", you have to provide the full details of the bank connection in the "Bank account details" fields. 

All settings further down on the page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box confirming that you have understood how bank transfers work in pretix, and the box next to "Enable payment method". 
Bank transfers will now appear as a payment option for customers in your shop. 

### Monitoring incoming payments 

For pretix Hosted, we have partnered with [GoCardless](https://gocardless.com) to allow a seamless integration for automatic transaction importing for [thousands of banks in over 30 countries](https://gocardless.com/bank-account-data/coverage/).
Alternatively, you can to notify pretix of incoming payments—either by manually approving payments as complete, or by regularly importing digital bank statements. 
This section is going to guide you through all three options. 

#### Option A: automatic transaction import using GoCardless 

<!-- md:hosted -->

If you are using pretix Hosted, you can activate the automatic transaction report via pretix's integration with GoCardless. 
This service is on the organizer level, meaning that bank data imported via this method is available for all events associated with the organizer. 
Navigate to :navpath:Your organizer → :material-bank: Bank transfer → Automatic import: . 

![Page titled Automatic transaction import, containing a lot of information and a button for uploading unmatched transactions for review.](../../assets/screens/payment/automatic-transaction-import.png "Automatic transaction import" )

Choose your country, bank, and start date for importing transactions. 
If you leave the "Import Transactions since" field empty, pretix will import as many transactions as possible. 
Usually, this includes all transactions of the last 90 days. 

This can lead to problems if you have previously imported bank data to the same organizer account because the datapoints will be formatted differently and may not be easily recognized as depicting the same transactions. 
Select the first day on which you have **not** imported bank data to the same organizer account if this applies to you. 
In all other cases, you can leave the field empty. 

Click the :btn-icon:material-login: Connect with bank: button. 
This takes you to a webpage on ob.gocardless.com which asks you to consent to your data being processed by GoCardless and to provide your bank login. 
Complete the authorization process according to the instructions on the website. 
You will then be redirected back to the pretix backend. 

If you have multiple accounts at the bank, you have to select the bank account that you want to import data from. 
Choose a start date for importing transactions and confirm by clicking the :btn:Connect to bank: button. 
If you now browse back to the "Automatic import" page, it will display the bank connections you selected on the previous page as connected. 

Once the automatic import is active, you should check it for unresolved transactions occasionally. 
The [section below](bank-transfer.md#handling-unresolved-transactions) explains how to handle unresolved transactions manually. 

#### Option B: importing bank data 

Acquire an export of your bank account's transaction data. 
The export has to be a file in the CSV or MT940 file format. 
It has to contain the following data: 

 - date 
 - amount 
 - reference 
 - payer 
 - IBAN 
 - BIC 

IBAN and BIC are optional, but pretix can offer additional functionality if they are provided (such as automatically generating refund files). 

You have two options: importing bank data for all events on the organizer level, or importing bank data for a single event. 
We recommend the first option, unless you have separate bank accounts for every event you are hosting. 
If you want to import data for all events associated with the organizer, navigate to :navpath:Your organizer → :material-bank: Bank transfer:. 
This will take you to a page titled "Import bank data". 

If you want to import data for a single event, navigate to :navpath:Your event → :material-bank: Bank transfer:. 
This will also take you to a page titled "Import bank data". 
The two pages are very similar, but one is located on the event level and the other is located on the organizer level. 
Whichever option you choose, the process is the same from here on out. 

Click the :btn:Browse...: button and select the export file for upload. 
Click the :btn:Start upload: button. 
pretix will now ask you to specify which column in your file contains which data. 
The screenshot illustrates what such an assignment could look like with a small example CSV file. 

![Import bank data page with a dialog asking the user to assign columns from a CSV file to the data points date, amount, reference, payer, IBAN and BIC.](../../assets/screens/payment-providers/import-bank-data.png "Import bank data" )

Click :btn:Continue:. 
You will be taken to a loading screen while your data is being processed and then to an overview of how many orders were marked as paid, invalid, or ignored. 
Transactions that are already known to the system because they have been imported at an earlier date will be ignored. 
Transactions will be unresolved if pretix cannot make a connection between the bank transaction and any order in your shop. 

You can intervene and make manual corrections here on this screen. 
The [section below](bank-transfer.md#handling-unresolved-transactions) explains how to handle unresolved transactions manually. 

#### Option C: approving payments manually 

![Page titled orders, showing a list currently containing one order with status pending, €0.00 out of €250.00 paid.](../../assets/screens/payment/orders.png "Orders" )

Navigate to :navpath:Your Event → Orders:. 
This page displays a list of all orders that have been placed in your shop. 
If orders have been placed and not yet received a payment (which is expected if they are paid via bank transfer), they will be displayed here with the yellow ":fa3-money: Pending" status tag. 

Click the order code of one of the pending orders. 
This takes you to the "order details" page for that order. 
Check the transaction data of your bank account. 
If your bank account's transaction data has a record that matches the order in question, click the :btn-icon:fa3-check:Mark as paid: button at the top of the order details page. 

![Page titled Mark order as paid, showing options for changing the payment amount of  €250.00, payment date, and whether or not to notify the customer by email.](../../assets/screens/payment/order-mark-as-paid.png "Orders" )

!!! Warning 

    Before confirming the order as paid, make absolutely sure that you have the correct order, the correct price, and the correct date. 
    Once a payment has been recorded, it cannot be deleted. 

Adjust the payment amount and date if necessary. 
By default, the customer will be notified about the order being marked as paid via email. 
You can prevent this by unchecking the box next to "notify customer by email". 
Confirm by clicking the :btn:Create payment: button. 

This takes you back to the "order details" page, now with a notification box at the top saying "The payment has been created successfully" and a green tag in the top right saying "✓ Paid". 
Repeat this process for every order that shows up in the list on the "orders" page. 

### Handling unresolved transactions 

Options A and B described above may sometimes yield unresolved transactions. 
The most frequent cause for this is a mistyped or missing order number in the reference line. 
If the bank account is also used for transactions unrelated to sales via pretix, this will produce unresolved transactions as well. 
pretix allows you to resolve these transactions manually. 

If you have imported bank data on the organizer level, navigate to :navpath:Your organizer → :material-bank: Bank transfer:, which lands you on the page titled "Import bank data". 
If you have imported bank data on the event level, navigate to :navpath:Your event → :material-bank: Bank transfer:, which lands you on the page titled "Import bank data". 
The process is the same from here on out. 

If there are unresolved transactions, they will be displayed on this page as a list titled "Unresolved transactions". 
For every transaction in this list, you have two options: 
You can either tell pretix to ignore it by clicking the :btn-icon:fa3-trash:: button, or you can search for a matching order and assign the order code to the transaction. 

In order to do that, enter part of the order code or the name recorded in the transaction into the "Order code" field on the unresolved transaction. 
Select the correct order from the search results and click the :btn-icon:fa3-check:: button to confirm. 
Repeat this process for all unresolved orders. 

If you cannot find and resolve all transactions this way, open a new browser tab and navigate to :navpath:Your event: → :fa3-shopping-cart: Orders:. 
Search the list for an order that matches the parameters of the unresolved transaction. 
Copy the order code, paste it into the "order code" input field on the unresolved transaction, and click the :btn-icon:fa3-check:: button to confirm. 

Only delete transactions if they are unrelated to the event you are hosting and no matching order can be found. 