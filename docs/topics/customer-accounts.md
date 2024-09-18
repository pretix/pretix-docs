# Customer accounts 

pretix allows your customers to use your ticket shop without having to create an account. 
However, pretix also lets you enable customer accounts. 
Customer accounts have three advantages: 

First, they allow your customers to log back in to their account to make adjustments to their personal data and attendee profiles. 
Second, they give you more fine-grained control over customer accounts, personal data, and the orders placed through them. 
Third, they allow you to grant memberships to your customers, which can then be used for season passes, special members-only offers, and reusable media. 

!!! Note 
    Customer accounts and memberships are not the same thing. 
    Customer accounts are usually created by the customers themselves. 
    Activating customer accounts is a prerequisite for access to the memberships feature. 
    Having access to a customer account is a prerequisite for getting access to a membership. 

    Memberships are usually assigned to a customer account with the purchase of a product and can then be used for exclusive discounts and access to products. 

This article tells you how to enable and manage customer accounts. 

## Prerequisites

Customer accounts are handled on the organizer level. 
You need access to an organizer account if you want to enable customer accounts. 

## General usage

Customer accounts are always tied to the organizer account. 
Once a customer has created an account while placing an order for one of your events, they will be able to log in and place an order through the same account for all events managed by the same organizer account. 
Customers may **not** log in to the same customer account with a different organizer. 

It is not possible to activate or deactivate customer accounts on a per-event basis. 
It is also not possible to force customers to create an account. 
The option to place an order as a guest is always available. 

![Organizer settings page, on the customer accounts tab, showing options for whether or not to allow customers to create accounts, whether or not to match orders based on mail addresses, as well as options for name formatting and allowed titles](../assets/screens/organizer/customer-accounts.png) 

If you want to allow your customers to create accounts, navigate to :navpath:Your organizer → Settings → General:, open the :btn:Customer accounts: tab, and check the box next to "Allow customers to create accounts". 

Checking that box makes another box appear that is checked by default: "Allow customers to log in with email address and password". 
Keep this box checked if you want customers to log in to your pretix ticket shop directly. 
Uncheck it if you want them to log in via an external single sign-on service only. 

By default, customers will be able to view and edit orders placed with the same customer account. 
If you check the box next to "Match orders based on email address", they will also be able to view and edit any orders that have been placed with the same email address without logging in. 

### Customer accounts from the customers' perspective 

From your customers' perspective, a pretix ticket shop is perfectly usable without creating an account. 
Giving your customers the option to create an account makes sense if you expect them to place orders repeatedly and to access and change their own account information after placing an order. 

![Page for an order at an organizer named 'Tutorial Ltd.', displaying an order with pending payment.](../assets/screens/customer-accounts/order-details.png) 

If a customer places an order without creating and logging in to a customer account, they receive an email with a URL. 
The URL points to a page on which they can make a payment, download their ticket, as well as change the details of their orders, shipping, and personal information. 
The URL is specific to that order. 

!['Your account' page for an organizer named 'Tutorial Ltd.', displaying account information, orders, memberships, addresses, attendee profiles, and options to view and edit those.](../assets/screens/customer-accounts/your-account.png) 

If the customer creates an account and then logs into that account, they will see an overview of their orders which they can view and edit individually just like described above. 
They will also be able to view and edit their memberships, addresses, attendee profiles, account information, and password. 

### Managing customer accounts 

Navigate to :navpath:Your organizer → :fa3-user: Customer accounts → Customers:. 
This menu option will only appear if customer accounts are enabled in the organizer account settings. 
The "Customers" page displays a list of all customer accounts known to your organizer account with their "Customer ID", email address, name, and optional "External identifier". 

The page gives you the option to search and filter customer accounts as well as to create a new one with the :btn-icon:fa3-plus: Create a new customer: button. 
pretix will automatically generate a "Customer ID" for every customer account. 
You can change this customer ID manually during creation. 
It serves as the accounts unique identifier and cannot be changed after the account has been created. 
The identifier may only contain letters, numbers, dots, dashes, and underscores. 
It must start and end with a letter or number. 

The only other mandatory piece of information for a customer account is the associated email address. 

