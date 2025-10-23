# Accessibility

The accessibility of your pretix ticket shop is not only important from ethics and business standpoints, but also a legal obligation.
As of 2025, the [European Accessibility Act](https://en.wikipedia.org/wiki/European_Accessibility_Act) and its national implementation laws mandate that all websites that are used to close contracts with consumers need to be in compliance with accessibility standards.
If you operate an online shop selling products or services to consumers within the EU, then this applies to you. 
This includes ticket shops created using pretix. 

The relevant European norm, [EN 301 549](https://en.wikipedia.org/wiki/EN_301_549), refers to the [WCAG 2.1 AA](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) standard.
Therefore, we develop pretix in a way that makes it easy for you to achieve **WCAG 2.1/2.2 AA** compliance for your ticket shop.

## Your responsibilities

pretix is not a ticket shop, but rather a software to create ticket shops.
As such, the real-world accessibility of the shop depends on a combination of our efforts in creating the software and your efforts in configuring it for good accessibility.
It is your responsibility to choose configuration parameters for pretix that are in line with accessibility requirements.
These are some of the steps you should take to fulfill these requirements:

- Use user-configured colors that are [well-distinguishable](https://www.w3.org/TR/WCAG22/#use-of-color) and provide [sufficient contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum) to surrounding colors.

- Provide any information that you [present as images](https://www.w3.org/TR/WCAG22/#images-of-text) (such as the header image or product pictures) also as text on the same page. 

- When providing formatted text using [Markdown](../guides/markdown.md), make sure to make semantically correct use of the markup. 
We recommend not using headlines (``##``) or HTML tags. 

- Select payment providers that provide good accessibility support.

- When embedding the [widget](../guides/widget.md), make sure that the CSS styling on the embedding website does not interfere with the accessibility and make sure that the user's path to the widget is also accessible.

- Use simple language e.g. for your event description, product titles, etc.
 
Due to the multitude of configuration options that pretix offers, we cannot provide an exhaustive list of steps you need to take in order to guarantee that your shop fulfills all accessibility requirements.

## Declaration of accessibility

Depending on your jurisdiction, you might need to publish information on the accessibility of your ticket shop.
You can embed this information using the configuration options at :navpath:Your organizer → :fa3-wrench: Settings → General → Accessibility:. 

Here is a Markdown-formatted sample based on the requirements of German law for a non-governmental entity.

!!! Warning 
    The pretix documentation is not legal advice. 
    The information below is provided **without warranty**. 
    Feel free to use it at your own risk.

```
# Sample information of accessibility

## General description

This website lets you purchase tickets for our events. You can find further information on each event in that event's description.

The following payment methods are available for ticket purchases:

- to be filled in

## Information on the provider

_Max Mustermann, Sesamstraße 1, 12345 Berlin, Phone: 0815 12345678, Email: mustermann@example.org._

## Compliance with accessibility requirements

The following standards and guidelines were used to ensure the accessibiltiy of this ticket shop:

- Harmonized European standard EN 301 549 V3.2.1
- Web Content Accessibility Guidelines (WCAG), V2.2, levels A and AA

Our offer is based on standardized ticket shop software. The software provider has worked with digital accessibility experts to optimize this software. External experts have tested the accessibility of several example shops. The software provider continues to regularly conduct internal automated or manual tests. 

During the configuration of the software for our ticket shop, we have implemented the provider's guidelines for an accessible ticket shop.

This ticket shop meets accessibility requirements using the following measures:

- The ticket shop is well-structured with informative and meaningfully structured headlines and descriptions. Links are clearly recognizable and labelled with informative text. 
- You can use this ticket shop with assistive devices such as screen readers without losing information.
- You can use and navigate this ticket shop with an external keyboard. This is true for all elements and functions. Navigation occurs in meaningful order. When you select interactive elements such as links or buttons with a keyboard, they are visibly highlighted (focus indicator). 
- Text and visual content has high contrast. You can adjust the visual presentation (e.g. text size) with your browser and/or operating system settings. All content is distinguishable without color perception. There are text alternatives for all non-text content. 
- Our ticket shop works in portrait and landscape display orientations. Elements, content and functions adapt to these orientations automatically.
- You do not have to be able to listen or speak to use our ticket shop.
- If a booking process has a time limit, then you are warned in reasonable time before it expires. You can then extend this time limit.
- The ticket shop is designed to help you avoid errors and correct errors. 
- You can use this ticket shop without complex, path-dependent, or simultaneous input. 
- The ticket shop does not contain any light effects or flashes known to cause photosensitive seizures. 

For feedback on the accessibility of this ticket shop, please refer to the contact details listed at "Information on the provider" above.

## Competent market surveillance authority

State market surveillance authority for the accessibility of goods and services (Marktüberwachungsstelle der Länder für die Barrierefreiheit von Produkten und Dienstleistungen, MLBF) in Magdeburg (Saxony-Anhalt).
```

**Attention for public authorities:** The new laws apply in addition to the existing laws based on the [Web Accessibility Directive](https://en.wikipedia.org/wiki/Web_Accessibility_Directive).
The earlier law, which only applies to public authorities, requires a declaration of accessibility that goes beyond the information required by the new laws.
The EU Commission has published an [official template](https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32018D1523) for the structure of such a declaration.

## Accessibility testing

External experts have tested the accessibility of several example shops. 
The last round of tests was between November 2024 and May 2025.

!!! Note

    At the moment, our accessibility commitment is only valid for the ticket shops created with pretix.
    We are working on improving accessibility of the pretix backend, but we have not yet performed intensive accessibility testing or updated the backend accordingly. 
    Our current priority are the ticket shops. 

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