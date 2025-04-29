# GDPR compliance

## Data processing

<!-- md:hosted -->

When using pretix Hosted, you act as the data controller and we act as the data processor (Art. 28 GDPR).

We strongly recommend that you sign a Data Protection Agreement (DPA) with us to be in compliance with Art. 28 GDPR.
You can do so within your pretix account at :navpath:Your organizer → :fa3-lock: Data protection:.

Unfortunately, we are usually not able to accommodate requests for a customized DPA based on a customer's DPA template.
This is because we act as a processor for a large number of controllers and can only efficiently ensure enforcement of the DPA when the same rules apply across our customer base.

## Processing location

<!-- md:hosted -->

When using pretix Hosted, we only process data within the European Union.
At the moment, all of our data centers are located within Germany.

## Records of processing activities

When describing pretix in your internal record of processing activities (Art. 30 GDPR), we recommend that you describe why you use pretix, what data you configure pretix to collect, and who will receive that data.
Unfortunately, we are unable to provide you with a template for pretix is used for a wide number of purposes and depending on your specific use cases, the categories of data subjects and the categories of personal data might be completely different to those of another user of pretix.

## Data protection by design and by default

pretix is designed to minimize the risks by collecting only very minimal data in its default configuration.
Specifically, in its most simple configuration, pretix will only store the email address entered by the customer and nothing else.
Every other data collection feature can be turned off and is either disabled or optional by default.
It is your obligation to only collect additional personal data that you require to provide your service to your customers.

## Security of processing

pretix applies state-of-the-art security mechanisms.
The application supports modern cryptography and authentication schemes.
For pretix Hosted, we take care of automated monitoring and backups.
You can learn more [on our website](https://pretix.eu/about/en/security).

## Rights of the data subject

pretix includes tools to allow you to help your users with exercising their rights.

### Transparent information

You can include links to your privacy policy within pretix, or even include it directly inside pretix using the [pages](https://marketplace.pretix.eu/products/pages/) plugin.

### Right of access

<!-- md:hosted -->

At :navpath:Your organizer → :fa3-lock: Data protection:, we have provided a tool that generates a PDF summary of the data stored within pretix for a specific email address.
You can use this tool to easily provide access to the data on request.

### Right to rectification, erasure, and restriction

You can, at any time, modify the data stored in pretix through its interface.
Since pretix is not only affected by privacy regulations, but also needs to provide audit-proof data for tax purposes, some data cannot be modified or will be stored within the historical records even after it has been replaced.
pretix provides a tool to scrub all personal data from an event after the event is over and all financial data has been archived on your end, which can be found at :navpath:Your event → Dashboard → Event status → Cancel or delete event → Delete personal data:.

Additional tools on the level of individual records will be provided in the future.
