# Responsible disclosure policy

!!! Warning

    If you discover a vulnerability with our software or server systems, please report it to us in private.
    Do not to attempt to harm our users, customer's data or our system's availability when looking for vulneratbilities.

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
However, if they affect software not created by us, we will pass the reports on to the respective software vendor and will not be able to issue bug bounties or CVE numbers.

## CVE Numbering Authority

rami.io GmbH has been authorized by the CVE Program as a CVE Numbering Authority (CNA) for any vulnerabilities in our own products.
CNAs are organizations responsible for the regular assignment of CVE IDs to vulnerabilities, and for creating and publishing information about the vulnerability in the associated CVE Record.
Our CNA assigns CVE numbers only for the products and services listed above.

A CVE ID will be issued by us only if all of the following conditions are met:

*   The issue can be reproduced by us and is confirmed to have a security impact.
*   Remediation of the issue might require action by users of the software, such as installing a patch.
*   The affected software version is not end of life.

## Disclosure

Security incidents concerning products under the pretix brand are announced on the pretix [security page](https://pretix.eu/about/en/security) and in the pretix [newsletter](https://pretix.eu/about/en/blog/).

## Bug Bounties

We're not large enough to run a formal bug bounty program. If you find a serious vulnerability in our service, we will find a way to show our gratitude.
We have, on occasion, issued monetary bug bounties for issues of high severity in our core services.

We consider an issue to have a high or critical severity if it allows the extraction of non-trivial confidential data, privilege escalation, authentication bypass, account takeover, or XSS in combination with a CSP bypass possibility.

We do not consider issues to have a high or critical severity that provide DoS or brute force attack vectors, can only be exploited in combination with significant other security flaws that have not been found, logic bugs.

We do not issue bounties for any reports referring to best practices around HTTP headers, email headers, SPF/DKIM/DMARC records, TLS ciphers, etc.

## Rules

If you report a security issue in our services to us in private without taking actions that attempt to harm our users, confidentiality of our customer's data or availability of our systems, we will treat your report properly and will not be threatening you with legal action.

Specifically, access only the data necessary to show that the vulnerability exists. Do not modify or delete any data not owned by you. Do not impact the availability of any of our internal or external services (e.g. through DDoS or similar attacks). Do not implement backdoors or use similar methods to obtain persistent access.
Do not send phishing e-mails or use any other social engineering techniques.