The customer can only log in to their account if the boxes next to "Account active" **and** "Verified email address" are checked. 
The "Verified email address" box will be checked automatically as soon as the customer clicks the link in the verification email or password reset email. 

If you already have customer accounts in a different software, then it makes sense to fill the "External identifier" field with the unique identifier of the account from the other software. 
If you want to import, export, or sync data between pretix and another software, then it makes sense to fill this field automatically using an integration with the pretix API. 

Entries in the "Notes" field will only be visible to you and your team; they will not be visible to the customer. 

### Single Sign-On (SSO) 

"Single sign-on" or SSO refers to a setup that allows users to sign in to multiple systems (e.g. apps or websites) with a single set of login data. 
It makes sense to implement SSO if pretix is just one of multiple applications you are planning for your customers to use. 
This has the advantage of unburdening your customers from memorizing the difference between your various systems and keeping track of different usernames and passwords for them. 
With an SSO setup, your customers can use the same credentials for every interaction with your company or your brand. 

You can use pretix as an SSO provider. 
Customers will be able to create a pretix account and then use that account for all other applications you connect as SSO clients with pretix serving as the single source of truth (SSOT). 

You can also use pretix as the SSO client. 
If you are already using a different SSO provider that serves as the single source of truth (SSOT) for your applications, you can connect pretix as an SSO client. 
This means that customers will be able to log into your pretix shop and make purchases there using your existing SSO setup. 

All SSO support for customer accounts in pretix is currently built on the OpenID Connect standard, a modern and widely accepted standard for SSO in all industries.

#### Using pretix as an SSO provider 

If you want to use pretix as an SSO provider, navigate to :navpath:Your organizer → :fa3-user: Customer accounts → SSO clients: and click the :btn-icon:fa3-plus: Create a new SSO client: button. 

The checkbox next to "Active" is enabled by default. 
Disable it if you want to disable SSO integration with the client in question. 

Insert an unambiguous name in the "Application name" field. 

Under "Client type", choose "Confidential" if the server-side application is able to store a secret that will be inaccessible to end users.
For a client-side application such as a typical mobile apps, choose "Public".

Your choice for the "Grant type" depends on the implementation of the OpenID Connect standard used by the application you are connecting. 

Enter one or multiple URIs that the user might be redirected to after the successful or failed login into the "Redirection URIs" field. 

Under "Allowed access scopes", check the boxes for which you want to grant access to the application. 

Once you click the :btn:Save: button, the client secret will be displayed at the top of the page. 
The client secret will only be displayed once. 
Copy and paste it to your application. 
You will also need the "Client ID" which will be displayed in a new field underneath "Application name". 

If you need a new client secret, check the box next to "Invalidate old client secret and generate a new one" and click the :btn:Save: button. 
The old client secret will not be usable anymore. 
The new client secret will be displayed in a green box at the top of the page. 

Beyond the client ID and secret, the service you are connecting is also going to need your issuer URI. 
If you are using pretix Hosted without a custom domain, your issuer URI will be the address of your organizer's public profile **without** the final slash. 
For instance, the issuer URI of our Tutorial Ltd. with the organizer short form will be [https://pretix.eu/tut](https://pretix.eu/tut). 

If you are using a custom domain, then your issuer URI will be the custom domain preceded by "https://". 
For instance, if your custom domain is tickets.mycompany.net, then your issuer URI will be [https://tickets.mycompany.net](https://tickets.mycompany.net). 

#### Using pretix as a Single Sign-On client 

If you want to use pretix as an SSO client, navigate to :navpath:Your organizer → :fa3-user: Customer accounts → SSO providers: and click the :btn-icon:fa3-plus: Create a new SSO provider: button. 

Choose a "Provider name" and "Login button label". 
These texts will be used as a label for the login option in your shop. 
Under "Single-sign-on method", choose "OpenID Connect". 
Fill out the fields that are displayed after you selected "OpenID Connect" with the information from your SSO provider. 

If you want your customers to log in via SSO only and not create accounts via pretix directly, navigate to :navpath:Your organizer → Settings → General:, open the :btn:Customer accounts: tab, and uncheck the box next to "Allow customers to log in with email address and password". 