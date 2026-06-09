# Responsible disclosure policy

!!! Warning

    If you discover a vulnerability with our software or server systems, please report it to us in private.
    Do not to attempt to harm our users, customer's data or our system's availability when looking for vulnerabilities.

    Please contact us at [security@pretix.eu](mailto:security@pretix.eu) with full details and steps to reproduce and allow reasonable time for us to resolve the issue before publishing your findings.
    If you wish to encrypt your email, you can use our [GPG key](https://pretix.eu/.well-known/security@pretix.eu.asc).

## Scope

The following products and services are within the scope for our disclosure process:

*   All open source projects in the GitHub organizations [pretix](https://github.com/pretix), [pretix-unofficial](https://github.com/pretix-unofficial), and [venueless](https://github.com/venueless) (excluding forked or archived repositories)
*   The open source projects [python-fints](https://github.com/raphaelm/python-fints), [python-sepaxml](https://github.com/raphaelm/python-sepaxml), [django-scopes](https://github.com/raphaelm/django-scopes), [django-i18nfield](https://github.com/raphaelm/django-i18nfield), and [django-hierarkey](https://github.com/raphaelm/django-hierarkey).
*   Proprietary pretix plugins sold as part of our pretix Enterprise offering
*   The following websites and services:
    *   https://pretix.eu
    *   https://marketplace.pretix.eu
    *   https://pretixstatus.com
    *   https://cdn.pretix.space
    *   https://\*.venueless.events
    *   https://vnls.io
*   The Android and iOS apps pretixSCAN, pretixPRINT, pretixPOS, pretixLEAD, and pretix Marketplace Client.
*   The Desktop and Server applications pretixSCAN, pretixSCAN Proxy, pretixKIOSK, pretixTURNSTILE.

We are also happy to receive reports for all other security issues regarding our infrastructure.
However, if they affect software not created by us, we will pass the reports on to the respective software vendor.
We will only issue [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) numbers or bug bounties for products and services listed above.

## CVE Numbering Authority

pretix GmbH (previously rami.io GmbH) has been authorized by the CVE Program as a CVE Numbering Authority (CNA) for any vulnerabilities in our own products.
CNAs are organizations responsible for the regular assignment of CVE IDs to vulnerabilities, and for creating and publishing information about the vulnerability in the associated CVE Record.
Our CNA assigns CVE numbers only for the products and services listed above.

A CVE ID will be issued by us only if all of the following conditions are met:

*   The issue can be reproduced by us and is confirmed to have a security impact.
*   Remediation of the issue might require action by users of the software, such as installing a patch.
*   The affected software version is not end of life.

## Disclosure

Security incidents concerning products under the pretix brand are announced on the pretix [security page](https://pretix.eu/about/en/security) and in the pretix [newsletter](https://pretix.eu/about/en/blog/).

## Bug Bounties

**We do not run a formal bug bounty program and do not regularly pay monetary bounties.**

If you find a critical vulnerability in our service, we will try to find a way to show our gratitude.
We only consider paying a monetary bounty for vulnerabilities of critical severity.
We consider an issue to have critical severity only if it allows the extraction, modification or destruction of non-trivial confidential data through privilege escalation (excluding within the same organizer account), authentication bypass, or account takeover.

We **never** pay bounties for the following types of reports:

- Denial of service or brute force attack vectors / rate-limiting issues
- Issues that can only be exploited in combination with significant other security flaws that have not been found (e.g. [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) without [CSP](https://en.wikipedia.org/wiki/Content_Security_Policy) bypass)
- Logic bugs in our business logic
- [HTTP](https://en.wikipedia.org/wiki/HTTP) or email header best practices
- [SPF/DKIM/DMARC](https://en.wikipedia.org/wiki/Email_authentication) best practices
- [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) cipher best practices
- **Any reports generated primarily by AI**

## Rules

Report a security issue in our services to us in private using the contact information at the start of this page.
All reports will be considered for appropriate action.
If you follow the rules below, we will not be threatening you with legal action.

* **Only** access the data necessary to demonstrate that the vulnerability exists.
* **Do not** take any actions that attempt to harm our users, confidentiality of our customer's data or availability of our systems.
* **Do not** modify or delete any data not owned by you.
* **Do not** impact the availability of any of our internal or external services (e.g. through DDoS or similar attacks).
* **Do not** implement backdoors or use similar methods to obtain persistent access.
* **Do not** send phishing emails or use any other social engineering techniques. 
