# United States

{% include "warning-tax-law.md" %}

## Sales Tax

In the US, sales tax regulation differs by state.
You can configure pretix to charge different sales tax rates depending for every event (depending on the state the event is in).
You can also use the advanced options of [tax rules](../../guides/taxes.md) to charge different sales tax rates depending on the state the buyer reports to be in.

pretix currently only supports tax rates with at most two decimal places (e.g. 6.25%, but not 4.712%).
At the time of writing 8 states have tax rates with three decimal places (Arizona, Arkansas, Hawaii, Minnesota, Nevada, New Jersey, New Mexico, New York).
We are working on allowing precise calculation of these tax rates in the future.

## Invoicing

### E-invoicing

The US currently do not require sending electronic invoices in a structured format.

## pretixPOS

We are not aware of specific requirements on cash registers in the US.
Therefore, we believe pretixPOS can generally be used in the US.

## Transparency on fees

The Federal Trade Commission (FTC) has ruled that ticket sellers must not make use of [unfair or deceptive fees](https://www.ftc.gov/legal-library/browse/rules/rulemaking-unfair-or-deceptive-fees).
We therefore recommend to include as many costs as possible in the ticket price and only use pretix to charge additional fees during checkout if there is no other option.