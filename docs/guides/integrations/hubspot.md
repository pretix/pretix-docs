# HubSpot

This article explains the HubSpot integration plugin in pretix and what you can do with it. 

## Prerequisites

Plugins are handled on the event level, so you have to create an event first. 
You need to have access to a HubSpot account. 

## How To

This section explains how to enable the HubSpot plugin and how to set up the connection between your pretix account and your HubSpot account. 

In order to activate the HubSpot plugin, navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins: and switch to the :btn:Integrations: tab. 
Click the :btn:Enable: button next to the "HubSpot" plugin. 

Click the :btn-icon:fa3-gear: Settings: drop-down menu next to HubSpot and then click the entry :btn:Settings > HubSpot:. 
This takes you to a page titled "HubSpot Integration". 
In order to set up the connection to HubSpot, click the :btn:Request access: button. 

![Page titled 'HubSpot Integration', displaying a large purple button labeled 'Request access'.](../../assets/screens/hubspot/request-access.png "HubSpot Integration Request access")

This opens a page on HubSpot, prompting you to create a HubSpot account or to sign into your existing one. 

![Page titled 'Connecting your pretix account to HubSpot', displaying the pretix and HubSpot logos and buttons labeled 'Create a new HubSpot account' and 'Sign in to your HubSpot account'.](../../assets/screens/hubspot/connecting.png "Connecting your pretix account to HubSpot")

Click the :btn:Sign in to your HubSpot account: button. 
This takes you to a page prompting you to choose an account

![Page titled 'Connecting pretix to HubSpot', displaying a list of accounts to choose from and a button labeled 'Choose account'.](../../assets/screens/hubspot/choose-account.png "Choose account")

Click your account in the list and then click the :btn:Choose Account: button. 
The next page warns you that you are connecting an unverified app. 

![Page titled 'Connecting pretix to HubSpot', displaying a warning that 'You're connecting an unverified app' and a list of permissions for changes pretix needs to be able to make in HubSpot](../../assets/screens/hubspot/connect-app.png "Connect app")

Scroll to the bottom of the page and click the :btn:Connect app: button. 
Once you have done that, you will be taken back to the HubSpot Integration settings page. 
Instead of the "Request access" button, this page now states that the event is connected to HubSpot and displays settings for object mappings. 

![Page titled 'HubSpot Integration', displaying a green message box saying 'The HubSpot integration is now active', a box with the status of the HubSpot connection, and settings for object mappings.](../../assets/screens/hubspot/integration-active.png "HubSpot Integration active")

Click the :btn:Save: button. 

### Adding customers and attendees to your HubSpot contacts database

This section explains how to add customers or attendees in pretix to your contacts database in HubSpot. 

!!! Note 
    The following paragraphs decide actions you need to take in the HubSpot backend. 
    pretix GmbH is not involved in the development of that software. 
    The process described here may be different due to an update. 

In order to so, you need to create a "pretix-order-id" property in HubSpot. 
pretix will use this property during export. 
Refer to the HubSpot documentation on how to [Create a custom property](https://knowledge.hubspot.com/properties/create-and-edit-properties?hubs_content=knowledge.hubspot.com/properties/export-property-history&hubs_content-cta=kb-breadcrumbs__item#create-a-custom-property).

Add the following property details: 

 - Property label: pretix-order-id
 - Object type: Contact 
 - Group: Order information 
 - Field type: Single-line text

![HubSpot page titled 'Add property details', displaying the properties described above plus an optional description field: 'For importing contact information from pretix'. The 'Field type' is on a separate page. ](../../assets/screens/hubspot/property-details.png "HubSpot Add property details")

Confirm by clicking the :btn:Create: button. 

After you have created the property in HubSpot, switch to the pretix backend. 
Navigate to :navpath:Your Event → :fa3-wrench: Settings → HubSpot:. 
Under "Object mappings", edit the first entry or, if you are already using it for a different purpose, click the :btn-icon:fa3-plus: Add mapping: button. 

Under "pretix object type", choose "Order". 
Under "HubSpot order type", choose "Contacts". 
Click the :btn:Save: button. 

In order to change the details of the data that pretix maps to the entries in HubSpot, click the :btn-icon:fa3-edit: Edit mapping: button. 

The first line under "Properties" specifies the identifier. 
Under "pretix Field", select `Order code [Text (one line)]`. 
Under "HubSpot Field", select `pretix-order-id (pretix_order_id | string)`. 

## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the subject? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant guides, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 