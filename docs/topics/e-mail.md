# Email settings 

pretix offers you many options for contacting your customers and attendees via email—both on the organizer level and on the event level. 


## Prerequisites

Your account needs to be activated before you can use pretix to send out emails. 
See the tutorial's section on [account activation](../tutorial/organizer-account.md#activation) for further information. 

## How To 

Navigate to :navpath:Your organizer → :fa3-wrench: Settings → E-Mail:. 

On the "E-mail content" tab, you can customize the content of emails for customer account registration, email change, and password reset. 
All other types of email content are customized on the event level. 

Navigate to :navpath:Your event → :fa3-wrench: Settings → E-Mail:. 
On the "E-mail content" tab, you can customize the content of emails for orders, purchased products, and payments. 
Emails related to the customer account are handled on the organizer level. 


## Troubleshooting 

If you use an email address with your own domain as the sender address and do not use a custom SMTP server, it is very likely that at least some of your emails will go to the spam folders of their recipients. 
If you do not want to or cannot use your organization's own SMTP server, you should add the pretix application server to your SPF record.
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

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

