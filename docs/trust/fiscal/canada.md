# Canada

{% include "warning-tax-law.md" %}

## Sales Tax

In Canada, there are two types of sales taxes:
Provincial sales taxes (PST) charged by the province and the federal Goods and services tax (GST).
In Ontario, New Brunswick, Newfoundland and Labrador, Nova Scotia and Prince Edward Island, the two taxes are combined into the Harmonized Sales Tax (HST).

pretix can only calculate one tax rate per product and can only show one tax per product in the invoice.
Some provinces (see e.g. [official guidance for Quebec](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/collecting-gst-and-qst/calculating-the-taxes/)) do specifically allow calculating the tax using the combination of GST + PST.
However, pretix is not able to show them individually on the invoice.

pretix currently only supports tax rates with at most two decimal places.
Quebec charges a PST of 9.975 % (or 14.975 combined with GST) which cannot be calculated in pretix.
We are working on allowing precise calculation of this tax rate in the future.
Some provinces (see e.g. [official guidance for Quebec](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/collecting-gst-and-qst/calculating-the-taxes/)) to specifically allow rounding off the tax rate if the system in use does not support a three-decimal tax rate.

## pretixPOS

Restaurant establishments in the province of Québec are required to use a Sales Recording Module (SRM), either physical or WEB-SRM. 
pretixPOS does not support these technologies. 
If you operate a restaurant establishment in Québec, then you should **not** use pretixPOS. 

We are not aware of any other specific requirements on cash registers in Canada.
Therefore, we believe pretixPOS can generally be used in Canada, except in the situation described above.
