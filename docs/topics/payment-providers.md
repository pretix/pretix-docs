# Payment Providers

Payment providers are the methods by which your customers can pay for their purchases in your ticket shop. They include payment methods that are handled within pretix, such as bank transfers and gift cards, and integrations with external services such as Stripe and PayPal. 

## Prerequisits

Payment providers are handled on the event level. You must create an event before you can set up payment providers. 

Please make sure you have an active account with any payment provider you intend to use with pretix. For example, if you want to receive payments via PayPal, you have to have a PayPal business account. 

## How To 

### Plugins for Payment Providers 

![Plugins Top Recommendations](../../assets/screens/payment-providers/plugins-top.png)

pretix offers more than three dozen payment providers. Each one of them is handled via a plugin. To enable plugins for payment providers, browse to [Your Event] → "Settings" → "Plugins". The "Payment providers" tab displays our top recommendations for payment provider plugins: Bank transfer, Paypal and Stripe. Below the top recommendations, there is a list of plugins for all other payment providers available in pretix. 

![Plugins List](../../assets/screens/payment-providers/plugins-list.png)

Choose the payment providers that you want to use from the top recommendations and the list and click the "Enable" button next to them. You can tell that a plugin is enabled by the green "✓ Active" tag. 

### Settings for Payment Providers 

Browse to [Your Event] → "Settings" → "Payment". The "Payment providers" tab displays the list of active payment providers. Every payment provider that you have enabled the plugin for on the "Plugins" page appears in this list. You can edit and enable the payment providers by clicking the "⚙ Settings" button next to them. 

Each payment method requires some mandatory information and settings before you can enable it. For example, the settings page for bank transfer requires you to enter your bank details and to check a box confirming that you have understood the special conditions that apply to this payment method. 

You can also apply a wide range of optional settings to each payment provider. For example, you can restrict availability of the payment method by date, country and sales channel. 

If the payment provider is an external service, the settings page only contains a button for connecting with your account on that service. For example, the settings page for Stripe contains a "Connect with Stripe" button. Clicking this button redirects you to stripe.com and opens a dialog for authorizing the connection between your Stripe and pretix accounts. Once the connection has been confirmed, the settings page for the payment provider contains the usual mandatory and optional settings. 




## Troubleshooting 

What are common problems that could be encountered here? How do you solve them? 

## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 