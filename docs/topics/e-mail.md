# Email settings 

pretix offers you many options for contacting your customers and attendees via email—both on the organizer level and on the event level. 
You can use either the system-provided email server or your organization's own. 
pretix comes with many pre-configured email messages that you can customize to your needs. 
This article tells you how to set up your desired email server solution within pretix and how to customize email content. 

## Prerequisites

Your account needs to be activated before you can use pretix to send out emails. 
See the tutorial's section on [account activation](../tutorial/organizer-account.md#activation) for further information. 

## How To 

### General e-mail settings 

By default, the general email settings are handled on the organizer level. 
Navigate to :navpath:Your organizer → :fa3-wrench: Settings → E-Mail:. 
Click the :btn-icon:fa3-edit: Edit: button next to "Sending method" and choose one of the three options: 

 1. **Use system default:** system-provided email server. 
 Emails will be sent from `support@pretix.eu` with your organizer account's name in the name field. 
 The "contact address" you specified for the organizer account under general settings will be used as the reply-to address. 
 2. **Use system email server with a custom sender address:** system-provided email server. 
 Emails will be sent from a custom email address. 
 This requires adding the pretix application server to your mail server's SPF record.
 3. **Use a custom SMTP server:** Use your organization's own SMTP server and fully customize mailing. 

If you want to change the general email settings for an individual event, you can unlock them for that event. 
Unlocking the settings is irreversible. 
Navigate to :navpath:Your event → :fa3-wrench: Settings → E-Mail: and click the :btn-icon:fa3-unlock: Unlock: buttons as required. 

### Using system email server with a custom sender address

If you use an email address with your own domain as the sender address and do not use a custom SMTP server, you have to add the pretix application server to your SPF record.
This is necessary to prevent your emails being misidentified as spam. 
If you are using our hosted service at pretix.eu, you can add the following to your SPF record:

`include:_spf.pretix.eu`

A complete record could look like this:

`v=spf1 a mx include:_spf.pretix.eu ~all`

Consult [the SPF specification](http://www.open-spf.org/SPF_Record_Syntax/) for the proper implementation.

If you want to authenticate your emails with DKIM, set up a `CNAME` record for the subdomain `pretix._domainkey` pointing to `dkim.pretix.eu`:

`pretix._domainkey.mydomain.com. CNAME dkim.pretix.eu.`

Contact our support team to enable DKIM for your domain on our mail servers. 

If you are sending out a large volume of emails, Google Mail also requires you to have a DMARC policy. 
Specifying the DMARC policy as `p=none` is enough. 

### Customizing email content 

Navigate to :navpath:Your organizer → :fa3-wrench: Settings → E-Mail:. 
On the "E-mail content" tab, you can customize the content of emails for customer account registration, email change, and password reset. 
All other types of email content are customized on the event level. 

Navigate to :navpath:Your event → :fa3-wrench: Settings → E-Mail:. 
On the "E-mail content" tab, you can customize the content of emails for orders, purchased products, and payments. 
Emails related to the customer account are handled on the organizer level. 

What follows is a list of all available placeholders and their function: 

| Placeholder | Function              | Example             | 
|-------------|-----------------------|---------------------|
| `{event}`   | the name of the event | Tutorial Conference | 
| `{event_slug}` | the short form of the event | tutcon27 |
| `{code}` | the order code **or** the voucher code to redeem for the waiting list | F8VVL **or** 68CYU2H6ZTP3WLK5 |
| `{currency}` | three-letter code for the event's currency  | EUR |
| `{total}` | invoice total for the order|  |
| `{total_with_currency}` | invoice total for the order including localized currency sign |  |
| `{refund_amount}` | (For cancellation emails) The amount of money that will be refunded, including the currency DEPRECATED?  |  |
| `{payment_info}` | Information text specific to the payment method (e.g. banking details) |  |
| `{url}` | An URL pointing to the download/status page of the order |  |
| `{url_info_change}` | An URL pointing to the page of the order that can be used to change ticket information |  |
| `{url_products_change}` | An URL pointing to the page of the order that can be used to change the products in the order |  |
| `{url_cancel}` | An URL pointing to the page of the order that can be used to cancel the order |  |
| `{name, name_*}` | Any name that can be used to address the recipient (e.g. name from invoice address, name from first ticket, …) |  |
| `{invoice_name, invoice_name_*}` | The name field of the invoice address |  |
| `{invoice_company}` | The company field of the invoice address |  |
| `{attendee_name, attendee_name_*}` | The name of the attendee represented by the ticket |  |
| `{expire_date}` | The order’s expiration date |  |
| `{comment}` | When rejecting an order, this will contain the reason for the rejection |  |
| `{date}` | The same as expire_date, but in a different e-mail (for backwards compatibility) |  |
| `{orders}` | A list of orders including links to their status pages, specific to the “resend link (requested by user)” e-mail |  |
| `{hours}` | In case of the waiting list, the number of hours the voucher code is valid
| `{product}` | In case of the waiting list, the product that has become available |  |
| `{voucher_list}` | When sending out vouchers in bulk, this will be replaced with the list of vouchers |  |

	

	


	



	



	

