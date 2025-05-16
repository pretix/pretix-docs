# GDPR compliance

!!! Warning

    The pretix Documentation is not legal advice.
    Please consult a lawyer specialized on privacy law for binding legal advice.

## Data processing

<!-- md:hosted -->

When using pretix Hosted, you act as the data controller and we act as the data processor (Art. 28 GDPR).

We strongly recommend that you sign a Data Protection Agreement (DPA) with us to be in compliance with Art. 28 GDPR.
You can do so within your pretix account at :navpath:Your organizer → :fa3-lock: Data protection:.

Unfortunately, we are usually not able to accommodate requests for a customized DPA based on a customer's DPA template.
This is because we act as a processor for a large number of controllers and can only efficiently ensure enforcement of the DPA if the same rules apply across our customer base.

## Processing location

<!-- md:hosted -->

When using pretix Hosted, we only process data within the European Union.
Your data is stored in data centers within Germany.

## Records of processing activities

When describing pretix in your internal record of processing activities (Art. 30 GDPR), we recommend that you describe why you use pretix, what data you configure pretix to collect, and who will receive that data.
We cannot provide you with a template for that description because pretix is used for a large number of purposes. 
Depending on your specific use case, the categories of data subjects and the categories of personal data might be completely different to those of another user of pretix.

## Data protection by design and by default

pretix is designed to minimize risk by collecting only very minimal data in its default configuration (Art. 25 GDPR).
Specifically, in its most simple configuration, pretix will only store the email address entered by the customer and nothing else.
Every other data collection feature can be turned off and is either disabled or optional by default.
It is your obligation to only collect additional personal data that you require to provide your service to your customers.

## Security of processing

pretix applies state-of-the-art security mechanisms (Art. 32 GDPR).
The application supports modern cryptography and authentication schemes.
For pretix Hosted, we take care of automated monitoring and backups.
You can learn more on our website: [security at pretix](https://pretix.eu/about/en/security).

## Rights of the data subject

pretix includes tools to allow you to help your users with exercising their rights.

### Transparent information (Art. 12-13 GDPR)

You can include a link to your privacy policy within pretix at :navpath:Your organizer → :fa3-wrench: Settings → General → Privacy:.
Alternatively, you can include it directly inside pretix using the [pages](https://marketplace.pretix.eu/products/pages/) plugin.

### Right of access (Art. 15 GDPR)

<!-- md:hosted -->

At :navpath:Your organizer → :fa3-lock: Data protection:, we have provided a tool that generates a PDF summary of the data stored within pretix for a specific email address.
You can use this tool to easily provide access to the data on request.

### Right to rectification, erasure, and restriction (Art. 16-18 GDPR)

You can, at any time, modify the data stored in pretix through its interface.
Since pretix is not only affected by privacy regulations, but also needs to provide audit-proof data for tax purposes, some data cannot be modified or will be stored within the historical records even after it has been replaced.
pretix provides a tool to scrub all personal data from an event after the event is over and all financial data has been archived on your end, which can be found at :navpath:Your event → Dashboard → Event status → Cancel or delete event → Delete personal data:.

Additional tools on the level of individual records will be provided in the future.

### Automated decision-making (Art. 22 GDPR)

In our opinion, pretix does not include any functionality that falls under the provisions of Art. 22 GDPR.