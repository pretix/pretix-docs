# Accessibility

The accessibility of your pretix ticket shop is not only important from ethics and business standpoints, but also a legal obligation.
As of 2025, the [European Accessibility Act](https://en.wikipedia.org/wiki/European_Accessibility_Act) and its national implementation laws mandate that all websites that are used to close contracts with consumers need to be in compliance with accessibility standards.
If you operate an online shop selling products or services to consumers within the EU, then this applies to you. 
This includes ticket shops created using pretix. 

The relevant European norm, [EN 301 549](https://en.wikipedia.org/wiki/EN_301_549), refers to the [WCAG 2.1 AA](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) standard.
Therefore, we develop pretix in a way that makes it easy for you to achieve **WCAG 2.1/2.2 AA** compliance for your ticket shop.

## Your responsibilities

pretix is not a ticket shop, but rather a software to create ticket shops.
As such, the real-world accessibility of the shop depends on a combination of our efforts of creating the software and your efforts of configuring it for good accessibility.
It is your responsibilities to choose configuration parameters for pretix that are in line with accessibility requirements.
This includes, but is not limited to:

- Use user-configured colors that are [well-distinguishable](https://www.w3.org/TR/WCAG22/#use-of-color) and provide [sufficient contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) to surrounding colors.

- Provide any information that you [present as images](https://www.w3.org/TR/WCAG22/#images-of-text) (such as the header image or product pictures) also as text on the same page. 

- When providing formatted text using [Markdown](../guides/markdown.md), make sure to make semantically correct use of the markup. 
We recommend against using headlines (``##``) or HTML tags in most cases.

- Select payment providers that provide good accessibility support.

- When embedding the [widget](../guides/widget.md), make sure that the CSS styling on the embedding website does not interfere with the accessibility and make sure that the users path to the widget is also accessible.

## Declaration of accessibility

Depending on your jurisdiction, you might need to publish information on the accessibility of your ticket shop.
You can embed this information using the configuration options at :navpath:Your organizer → :fa3-wrench: Settings → General → Accessibility:. 

Here is a Markdown-formatted sample based on the requirements of German law for a non-governmental entity.
!!! Warning 
    The pretix documentation is not legal advice. 
    The information below is provided **without warranty**. 
Feel free to use it at your own risk.

```
TODO
```

## Accessibility testing

To ensure that our ticket shops are accessible, we have conducted testing of by external experts.
These last round of tests was between November 2024 and May 2025.

!!! Note

    At the moment, our accessibility commitment is only valid for the ticket shops created with pretix.
    For other functionality, such as the pretix backend, we are also working to improve accessibility, but we have prioritized the ticket shops and have not yet performed intensive accessibility testing and improvements on the backend.

### Scope of testing

Due to the complex and highly configurable nature of pretix, it is impossible to test all possible configurations.
Therefore, we performed the test on sample ticket shops and attempted to include as many pretix features and configurations as possible.
If a configuration, plugin, or process is not listed here, then we did not include it in our accessibility tests.
If you require proof of compliance for your individual pretix ticket shop, then you need to perform your own tests.

The accessibility tests included **all core system functions** as well as the following plugins:

- Bank transfer
- Double opt-in step 
- Passbook tickets
- PDF ticket output
- Newsletter integration (rapidmail used as an example)
- Pages
- Seating
- Shipping

We tested the following features of pretix for accessibility: 

#### Organizer pages

- Switching the page language.
- Exploring the list of events through list and calendar views.
- Getting in touch with the organizer.
- Creating a customer account.
- Logging in to a customer account.
- Performing a customer account password reset.
- Updating customer account information.
- Viewing memberships, recent orders, stored addresses, and profiles.

#### Event pages

- Navigating the dates of an event series.
- Discovering all event information (date, time, location, description).
- Discovering and navigating the list of products including reduced tickets, sold-out tickets, tickets with variations, tickets with a waiting list, and tickets that require a voucher.
- Discovering and navigating the seating plan.
- Signing up for the waiting list for a sold-out ticket.
- Adding tickets to the cart. 
- Interacting with the cart. 
- Selecting add-on and cross-selling products.
- Going through checkout without creating a customer account, using an existing customer account, or creating a customer account.
- Answering custom questions of various types.
- Completing the double-opt-in step.
- Selecting a shipping method.
- Selecting a payment method (We did not test any external components of payment methods).
- Clicking consent checkboxes before confirming the order.
- Completing the order.

#### Widget

- Discovering and navigating the list of products.
- Navigating the event dates of an event series in a calendar view.
- Going directly to checkout with the pretix button.