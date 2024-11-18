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
 This requires adding the pretix application server to your mail server's SPF record (see [Using system email server with a custom sender address](email.md#using-system-email-server-with-a-custom-sender-address) below).
 3. **Use a custom SMTP server:** Use your organization's own SMTP server and fully customize mailing. 

If you want to change the general email settings for an individual event, you can unlock them for that event. 
Unlocking the settings is irreversible. 
Navigate to :navpath:Your event → :fa3-wrench: Settings → E-Mail: and click the :btn-icon:fa3-unlock: Unlock: buttons as required. 

### Using system email server with a custom sender address

If you use an email address with your own domain as the sender address and do not use a custom SMTP server, you have to add the pretix application server to your SPF record.
This is necessary to prevent your emails being misidentified as spam. 

You can add SPF record in the administrative console of the provider with whom you registered your domain.
The exact process varies from provider to provider.
The settings can usually be found on the "DNS records" page or one with a similar name.

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

What follows is a list of all available placeholders, their function and an example. 
Not all placeholders are available for every type of email. 
The available palceholders are listed underneath the email in the backend. 

| Placeholder                        | Function                                                                                                         | Example             | 
|------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------|
| `{attendee_name}`                  | name of the attendee represented by the ticket                                                                   | John Doe |
| `{code}`                           | order code **or** voucher code to redeem for the waiting list                                                    | F8VVL **or** 68CYU2H6ZTP3WLK5 |
| `{comment}`                        | reason for the rejection or cancellation of an order                                                             | An individual text with a reason can be inserted here. |
| `{currency}`                       | three-letter code for the event's currency                                                                       | EUR |
| `{event}`                          | name of the event                                                                                                | Tutorial Conference | 
| `{event_admission_time}`           | admission time of the event                                                                                      | tutcon27 |
| `{event_location}`                 | location of the event                                                                                            | tutcon27 |
| `{event_slug}`                     | short form of the event                                                                                          | tutcon27 |
| `{expire_date}`                    | order expiration date                                                                                            | 2024-11-13 |
| `{hours}`                          | the number of hours the voucher code can be redeemed for the waiting list                                        | 48 |
| `{invoice_company}`                | company from invoice address                                                                                     | Sample Corporation |
| `{invoice_name}`                   | name from invoice address                                                                                        | John Doe |
| `{name}`                           | any name that can be used to address the recipient (e.g. name from invoice address, name from first ticket)      | Mr Doe |
| `{name_family_name}`               | family name of recipient                                                                                         | Doe |
| `{name_for_salutation}`            | preferred address, title and name                                                                                | Dr. Jane Doe |
| `{name_given_name}`                | given name of recipient                                                                                          | John |
| `{order_modification_deadline_date_and_time}` | the deadline date and time for making modifications to the order                                      | June 4, 2027, 6:00 AM    
| `{orders}`                         | list of orders including links to their status pages, specific to the “resend link (requested by user)” e-mail   |  • TUTCON27-F8VVL - https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/open/abcdefghi/ <br> • TUTCON27-HIDHK - https://pretix.eu/tut/tutcon27/order/HIDHK/98kusd8ofsj8dnkd/open/jklmnopqr/ <br> • TUTCON27-OPKSB - https://pretix.eu/tut/tutcon27/order/OPKSB/09pjdksflosk3njd/open/stuvwxy2z/ |
| `{organizer}`                      | name of the organizer                                                                                            | Tutorial Ltd. | 
| `{payment_info}`                   | information about the payment method (e.g. banking details)                                                      | The amount has been charged to your card. |
| `{product}`                        | the product that has become available on the waiting list                                                        | Discount ticket |
| `{refund_amount}`                  | in event cancellation emails, the amount of money that will be refunded, including the currency                  | 42,23 € |
| `{subevent}`                       | the relevant event in an event series                                                                            | Tutorial Conference |
| `{subevent_date_form}`             | the date of the relevant event in an event series                                                                | June 4, 2027, midnight |
| `{total}`                          | invoice total for the order                                                                                      | 42.23 |
| `{total_with_currency}`            | invoice total for the order including localized currency sign                                                    | 42,23 € |
| `{url}`                            | event level: URL pointing to the order's download/status page **or** organizer level: account activation URL     | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/open/98kusd8ofsj8dnkd/ **or** https://pretix.eu/tut/account/activate?token=RAW71yeKrZiYgQCxh7DLLmoQbJePha |
| `{url_cancel}`                     | URL pointing to the order's cancellation page                                                                    | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/cancel |
| `{url_info_change}`                | URL pointing to the order's ticket information page                                                              | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/modify |
| `{url_products_change}`            | URL pointing to the order's products page of the order                                                           | https://pretix.eu/tut/tutcon27/order/F8VVL/6zzjnumtsx136ddy/change |
| `{url_remove}`                     | URL that allows the customer to remove themselves from the waiting list                                          | https://pretix.eu/tut/tutcon27/waitinglist/remove?voucher=68CYU2H6ZTP3WLK5 | 

Clicking the :btn-icon:fa3-tv: Preview: tab gives you a preview of the content with placeholders replaced by examples. 
If you have used a placeholder that is not available for that particular mail, then an error notification is displayed saying "Invalid placeholder: {placeholder}". 

The "Free order" email is sent if a customer places an order exclusively containing free products. 
The "Placed order" email is sent if a customer places an order with a total higher than zero. 
The "Paid order" email is sent after the payment for an order has been registered. 
Depending on the payment method, this can be right after the "Placed order" email. 

### Manually sending out emails 

The settings for emails described above are all tied to certain actions in the pretix backend.
However, you can also send out emails at a time of your choosing. 

If you want to send out an email right away, navigate to :navpath:Your event → :fa3-wrench: :fa3-envelope: Send out emails → Send email:. 
If your email is related to waiting lists, select :btn:Waiting list:. 
In all other cases, select :btn:Orders or attendees:. 

You can restrict the set of recipients by product, order status, time that the order was placed, and check-in status. 
The subject line and message can be customized with text and placeholders. 
Tickets, calendar files or other files can be attached. 
Once you are happy with the email's contents, click :btn:Preview email:. 
The ":fa3-send: Send" button displays the number of matching recipients. 
You can double-check your settings on the preview page and then click :btn-icon:fa3-send: Send (# matching order):