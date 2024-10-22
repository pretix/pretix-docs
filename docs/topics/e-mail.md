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