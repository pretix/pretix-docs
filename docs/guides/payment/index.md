# Payment

If you are not operating an entirely free shop, your customers need some way of sending you payments. 
pretix takes care of payment via a wide selection of payment providers. 
There are two types of payment providers: 

 - methods that are handled entirely within pretix, such as bank transfers and gift cards 
 - integrations with external services such as Stripe and PayPal 

You have to enable and set up at least one payment provider if you want to receive payments from your customers via pretix. 
This article will show you how to do that. 
It will also tell you how to take some optional steps such as setting up additional fees or deadlines. 

## Prerequisites

Setting up payment providers is handled on the event level, so you need to create an event first. 

Make sure you have an active account with each external payment provider you intend to use with pretix. 
For example, if you want to receive payments via PayPal, you need to have a PayPal business account. 

## How To 

Setting up payment providers in pretix involves the following steps: 

 1. [Enable the plugin](index.md#plugins-for-payment-providers) for the payment provider
 2. Connect to your account with the payment provider 
 3. Enter mandatory info on the [settings page](index.md#general-settings-for-payment-providers) for the payment provider
 4. Make optional adjustments, such as adding [additional fees](index.md#additional-fees)
 5. Enable the payment provider for use in your shop
 6. Repeat steps 1 through 5 for each payment provider you want to use
 7. Set [deadlines](index.md#deadlines) and advanced settings

The following sections will guide you through those steps in detail. 

### Plugins for Payment Providers 

pretix allows handling payment via more than three dozen payment providers. 
There is a plugin for each one of them. 
You have to enable the plugins for every payment provider that you want to use for your event. 
This section is going to tell you how to do that. 

![Top recommendations for available payment provider plugins. The Top recommendations are bank transfer, PayPal and Stripe. All of them have a green 'active' tag and a 'disable' button next to them.](../../assets/screens/payment-providers/plugins-top.png "Plugins Payment providers top recommendations")

Navigate to :navpath:Your Event → Settings → Plugins:. 
The :btn:payment providers: tab displays our top recommendations for payment provider plugins: bank transfer, PayPal and Stripe at the top of the page. 
Below that, you can find the list of plugins for all other payment providers available in pretix. 
By default, the plugins for bank transfer, PayPal, Stripe and SEPA Direct debit will be active. 

![Part of the list of available payment provider plugins. Entries for Saferpay, secuconnect, SEPA direct debit, SOFORT and Stadtguthaben are visible. The SEPA option is active. The other entries have a purple 'enable' button next to them.](../../assets/screens/payment-providers/plugins-list.png "Plugins Payment providers list")

Choose the payment providers that you want to use from the top recommendations and the list and click the :btn:Enable: button next to them. 
You can tell that a plugin is enabled by the green "✓ Active" tag and the purple :btn:Enable: button being replaced by a white :btn:Disable: button. 
Disable any active plugins that you do not want to use for your event. 

### General settings for Payment Providers 

Enabling a plugin does not automatically make the payment method available in your shop. 
You also need to provide some data for each payment provider you want to use on the settings page. 
This section is going to tell you how to do that. 

Navigate to :navpath:Your Event → Settings → Payment:. 
The :btn:Payment providers: tab on this page displays the list of active payment providers. 
By default, this list includes bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. 
If you have enabled or disabled any of the default plugins for payment providers, your list will look different. 

Every payment provider that you have enabled the plugin for on the "plugins" page appears in this list. 
The list will also always contain the entry for gift cards. 
Gift cards are the only payment method that is not handled by a plugin since gift cards are part of the core functions of pretix. 

![Payment settings page. The "payment providers" tab is open, showing a list with the following entries: bank transfer, gift card, PayPal, SEPA debit and Stripe; gift card is enabled and all other entries are disabled. All entires have 'settings' buttons next to them. ](../../assets/screens/payment-providers/payment-settings.png "Payment settings" )

You can edit and enable payment providers by clicking the :btn-icon:fontawesome-solid-gear:Settings: button next to them. 
Each payment method requires some mandatory information and settings before you can enable it. 
For example, the settings page for bank transfer requires you to enter your bank details and to check a box confirming that you have understood the specific conditions that apply to this payment method. 

You can also apply a wide range of optional settings to each payment provider. 
You can restrict availability of the payment method by date ("Available from" and "Available until"), country ("Restrict to countries") and sales channel ("Restrict to specific sales channels"). 

![Settings page for stripe, showing a large purple button labeled 'Connect with Stripe'](../../assets/screens/payment-providers/payment-external.png "Stripe settings")

If the payment provider is an external service, the settings page only contains a button for connecting with your account on that service. 
Once the connection has been confirmed, the settings page for the payment provider will display the usual settings. 
For detailed information on how to set up and enable specific payment providers, refer to the pages nested below this one: 

 -  [Bank transfer](bank-transfer.md) 
 -  [Stripe](stripe.md) 
 -  [PayPal](paypal.md) 

### Additional fees 

!!! Warning 
    EU Directive 2015/2366 bans surcharging payment fees for most common payment methods within the European Union. 
    Consult a lawyer or refrain from charging payment fees for transactions within the European Union.

Most payment providers charge a fee on every transaction they process. 
If you are planning to pay this fee yourself, you do not need to change any settings. 
If you want to add the fee to your customer's total, consult an expert to make sure that it is legal for you to do so. 

Once you have done that, navigate to :navpath:Your Event → Settings → Payment:, and open the :btn:Advanced: tab. 
In the dropdown menu labeled "Tax rule for payment fees", select the appropriate tax rule. 

If you want to learn more on how to handle taxes in pretix, refer to our guide on [taxes](../taxes.md). 

Then, open the :btn:Payment providers: tab and then open the settings page for the payment provider for which you want to enable additional fees. 

Three elements on this page are relevant for additional fees: two fields labeled "Additional fee" and a checkbox labeled "Calculate the fee from the total value including the fee". 
The first field has the description "Absolute value" and interprets input as currency. 
The second field has the description "Percentage of the order total" and interprets input as a percentage. 
Your choices here depend on your exact use case. 

The next sections explain what to do if you want to pass on a fee to your customers, or if you want to discourage use of a payment provider with an extra fee. 

#### Passing payment provider fees on to your customers 

For illustrative purposes, let us assume that your payment provider is charging you a transaction fee of 2.99% plus a fixed rate of $0.49. 
Enter 0.49 in the "Absolute value" field and 2.99 in the "Percentage of the order total" field. 
Neither input is mandatory. 
You can also add an absolute value only, or a percentage value only. 

Make sure that the "Calculate the fee from the total value including the fee" is checked and click the :btn:Save: button. 
This checkbox determines the way pretix calculates additional fees. 
If the box is checked, pretix will calculate fees in the following way: 

```
((price + fee_abs) * (1 / (1 - fee_percent / 100)) - price)
```

`price` is the net total of the order, `fee_abs` is the fixed portion of the fee, and `fee_percent` is the percentage portion of the fee. 
If the example fees from above are applied to a purchase with a net total of $250, this yields the following calculation: 

```
((250 + 0.49) * (1 / (1 - 2.99 / 100)) - 250) = 8.21049376353 ≈ 8.21
```

The result is the fee that pretix calculates on top of the net total of the order. 
In this example, your customer will have to pay $258.21, the payment provider will subtract $8.21 in transaction fees, and $250 will be added to your balance. 
Depending on the exact calculation and rounding methods used by the payment provider, the final amount that is added to your balance may vary by one cent. 

A payment provider will always use the total amount of a transaction or multiple transactions to calculate their fees. 
The "Calculate the fee from the total value including the fee" method gives you better control over the final amount of money added to your bank account by the payment provider. 
The following table compares the two different calculation methods provided by pretix: 

|                                         | calculation from subtotal without the fee | calculation from total value including the fee |
|-----------------------------------------|-------------------------------------------|------------------------------------------------|
| ticket price                            | $250.00                                   | $250.00                                        |
| fee calculated by pretix                | $7.96                                     | $8.21                                          | 
| total paid by customer                  | $257.96                                   | $258.21                                        |
| fee calculated by payment provider      | $8.20                                     | $8.21                                          |
| final amount added to your bank balance | $249.76                                   | $250.00                                        |

#### Discouraging use of a payment provider with an extra fee 

pretix allows you to use a more straightforward formula for the calculation of that fee. 
This is useful if, for instance, you want to discourage your customers from using a certain payment provider by adding an additional fee. 

For illustrative purposes, we will use a fee of 2.99% plus a fixed rate of $0.49. 
Enter 0.49 in the "Absolute value" field and 2.99 in the "Percentage of the order total" field. 
Neither input is mandatory. 
You can also add an absolute value only, or a percentage value only. 

If you uncheck the box next to "Calculate the fee from the total value including the fee" and click the :btn:Save: button, pretix will use the following formula for the calculation: 

```
price * (fee_percent / 100) + fee_abs
```

If the example fees from above are applied to a purchase with a net total of $100, this yields the following calculation: 

```
250 * (2.99 / 100) + 0.49 = 7.965 ≈ 7.96
```

Your customer will have to pay $257.96. 
Note that this sum is smaller than the one resulting from the formula described above. 
If you use this method for calculating the fee raised by an external payment provider, the amount added to your balance will be 249.756996 ≈ 249.76 and thus slightly smaller than the originally intended net total of $250. 

Use the method described [above](index.md#passing-payment-provider-fees-on-to-your-customers) if you want your users to cover the payment fees charged by the payment provider.

### Deadlines

![Payment settings page. The "deadlines" tab is open, showing various options for settings deadlines.](../../assets/screens/payment-providers/payment-deadlines.png "Payment deadlines settings")

Navigate to :navpath:Your Event → Settings → Payment:. 
The :btn:Deadlines: tab lets you set payment terms measured in either days or minutes. 
By default, the payment term for your customers is set to 14 days. 
This page also lets you make optional adjustments such as a last day of payment, an additional expiration delay beyond the time communicated to your customer, and the option to only end payment terms on weekdays. 

These settings apply on the event level, i.e. equally to all payment providers. 
Keep this in mind if you are using payment methods with long processing times, such as bank transfers. 

pretix does not support setting different deadlines for different payment providers because this could make ordering and paying very confusing and frustrating for your customers. 

Consider, for example, if pretix allowed different deadlines for each payment method. 
A customer first places their order with one payment method, but then switched to a different one with a shorter deadline. 
The customer's order would be rendered invalid and they would have to place a new one for reasons that are not clearly evident to them. 
Placing a new order also means losing the reservation for the items in the shopping cart. 
If a quota has been exhausted in the meantime, then your customer cannot order their preferred product anymore, possibly discouraging them from placing an order at all. 

Alternatively, if each payment method's deadline was added on top of the old one, switching back and forth between payment methods would allow a customer to extend the deadline indefinitely, thus never actually being required to pay you. 
It is for these reasons that pretix only lets you set unified payment deadlines that apply to all payment methods equally. 

## Troubleshooting 

__A payment provider does not show up in :navpath:Your Event → Settings → Payment:__
Navigate to :navpath:Your Event → Settings → Plugins: and open the "payment providers" tab. 
Enable the corresponding plugin. 
Make sure it has the green "✓ Active" tag next to it. 

__A payment provider does not show up in your test shop/Customers cannot select a payment method during their purchase:__ 
Navigate to :navpath:Your Event → Settings → Payment: and open the "payment" tab. 
Click the :btn-icon:fontawesome-solid-gear:Settings: button next to the payment provider that isn't showing up in the shop. Check the "☑ Enable payment method" box. 
Then scroll to the bottom of the page and click :btn:Save:. 

If any mandatory information hasn't been filled out yet, the webpage will notify you. 
Fill out all the mandatory information and click :btn:Save: again. 
The corresponding payment method should now show up in your online shop. 

## Further Information

Here is the full list of articles on setting up and using specific payment providers: 

 -  [Bank transfer](bank-transfer.md) 
 -  [Stripe](stripe.md) 
 -  [PayPal](paypal.md) 