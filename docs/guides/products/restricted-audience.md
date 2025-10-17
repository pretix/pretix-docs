# Restricted audience 

Not all events are for everyone. 
Sometimes, there is a good reason to restrict access to your event or [parts of your event](sessions.md) only to a specific group of people. 
There are several ways to implement this with pretix. 
This article will guide you through all of them. 

## Option A: Required voucher codes

You can use vouchers to make a product (or multiple products) only available to a select group of invited guests. 
Refer to [Vouchers: Exclusive product availability](../vouchers.md#exclusive-product-availability) for detailed instructions. 

## Option B: Order approvals

If you do not know individual members of your audience already, but still want to restrict it to a certain group, you can require approval for orders. 
This is useful if you are offering discounts or free products for certain groups such as press or students. 
Requiring approval allows you to check your customers' status as members of that group before confirming the order. 

In order to require approval for a product, edit your admission products.
On the :btn:General: tab, scroll to the bottom of the page and check the box next to "Buying this product requires approval". 
Customers will be able to place an order for such a product, but cannot proceed to payment without you having approved the order. 

Orders waiting for approval behave like orders waiting for payment. 
Once a customer orders them, they are reserved in the quota and, if a seating plan exists, in the seating plan. 

!!! Note 
    The setting "Buying this product requires approval" affects the whole order. 
    If a customer orders several products and one or more of them require approval, then the whole order will require approval. 
    If you have to deny approval, then you may also have to split the order. 

In order to review incoming orders, navigate to :navpath:Your event → :fa3-shopping-cart: Orders → All orders:. 
Manually approve or decline each order that contains a product that requires approval. 
Once you have done that, the customer will receive an email notifying them that their order has been approved and they can proceed to payment. 

The main downside of this approach is that your customers will have to interact with the ticket shop twice: once for placing the order, and once for paying. 
This downside does not affect entirely free orders because the payment step is not necessary for those. 
The main advantage of this method is that it gives you control over who attends the event for each individual order. 

## Option C: Registered customers & memberships

You can restrict your event to a certain group by requiring a membership for purchasing a ticket.
Refer to the article on [customer accounts](../customer-accounts.md) for instructions on how to set this up. 
You can find more information on granting and requiring memberships under [season tickets](index.md#option-a-memberships-and-multiple-tickets). 
