# Payment Providers

Payment providers are the means by which your customers can pay for their purchases in your ticket shop. They include payment methods that are handled within pretix, such as bank transfers and gift cards, and integrations with external services such as Stripe and PayPal. 

## Prerequisits

Payment providers are handled on the event level, so you must create an event before you can set up payment providers. 

Please make sure you have an active account with each payment provider you intend to use with pretix. For example, if you want to receive payments via PayPal, you have to have a PayPal business account. 

## How To 

Setting up payment providers in pretix involves the following steps: 

 1. Enable the plugin for the payment provider
 2. Connect to your account with the payment provider 
 3. Enter mandatory info on the settings page for the payment provider
 4. Make optional adjustments
 5. Enable the payment provider
 6. Repeat steps 1. through 5. for every payment provider you want to use
 7. Set deadlines and advanced settings

The following sections will guide you through those steps in detail. 

### Plugins for Payment Providers 

![Plugins Top Recommendations](../../assets/screens/payment-providers/plugins-top.png)

pretix offers more than three dozen payment providers. Each one of them is handled by a plugin. To enable plugins for payment providers, browse to [Your Event] → "Settings" → "Plugins". The "Payment providers" tab displays our top recommendations for payment provider plugins: Bank transfer, PayPal and Stripe, and below that, the list of plugins for all other payment providers available in pretix. By default, the plugins for Bank transfer, PayPal, Stripe and SEPA Direct debit will be active. 

![Plugins List](../../assets/screens/payment-providers/plugins-list.png)

Choose the payment providers that you want to use from the top recommendations and the list and click the :btn:Enable: button next to them. You can tell that a plugin is enabled by the green "✓ Active" tag. You can disable the default plugins that you don't want to use. 

### Settings for Payment Providers 

![Payment Settings](../../assets/screens/payment-providers/payment-settings.png)

Browse to [Your Event] → "Settings" → "Payment". The "Payment providers" tab on this page displays the list of active payment providers. Every payment provider that you have enabled the plugin for on the "Plugins" page appears in this list. By default, this list includes Bank transfer, Gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. You can edit and enable the payment providers by clicking the :btn:⚙ Settings: button next to them. 

Each payment method requires some mandatory information and settings before you can enable it. For example, the settings page for bank transfer requires you to enter your bank details and to check a box confirming that you have understood the special conditions that apply to this payment method. 

You can also apply a wide range of optional settings to each payment provider. For example, you can restrict availability of the payment method by date, country and sales channel. 

![Payment External](../../assets/screens/payment-providers/payment-external.png)

If the payment provider is an external service, the settings page only contains a button for connecting with your account on that service. For example, the settings page for Stripe contains a :btn:Connect with Stripe: button. Clicking this button redirects you to stripe.com and opens a dialog for authorizing the connection between your Stripe and pretix accounts. Once the connection has been confirmed, the settings page for the payment provider contains the usual mandatory and optional settings. 

### Deadlines

![Payment Deadlines](../../assets/screens/payment-providers/payment-deadlines.png)

Browse to [Your Event] → "Settings" → "Payment". The "Deadlines" tab lets you set payment terms measured in either days or minutes. By default, the payment term for your customers is set to 14 days. This page also lets you make optional adjustments such as a last day of payment, an additional expiration delay beyond the time communicated to your customer, and the option to only end payment terms on weekdays. 

!!! Note
 
    Payment deadlines are configured on the event level. The same settings apply to all payment providers. 

## Troubleshooting 

__A payment provider does not show up in [Your Event] → "Settings" → "Payment"__
Browse to [Your Event] → "Settings" → "Plugins" and open the "Payment providers" tab. Enable the corresponding plugin. Make sure it has the green "✓ Active" tag next to it. 

__A payment provider does not show up in your test shop/Customers cannot select a payment method during their purchase__ 
Browse to [Your Event] → "Settings" → "Payment" and open the "Payment" tab. Click the :btn:⚙ Settings: button next to the payment provider that isn't showing up in the shop. Check the "☑ Enable payment method" box. Then scroll to the bottom of the page and click :btn:Save:. If any mandatory information hasn't been filled out yet, the webpage will notify you. Fill out all the mandatory information and click :btn:Save: again. The corresponding payment method should now show up in your online shop. 


## Further Information

What other media do we have on the topic? Youtube videos, PDF handouts, vendor documentation (for plugins etc.) etc.? Link it here and explain what it does

## See Also 

Link to other relevant topics, for example, in the case of Payment Providers, link to the articles on payment settings and plugins. Do not link to pages already linked underneath the title heading, prerequisites, or further information. 