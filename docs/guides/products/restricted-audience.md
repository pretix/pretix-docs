# Restricted audience 

Not all events are for everyone. 
Sometimes, there is a good reason to restrict access to your event or [parts of your event](sessions.md) only to a specific group of people. 
There are several ways to implement this with pretix. 
This article will guide you through all of them. 

## Option A: Required voucher codes

You can use vouchers to make a product (or multiple products) only available to a select group of invited guests. 
Refer to [Vouchers: Exclusive product availability](../vouchers.md#exclusive-product-availability) for detailed instructions. 

## Option B: Order approvals

If you do not know individual members of your audience already, but still want to restrict it to a certain group, edit your admission products and check the box next to "Buying this product requires approval". 
Customers will be able to place an order for such a product, but cannot proceed to payment without you having approved the order. 
This can be useful if, for instance, you are offering special tickets for journalists. 

In order to review incoming orders, navigate to :navpath:Your event → :fa3-shopping-cart: Orders → All orders:. 
Manually approve or decline each order that contains a product that requires approval. 
Once you have done that, the customer will receive an email notifying them that their order has been approved and they can proceed to payment. 

The main downside of this approach is that your customers will have to interact with the ticket shop twice: once for placing the order, and once for paying. 
On the other hand, it gives you control over who attends the event for each individual order. 

## Option C: Registered customers & memberships

You can restrict your event to a certain group by requiring a membership for purchasing a ticket.
Refer to the article on [customer accounts](../customer-accounts.md) for instructions on how to set this up. 
You can find more information on granting and requiring memberships under [season tickets](index.md#option-a-memberships-and-multiple-tickets). 
