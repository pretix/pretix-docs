# Restricted audience 

Not all events are for everyone. 
Sometimes, there is a good reason to restrict access to your event or parts of your event only to a specific, invited group. 
There are several ways to implement this with pretix. 
This article will guide you through all of them. 

## Prerequisites 

## How To 

### Option A: Required voucher codes

You can use vouchers to make a product (or multiple products) only available to a select group of invited guests. 
Refer to [Vouchers: Exclusive product availability](vouchers.md#exclusive-product-availability) for detailed instructions. 

### Option B: Order approvals

If you do not know individual members of your audience already, but still want to restrict it to a certain group, e.g. people with a given profession, you can check the "Buying this product requires approval" in the settings of your product. 
If a customer tries to buy such a product, they will be able to place their order but cannot proceed to payment. 
Instead, you will be asked to approve or deny the order and only if you approve it, we will send a payment link to the customer.

This requires the customer to interact with the ticket shop twice (once for the order, once for the payment) which adds a little more friction, but gives you full control over who attends the event.

### Option C: Registered customers & memberships

You can also do this by requiring that customers have a [customer account](customer-accounts.md) and an active membership. 
You can find more information on this mechanism under [season tickets](products.md#season-tickets).
