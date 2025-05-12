# Bank transfer

Bank transfers are one of the numerous options for handling payments within pretix. 
Payments made via bank transfer go directly to your bank account. 
By default, pretix does not monitor payments arriving at your bank account. 
If you are using pretix Hosted, you can connect your bank account via our integration with GoCardless for automatic imports of bank data. 

The alternatives for notifying pretix of incoming payments are: manually approving payments as complete or regularly importing digital bank statements. 
This article is going to tell you how to set up a bank connection so that you can use it to receive payments via pretix. 
It is also going to tell you how to notify pretix of incoming payments. 

!!! Note 
    pretix does not handle refunds via bank transfer automatically. 
    If a customer cancels their order and requests a refund via the original payment method, and that payment method is bank transfer, you will receive an email notification. 
    You will have to issue the refund manually. 

## Prerequisites

As setting up payment providers is handled on the event level, you need to create an event first. 
Make sure you have access to the bank account that you want to use. 

## How To

Successfully using bank transfer as a payment provider in pretix requires the following steps: 

 1. Setting up bank transfers by enabling the bank transfer plugin and adjusting the bank transfer settings 
 2. Setting up automatic transaction import **or** regularly importing a digital bank statement 
 3. Approving transactions manually 
 4. Handling transactions manually 

This section will guide you through these steps in detail. 

### Setting up bank transfers

If you want to use bank transfers to receive payments in pretix, the "Bank transfer" plugin needs to be enabled. 
In order to make sure that the plugin is enabled, navigate to :navpath:Your Event → Settings → Plugins:. 
Switch to the :btn:Payment providers: tab. 

The bank transfer plugin is displayed at the top of the page. 
It should be enabled by default. 
If it is enabled, it will have a green ":fa3-check: Active" tag, a white "Disable" button, and two drop-down menus. 
If it isn't enabled, the tag will be missing and it will have a purple :btn:Enable: button. 

