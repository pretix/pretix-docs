# Plugins

Plugins are optional pieces of software that can be enabled or disabled for every event. 
Plugins handle functions such as, but not limited to: 

 - native features such as participant badges, emails, and seating plans
 - integrations with payment providers such as Mollie or PayPal
 - integrations with external services such as Google Analytics or Venueless 
 - output formats such as PDF tickets or sales reports 

Some plugins are active by default while others have to be enabled first. 
The availability of plugins depends on the edition of pretix you are using. 
You may have to install plugins before you can enable them. 
If you are using pretix Enterprise, refer to the guide on [installing pretix Enterprise plugins](../../self-hosting/installation/enterprise.md). 

This article explains how to manage pretix plugins that are already available. 
If you want to create a plugin yourself, refer to the developer documentation.

If you want to learn how to activate payment providers for your events, refer to the guide on [payment providers](../payment/index.md). 

## Prerequisites

Plugins are handled on the event level, so you have to create an event first. 

## How To 

In order to enable or disable plugins, navigate to :navpath:Your Event → :fa3-wrench: Settings → Plugins:. 
This lands you on the :btn:Features: tab which lists plugins for optional features. 
More plugins for functions such as integrations with payment providers or other external services can be found on the other tabs at the top of the page. 

On each tab, choose the plugins that you want to use from the top recommendations and the list and click the :btn:Enable: button next to them. 
You can tell that a plugin is enabled by the green "✓ Active" tag and the purple :btn:Enable: button being replaced by a white :btn:Disable: button. 
Disable any active plugins that you do not want to use for your event. 

Most enabled plugins will add a corresponding entry to the sidebar menu via which grants access to its settings. 
