# Presale SAML Authentication

This guide explains how to set up strong customer authentication using Security Assertion Markup Language (SAML). 
You can use the plugin "Presale SAML Authentication" to integrate pretix as a service provider (SP) with a SAML identity provider (IdP). 
Once this is set up, customers will have to log in to your SAML IdP during checkout. 

!!! Note 
    SAML authentication is intended for advanced use cases only. 
    If you do not already have a working SAML setup outside of pretix, it is very likely that you do not need to use this feature. 

## Prerequisites 

Before you can use the SAML integration, you need to have access to a 

## How to 

Setting up the SAML integration involves the following steps: 

 1. If you are using pretix Hosted, ask pretix support to unlock the GetYourGuide plugin on your account. 
 If you are using pretix Enterprise, install the plugin and set it up. 
 2. 

### Plugin installation and initial configuration

<!-- md:enterprise -->  

If you are using pretix Enterprise, then you first have to install the plugin "Presale SAML Authentication" and do some setup on your pretix instance. 
These steps are **not** necessary if you are using pretix Hosted. 

Follow the instructions on [how to install pretix Enterprise plugins](../../self-hosting/installation/enterprise.md) in the self-hosting documentation. 

You have to decide if you want your pretix instance to be a single service provider (SP) for all organizers, or if every organizer has to provide their own SP.
A single unified SP makes sense if all organizers hosted on the pretix instance are part of the same organization. 
For example, if your company controls the SP, the pretix instance, and all organizers hosted on it, then a single SP is enough. 