![Payment settings page. The "Payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entries have 'settings' buttons next to them.](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

You can jump straight to the bank transfer settings by clicking the :btn-icon:fa3-gear: Settings: drop-down menu and then :btn:Payment > Bank transfer:. 

Alternatively, navigate to :navpath:Your Event → Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
The list should now include an entry for bank transfer with a red ":fa3-remove: Disabled" tag. 

The plugin is enabled, but bank transfers have not been set up and enabled as a payment provider for the event yet. 
Click the :btn-icon:fa3-gear:Settings: button next to bank transfer. 
This takes you to the settings page for bank transfer.  

The first thing you need to do on this page is choose the "Bank account type". 
If you choose "SEPA bank account", you have to provide the name of the account holder, IBAN, BIC and the name of the bank. 
If you choose "Other bank account", you have to provide the full details of the bank connection in the "Bank account details" fields. 

All settings further down on the page are optional. 
Take a detailed look at the page and enable any settings you want for this payment provider for your event. 
Once you are satisfied, scroll to the top of the page and check the box confirming that you have understood how bank transfers work in pretix, and the box next to "Enable payment method". 
Bank transfers will now appear as a payment option for customers in your shop. 

### Monitoring incoming payments automatically

For pretix Hosted, we have partnered with [GoCardless](https://gocardless.com) to allow a seamless integration for automatic transaction importing for [thousands of banks in over 30 countries](https://gocardless.com/bank-account-data/coverage/).
Alternatively, you can notify pretix of incoming payments by regularly importing digital bank statements. 
This section is going to guide you through both options. 

#### Option A: automatic transaction import using GoCardless

<!-- md:hosted -->

If you are using pretix Hosted, you can activate the automatic transaction import via pretix's integration with GoCardless. 
This service is on the organizer level, meaning that bank data imported via this method is available for all events associated with the organizer. 
Navigate to :navpath:Your organizer → :fa3-bank: Bank transfer → Automatic import: . 

![Page titled Automatic transaction import, containing text with the subheadings 'Why importing transactions automatically?', 'Unmatched transactions' and 'Security and privacy', as well as a button for uploading unmatched transactions for review.](../../assets/screens/payment/automatic-transaction-import.png "Automatic transaction import" )

Choose your country, bank, and start date for importing transactions. 
If you leave the "Import Transactions since" field empty, pretix will import as many transactions as possible. 
Usually, this includes all transactions of the last 90 days. 

This can lead to problems if you have previously used a different method to import bank data to the same organizer account. 
Data may be formatted differently and thus not be easily recognized as depicting the same transactions. 
Select the first day for which you have **not** imported bank data to the same organizer account if this applies to you. 
Make sure you do not leave a gap between the old and new imports, for example if you previously imported data before the end of the banking day. 

If you have not previously used a different method for bank data imports, you can leave the field empty. 

Click the :btn-icon:fa3-sign-in: Connect with bank: button. 
This takes you to a webpage on ob.gocardless.com which asks you to consent to your data being processed by GoCardless and to provide your bank login. 
Complete the authorization process according to the instructions on the website. 
You will then be redirected back to the pretix backend. 

If your GoCardless account contains information for multiple accounts at the same bank, you have to select the bank account that you want to import data from. 
Choose a start date for importing transactions and confirm by clicking the :btn:Connect to bank: button. 
If you now navigate back to the "Automatic import" page, it will display the bank accounts you selected on the previous page as connected. 
Once the automatic import is active, you should check it for unresolved transactions occasionally. 

The most frequent cause of unresolved transactions is a mistyped or missing order number in the reference line. 
If the bank account is also used for transactions unrelated to sales via pretix, this will produce unresolved transactions as well. 
pretix allows you to resolve these transactions manually. 
The section below explains [how to handle unresolved transactions manually](bank-transfer.md#handling-unresolved-transactions). 

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

"Payer" should contain the name of the person making the payment. 
IBAN and BIC refer to IBAN and BIC of the bank account making the payment. 
IBAN and BIC are optional, but pretix can offer additional functionality if they are provided (such as automatically generating refund files). 

You have two options: importing bank data for all events on the organizer level, or importing bank data for a single event. 
We recommend the first option, unless you have separate bank accounts for every event you are hosting. 
If you want to import data for all events associated with the organizer, navigate to :navpath:Your organizer → :fa3-bank: Bank transfer:. 
This will take you to a page titled "Import bank data". 

If you want to import data for a single event, navigate to :navpath:Your event → :fa3-bank: Bank transfer:. 
This will also take you to a page titled "Import bank data". 
The two pages are very similar, but one is located on the event level and the other is located on the organizer level. 
Whichever option you choose, the process is the same from here on out. 

Click the :btn:Browse...: button and select the export file for upload. 

Click the :btn:Start upload: button. 
pretix will now ask you to specify which column in your file contains which data. 
The screenshot illustrates what such a mapping could look like with a small example CSV file. 

![Import bank data page with a dialog asking the user to assign columns from a CSV file to the data points date, amount, reference, payer, IBAN and BIC. Radio buttons and checkboxes map each type of data to a column in the CSV containing that type of data. ](../../assets/screens/payment-providers/import-bank-data.png "Import bank data" )

Click :btn:Continue:. 
You will be taken to a loading screen while your data is being processed and then to an overview of how many orders were marked as paid, invalid, or ignored. 
Transactions that are already known to the system because they were imported using the same method at an earlier date will be ignored. 

This method may sometimes yield unresolved transactions. 
The most frequent cause of this is a mistyped or missing order number in the reference line. 
If the bank account is also used for transactions unrelated to sales via pretix, this will produce unresolved transactions as well. 
You can intervene and make manual corrections here on this screen. 

Refer to the section below for a more detailed explanation on [how to handle unresolved transactions manually](bank-transfer.md#handling-unresolved-transactions). 

### Approving transactions manually


![Page titled orders, showing a list currently containing one order with status pending, €0.00 out of €250.00 paid.](../../assets/screens/payment/orders.png "Orders" )

In addition to the [automated option A](bank-transfer.md#option-a-automatic-transaction-import-using-gocardless) and the [semi-automated option B](bank-transfer.md#option-b-importing-bank-data) described above, pretix also allows you to approve payments manually. 
In order to do so, navigate to :navpath:Your Event → Orders:. 
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

This takes you back to the "order details" page, now with a notification box at the top saying "The payment has been created successfully" and a green tag in the top right saying ":fa3-check: Paid". 
Repeat this process for every order that shows up in the list on the "orders" page. 

### Handling unresolved transactions

You can handle unresolved transactions either on the organizer level or on the event level. 

If you are using the automated import via GoCardless or have imported bank data on the organizer level, navigate to :navpath:Your organizer → :fa3-bank: Bank transfer:, which lands you on the page titled "Import bank data". 
If you have imported bank data on the event level, navigate to :navpath:Your event → :fa3-bank: Bank transfer:, which lands you on the page titled "Import bank data". 
The process is the same from here on out. 

If there are unresolved transactions, they will be displayed on this page as a list titled "Unresolved transactions". 
For every transaction in this list, you have two options: 
You can either tell pretix to ignore it by clicking the :btn-icon:fa3-trash:: button, or you can search for a matching order and assign the order code to the transaction. 

In order to do so, use the "Order code" field on the unresolved transaction. 
You can enter part of the order code, the buyer's name, one of the attendees' names, or the email address used to place the order.  
Select the matching order from the suggested search results and click the :btn-icon:fa3-check:: button to confirm. 
Repeat this process for all unresolved orders. 

You can view orders by navigating to :navpath:Your event: → :fa3-shopping-cart: Orders:. 

Only delete transactions if they are unrelated to the event you are hosting and no matching order can be found. 
If a transaction has been imported before, it is recognized as a duplicate and ignored upon repeated import, even if the original entry has been deleted. 