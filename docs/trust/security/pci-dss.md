# PCI DSS

The **Payment Card Industry Data Security Standard** (PCI DSS) mandates security requirements that every party involved with accepting credit cards needs to follow.
Depending on what role you play in the credit card acceptance process, only a subset of the requirements need to be followed.
If in doubt, you should ask your payment service provider on what exactly you need to do.

pretix never handles credit card direction directly.
All of our official integrations with payment providers are built in a way that embeds the credit card form from the payment provider either through a redirect or iframe.
Therefore, you usually need to fill out the questionnaire [SAQ A](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4_0_1-SAQ-A-r1.pdf) and comply with the requirements listed there.

## pretix Hosted

If you use our Software-as-a-Service offering, pretix Hosted, we are responsible for complying with many of the requirements.

Specifically, we ensure that the technical configuration of our systems is in line with all technical requirements listed in SAQ A.
We ensure all required processes for security policies, risk management, employee training, and incident response are in place on our end.
We undergo a yearly **external certification** to ensure we are meeting all requirements.

Your payment service provider might request you to do **vulnerability scans** of your shop.
We contract with a PCI DSS Approved Scanning Vendor (ASV) to perform quarterly scans of our systems using sample ticket shops that are representative of our system environment for all shops.
In most cases, submitting these scan results to your payment service provider is sufficient to achieve compliance.
In some cases, when using the pretix widget, it might be required for you to perform scans of the website embedding the widget as well.

To be fully compliant with PCI DSS, you still need to set up some internal processes and documentation to manage the relationship with us.

You can find the latest version of all relevant documents, such as our **Attestation of Scan Compliance**, our **Attestation of Compliance** and the **Responsibility Matrix** for our relationship with you in your pretix account at :navpath:Your organizer → :fa3-wrench: Settings → PCI DSS compliance:.

## pretix Community or Enterprise

TBD after clarification abour SAQ A 4.0.1 rev1


Should you require any additional documentation or have any further questions on the topic, please reach out to us at [pci@pretix.eu](mailto:support@pretix.eu).