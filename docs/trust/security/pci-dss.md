# PCI DSS

The **Payment Card Industry Data Security Standard** (PCI DSS) mandates security requirements that every party involved with accepting credit cards needs to follow.
Following PCI DSS standards is not required by law, but your payment service provider might require you to send them documentation that you do so.
Depending on what role you play in the credit card acceptance process, you may only need to follow a subset of the requirements.
If in doubt, ask your payment service provider what exactly you need to do.

pretix never handles credit card account data directly.
All of our official integrations with payment providers are built in a way that embeds the credit card form from the payment provider either through a redirect or iframe.
Therefore, you usually need to fill out the [Self-Assessment Questionnaire (SAQ) A](https://docs-prv.pcisecuritystandards.org/SAQ%20(Assessment)/SAQ/PCI-DSS-v4_0_1-SAQ-A-r1.pdf) and comply with the requirements listed there.
Whether this questionnaire and the requirements apply to you depend on how your payment provider categorizes your business.

## pretix Hosted

<!-- md:hosted -->

If you use our SaaS offer, pretix Hosted, then the responsibility to comply with many of the requirements lies with us.
Specifically, we ensure that the technical configuration of our systems is in line with all technical requirements listed in SAQ A.

Some other requirements need to be handled by you.
For example, requirements 12.8.1–12.8.5 require you to keep a list of all service providers (such as us and your payment service provider) and regularly check that we are still PCI DSS compliant.
Our **Responsibility Matrix** indicates exactly which parts of the SAQ A requirements are handled by us and which are to be done by you.

We undergo a yearly **external certification** to ensure we are meeting all relevant requirements.
You can access our current certificate through the [security page](https://pretix.eu/about/en/security) on our website.

Your payment service provider might request you to submit **vulnerability scans** of your shop.
We have a contract with a PCI-Approved Scanning Vendor (ASV) to perform quarterly scans of our systems using sample ticket shops that are representative of our system environment for all shops.
If you send your customers to the ticket shop hosted with us using a link, submitting these scan results to your payment service provider is sufficient to achieve compliance.

If you embed our [Widget](../../guides/widget.md) into your website, your payment service provider may require you to perform scans of your website as well.
This does not apply if your payment provider's credit card form always opens in a new tab.
You can also avoid this requirement by configuring the widget to [always open in a new tab](../../guides/widget.md#always-open-a-new-tab).
Should you do require a scan, there is a list of [Approved Scanning Vendors](https://www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors/) on the PCI website, such as [usd AG](https://www.usd.de/en/pci-payment-security/pci-security-scans/) which is performing our scans.

You can find the latest version of all relevant documents, such as our **Attestation of Scan Compliance**, our **Attestation of Compliance** and the **Responsibility Matrix** for our relationship with you in your pretix account at :navpath:Your organizer → :fa3-wrench: Settings → PCI DSS compliance:.

Should you require any additional documentation or have any further questions on the topic, please reach out to us at [pci@pretix.eu](mailto:pci@pretix.eu).

## Self-hosted versions of pretix

<!-- md:community -->
<!-- md:enterprise -->

If you host pretix on your own servers, you need to ensure compliance with **all requirements** listed in the SAQ A questionnaire.
This includes technical requirements such as using strong authentication methods, process requirements such as ensuring you always apply security updates quickly and having an incident response plan, as well as the requirement to perform **quarterly vulnerability scans** on your server through a PCI Approved Scanning Vendor (ASV).

The scan should include all servers used to run pretix and, if applicable, your website embedding our [Widget](../../guides/widget.md).
This does not apply if your payment provider's credit card form always opens in a new tab.
You can also avoid this requirement by configuring the widget to [always open in a new tab](../../guides/widget.md#always-open-a-new-tab).
There is a list of [Approved Scanning Vendors](https://www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors/) on the PCI website, such as [usd AG](https://www.usd.de/en/pci-payment-security/pci-security-scans/) which is performing our scans.

### SAQ A eligibility criteria and custom plugins

The PCI questionnaires of every level include a number of eligibility criteria.
SAQ A is the simplest level and should be sufficient if you use pretix in a default configuration and your company does not process credit cards in other ways.

pretix and official pretix plugins never store any credit card numbers directly, as required by SAQ A eligibility criteria.
If you create a custom payment plugin, make it so that it also fulfills this requirement.
All credit card inputs must be served directly by a PCI-certified payment provider through an iframe or redirect.
If you want to implement a payment provider plugin with an HTML form within pretix collecting credit card information, then you need to comply with the requirements of the SAQ A-EP questionnaire.

In particular, we want to point out that version 4.0.1 of the SAQ A also includes the following requirement:

> The merchant has confirmed that their site is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s).

We believe pretix is providing a good foundation for this requirement by using a strict [Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) and not allowing further scripts to be added without a software modification.
However, it probably also means that you have to implement security measures that ensure that no unauthorized users are able to modify your pretix installation.

If you create custom plugins that inject additional JavaScript scripts, such as external components or tracking snippets, we recommend that you exclude payment pages from this injection.
You can do so by checking for the ``pci_dss_payment_page`` attribute on the request object:

```python
@receiver(html_head)
def html_head_receiver(request=None, **kwargs):
    if getattr(request, "pci_dss_payment_page", False):
        # No tracking scripts on PCI DSS relevant payment pages
        return ""
```