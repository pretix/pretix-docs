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

To connect an external application as a SSO client, go to “Customer accounts” → “SSO clients” → “Create a new SSO client” in your organizer account.

You will need to fill out the following fields:

Active

    If this checkbox is removed, the SSO client can not be used.
Application name

    The name of your external application, e.g. “digital event marketplace”.
Client type

    For a server-side application which is able to store a secret that will be inaccessible to end users, chose “confidential”. For a client-side application, such as many mobile apps, choose “public”.
Grant type

    This value depends on the OpenID Connect implementation of your software.
Redirection URIs

    One or multiple URIs that the user might be redirected to after the successful or failed login.
Allowed access scopes

    The types of data the SSO client may access about the customer.

After you submitted all data, you will receive a client ID as well as a client secret. The client secret is shown in the green success message and will only ever be shown once. If you need it again, use the option “Invalidate old client secret and generate a new one”.

You will need the client ID and client secret to configure your external application. The application will also likely need some other information from you, such as your issuer URI. If you use pretix Hosted and your organizer account does not have a custom domain, your issuer will be https://pretix.eu/myorgname, where myorgname is the short form of your organizer account. If you use a custom domain, such as tickets.mycompany.net, then your issuer will be https://tickets.mycompany.net.
Technical details

We implement OpenID Connect Core 1.0, except for some optional parts that do not make sense for pretix or bring no additional value. For example, we do not currently support encrypted tokens, offline access, refresh tokens, or passing request parameters as JWTs.

We implement the provider metadata section from OpenID Connect Discovery 1.0. You can find the endpoint relative to the issuer URI as described above, for example http://pretix.eu/demo/.well-known/openid-configuration.

We implement all three OpenID Connect Core flows:

    Authorization Code Flow (response type code)

    Implicit Flow (response types id_token token and id_token)

    Hybrid Flow (response types code id_token, code id_token token, and code token)

We implement the response modes query and fragment.

We currently offer the following scopes: openid, profile, email, phone

As well as the following standardized claims: iss, aud, exp, iat, auth_time, nonce, c_hash, at_hash, sub, locale, name, given_name, family_name, middle_name, nickname, email, email_verified, phone_number.

The various endpoints are located relative to the issuer URI as described above:

    Authorization: <issuer>/oauth2/v1/authorize

    Token: <issuer>/oauth2/v1/token

    User info: <issuer>/oauth2/v1/userinfo

    Keys: <issuer>/oauth2/v1/keys

We currently do not reproduce their documentation here as they follow the OpenID Connect and OAuth specifications without any special behavior.

#### Using pretix as a Single Sign-On client 

To connect an external application as an SSO client, go to “Customer accounts” → “SSO providers” → “Create a new SSO provider” in your organizer account.

The “Provider name” and “Login button label” is what we’ll use to show the new login option to the user. For the actual connection, we will require information such as the issuer URL, client ID, client secret, scope, and field (or claim) names that you will receive from your SSO provider.

Note

If you want your customers to only use your SSO provider, it makes sense to turn off the “Allow customers to log in with email address and password” settings option (see above).
Technical details

We assume that SSO providers fulfill the following requirements:

    Implementation according to OpenID Connect Core 1.0.

    Published meta-data document at <issuer>/.well-known/openid-configuration as specified in OpenID Connect Discovery 1.0.

    Support for Authorization code flow (response_type=code) with response_mode=query.

    Support for client authentication using client ID and client secret and without public key cryptography.

## Troubleshooting 

What are common problems that could be encountered here? 
How do you solve them? 

## Further Information

What other media do we have on the topic? 
Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? 
Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. 
Do not link to pages already linked underneath the title heading, prerequisites, or further information. 