If every organizer is a separate legal entity, then you have to set up the pretix instance so that every organizer has to provide their own SP. 
For example, pretix Hosted as provided on [pretix.eu](https://pretix.eu) serves a multitude of clients. 
Every organizer is a separate legal entity and as such will have to provide their own SP if they need to use the SAML integration. 

If you want to use a single SP for the entire instance, extend the configuration file `<config>` with the following lines: 

``` ini
[presale-saml]
level=global
```

If you want every organizer to provide their own SP, extend the configuration file `<config>` with the following lines instead: 

``` ini
[presale-saml]
level=organizer
```

If you set `level` to `global`, then your instance will use a single system-wide SP
If you set `level`to `organizer`, then the SP will have to be configured for each organizer individually. 
If you do not define `level`, then it defaults to `organizer`. 

### Plugin activation 

<!-- md:hosted -->

If you are using pretix Hosted, the pretix team has to activate the "Presale SAML Authentication" plugin once for your organizer account before you can use it. 
Contact support via [email](mailto:support@pretix.eu) or [phone](tel:+4962213217750) and ask them to activate the SAML plugin. 
Once the plugin has been activated for the organizer account, a button ":fa3-key: SAML" will appear under the organizer settings in the sidebar menu. 

<!-- md:enterprise --> 

If you are using pretix Enterprise and have access to an admin account, you have to activate the "Presale SAML Authentication" plugin once for your organizer account. 
Click the :btn-icon:fa3-id-card: Admin mode: button. 
Navigate to :navpath:Your organizer: → :fa3-wrench: Settings: and open the :btn:General: tab. 
Under "Allow usage of restricted plugins", check the box next to "Presale SAML Authentication" and click the :btn:Save: button. 
A button ":fa3-key: SAML" will now appear under the organizer settings in the sidebar menu. 

Repeat these steps for every organizer account with which you want to use SAML authentication. 

If you are using pretix Enterprise but do not have access to an admin account, ask someone with access to an admin account to perform these steps for you. 

### Setting up the SP 

If you are using pretix Enterprise and want to configure the service provider (SP) for the entire pretix instance, navigate to :navpath::i-pretix: Dashboard:, click the :btn-icon:fa3-id-card: Admin mode: button and then the :btn-icon:fa3-key: SAML: in the sidebar menu. 
If you want to configure the SP for the organizer account, navigate to :navpath:Your organizer → :fa3-key: SAML: instead. 
The process is the same from here on out. 

Setting up the connection between SP and IdP requires a lot of information. 
If you are not sure what which setting you should choose or what information you should provide in any of the fields, contact your IdP operator. 
They should know exactly what information the IdP expects and supports. 

Provide the URL where your IdP outputs its metadata under "IdP Metadata URL". 
For most IdPs, this URL is static and the same for all SPs. 
If you are a member of the DFN-AAI, you can find the metadata for the [Test-, Basic- and Advanced-Federation](https://doku.tid.dfn.de/en:metadata) on their website. 

Contact your IdP operator and ask them whether or not you need to go through the DFN-AAI
It is also possible that you can just use your institution's local IdP, which will also host their metadata on a different URL.

The URL needs to be publicly accessible.
Saving the settings will fail if the IdP metadata cannot be retrieved. 
pretix will automatically refresh the IdP metadata on a regular basis.

Use the system-proposed metadata URL as the "SP Entity Id". 
You can also set any URL as the SP Entity Id if required by your IdP. 

Most IdPs will display the name and description of your SP to the users during authentication. 
The "SP Name" and "SP Decription" fields can be used to explain to the users how their data is being used.

Your SP needs an "SP X.509 Certificate" and an "SP X.509 Private Key". 
Ask your IdP if they can provide you with a certificate and key. 
If not, you need to generate these yourself. 

Certificates have an expiry date and need to be renewed on a regular basis. 
In order to facilitate the rollover from the expiring to the new certificate, you can provide an "SP X.509 New Certificate" before the expiration of the existing one. 
pretix will automatically use the correct one. 
Once the old certificate has expired and is not in use anymore, you can move the new certificate to the "SP X.509 Certificate" field and keep the new slot empty for your next renewal process.

`Requested Attributes`

Not all IdPs use the same attributes to authenticate a user. 
Your IdP will dictate which of the available attributes your SP can receive. 
Use the "Requested Attributes" field to define exactly which attributes the SP should request.
This field comes with a template input that will help you use the proper formatting. 
The notation is a JSON list of objects with 5 properties each:

 - `attributeValue`: can be defaulted to `[]`.
 - `friendlyName`: string used in the event-level settings to retrieve the attribute data.
 - `isRequired`: boolean indicating whether the IdP must enforce the transmission of this attribute. 
   In most cases, `true` is the best choice.
 - `name`: string containing the internal/technical name of the requested attribute. 
   Often starting with `urn:mace:dir:attribute-def:`, `urn:oid:` or `http://`/`https://`.
 - `nameFormat`: String describing the type of `name` that has been set in the previous section. 
   Often starting with `urn:mace:shibboleth:1.0:` or `urn:oasis:names:tc:SAML:2.0:`.

Ask your IdP for a list of available attributes. 
See below for a sample configuration in an academic context. 

!!! Note
    You can have multiple attributes with the same `friendlyName` value but different `name` values. 
    This can be used in cases in which the same information, for example a customer's name, is stored in more than one field. 
    Such a setup may be necessary in a case in which one piece of software returns SAML 1.0 and another piece of software returns SAML 2.0-style attributes. 

    This mostly occurs in mixed environments like the DFN-AAI with a large number of participants. 
    If you are only using your own institution's IdP and not providing authentication for any third parties, then this will probably not apply to you. 

Inquire with your IdP for the correct settings for the checkboxes on the SAML settings page. 
Every checked box improves the security of the setup. 
Some IdP setups may cause problems with some of these settings. 


Choose a "Signature Algorithm" and a "Digest algorithm" that both pretix/your SP and the IdP can communicate with. 
A common source of issues when connecting to a Shibboleth-based IdP is the Digest Algorithm. 
pretix does not support RSA-OAEP and authentication will fail if the IdP enforces this.

Technical contacts and support contacts are encoded into the SPs public metadata. 
They might be displayed to customers if they run into problems while trying to authenticate. 
We recommend providing two dedicated point of contact, one for general support and one for technical issues. 

## Event / Authentication configuration

### Basic settings

Contact support and ask them to unlock the "Presale SAML Authentication" plugin for your account. 
Navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and switch to the :btn:Integrations: tab. 
Click the :btn:Enable: button next to the " Presale SAML Authentication" plugin. 
A new "SAML" menu item will appear now. 

On this page, the actual authentication can be configured.

`Checkout Explanation`

"Since most users probably won't be familiar with why they have to authenticate to buy a ticket, you can provide them a small blurb here. 
Markdown is supported.

`Attribute RegEx`

"By default, any successful authentication with the IdP will allow the user to proceed with their purchase. 
Should the allowed audience needed to be restricted further, a set of regular expressions can be used to do this.

    An Attribute RegEx of `{}` will allow any authenticated user to pass.

    A RegEx of `{ "affiliation": "^(employee@pretix.eu|staff@pretix.eu)$" }` will only allow user to pass which have the `affiliation` attribute and whose attribute either matches `employee@pretix.eu` or `staff@pretix.eu`.

    Please make sure that the attribute you are querying is also requested from the IdP in the first place - for a quick check you can have a look at the top of the page where all currently configured attributes are listed.

`RegEx Fail Explanation`

"Only used in conjunction with the above Attribute RegEx. 
Should the user not pass the restrictions imposed by the regular expression, the user is shown this error message.

    If you are - for example in an university context - restricting access to students only, you might want to explain here that employees are not allowed to book tickets.

`Ticket Secret SAML Attribute`

"In very specific instances, it might be desirable that the ticket secret is not the randomly one generated by pretix but rather based on one of the user's attributes - for example their unique ID or access card number.

    To achieve this, the name of a SAML attribute can be specified here.

    It is however necessary to note that even with this setting in use, ticket secrets need to be unique. 
    This is why when this setting is enabled, the default, pretix-generated ticket secret is prefixed with the attributes value.

    Example: A user's `cardid` attribute has the value of `01189998819991197253`. 
    The default random ticket secret would have been `yczygpw9877akz2xwdhtdyvdqwkv7npj`. 
    The resulting new secret will now be `01189998819991197253_yczygpw9877akz2xwdhtdyvdqwkv7npj`.

    That way, the ticket secret is still unique, but when checking into an event, the user can easily be searched and found using their identifier.

### IdP-provided email addresses, names

By default, pretix will only authenticate the user and not process the received data any further.

However, there are a few exceptions to this rule.

There are a few magic attributes that pretix will use to automatically populate the corresponding fields within the checkout process **and lock them out from user editing**.

> -   `givenName` and `sn`: If both of those attributes are present and pretix is configured to collect the user's name, these attributes' values are used for the given and family name respectively.
> -   `email`: If this attribute is present, the email address of the user will be set to the one transmitted through the attributes.

The latter might pose a problem if the IdP is transmitting an `email` attribute which does contain a system-level mail address which is only used as an internal identifier but not as a real mailbox. 
In this case, please consider setting the `friendlyName` of the attribute to a different value than `email` or removing this field from the list of requested attributes altogether.

### Saving attributes to questions

By setting the `internal identifier` of a user-defined question to the same name as a SAML attribute, pretix will save the value of said attribute into the question.

All the same as in the above section on email addresses, those fields become non-editable by the user.

Please be aware that some specialty question types might not be compatible with the SAML attributes due to specific format requirements. 
If in doubt (or if the checkout fails/the information is not properly saved), try setting the question type to a simple type like "Text (one line)".

## Notes and configuration examples

### Requesting SAML 1.0 and 2.0 attributes from an academic IdP

This requests the `eduPersonPrincipalName` (also sometimes called EPPN), `email`, `givenName` and `sn` both in SAML 1.0 and SAML 2.0 attributes.

``` json
[
    {
        "attributeValue": [],
        "friendlyName": "eduPersonPrincipalName",
        "isRequired": true,
        "name": "urn:mace:dir:attribute-def:eduPersonPrincipalName",
        "nameFormat": "urn:mace:shibboleth:1.0:attributeNamespace:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "eduPersonPrincipalName",
        "isRequired": true,
        "name": "urn:oid:1.3.6.1.4.1.5923.1.1.1.6",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "email",
        "isRequired": true,
        "name": "urn:mace:dir:attribute-def:mail",
        "nameFormat": "urn:mace:shibboleth:1.0:attributeNamespace:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "email",
        "isRequired": true,
        "name": "urn:oid:0.9.2342.19200300.100.1.3",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "givenName",
        "isRequired": true,
        "name": "urn:mace:dir:attribute-def:givenName",
        "nameFormat": "urn:mace:shibboleth:1.0:attributeNamespace:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "givenName",
        "isRequired": true,
        "name": "urn:oid:2.5.4.42",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "sn",
        "isRequired": true,
        "name": "urn:mace:dir:attribute-def:sn",
        "nameFormat": "urn:mace:shibboleth:1.0:attributeNamespace:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "sn",
        "isRequired": true,
        "name": "urn:oid:2.5.4.4",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    }
]
```

### skIDentity IdP Metadata URL

Since the IdP Metadata URL for [skIDentity](https://www.skidentity.de/) is not readily documented/visible in their backend, we document it here: `https://service.skidentity.de/fs/saml/metadata`

### Requesting skIDentity attributes for electronic identity cards

This requests the basic `eIdentifier`, `IDType`, `IDIssuer`, and `NameID` from the [skIDentity](https://www.skidentity.de/) SAML service, which are available for electronic ID cards such as the German ePA/NPA. (Other attributes such as the name and address are available at additional cost from the IdP).

``` json
[
    {
        "attributeValue": [],
        "friendlyName": "eIdentifier",
        "isRequired": true,
        "name": "http://www.skidentity.de/att/eIdentifier",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "IDType",
        "isRequired": true,
        "name": "http://www.skidentity.de/att/IDType",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "IDIssuer",
        "isRequired": true,
        "name": "http://www.skidentity.de/att/IDIssuer",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    },
    {
        "attributeValue": [],
        "friendlyName": "NameID",
        "isRequired": true,
        "name": "http://www.skidentity.de/att/NameID",
        "nameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
    }
]
```
