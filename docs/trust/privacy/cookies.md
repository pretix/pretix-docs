# Cookie usage

## Ticket shop

When purchasing a ticket or interacting with the ticket shop in other ways, the following cookies are used in a default configuration of pretix:

<table>
<thead>
<tr>
<th>Name</th>
<th>Content</th>
<th>Lifetime</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>__Host-pretix_csrftoken</code></td>
<td>Random ID</td>
<td>365 days</td>
<td>Security token for form submissions. Provides a security measure against <a href="https://de.wikipedia.org/wiki/Cross-Site-Request-Forgery" target="_blank">CSRF attacks</a>.<br>
We consider the cookie to be technically necessary to provide the desired functionality and therefore not require consent before setting it.
We do not correlate this ID with other data sources and do not use it for tracking.</td>
</tr>
<tr>
<td><code>__Host-pretix_session</code></td>
<td>Language ID</td>
<td>14 days</td>
<td>This cookie is used to recognize the user session across page loads for all features that require this, such as assigning a cart to the user or realizing a login functionality for customer accounts.<br>
The cookie will only be set when the user uses a feature that requires this.<br>
We consider the cookie to be technically necessary to provide the desired functionality and therefore not require consent before setting it.
This cookie is not used for any tracking purposes in the default configuration.</td>
</tr>
<tr>
<td><code>pretix_language</code></td>
<td>Language ID, such as "en" or "de"</td>
<td>10 years</td>
<td>Storage of the user's selected language to display the ticket shop in such that we cna later show the shop in the same preferred language.
Will only be set if the user explicitly sets the language.<br>
We consider the cookie to be technically necessary to provide the desired functionality and therefore not require consent before setting it.
Using this cookie for tracking is practically impossible due to the low information content.</td>
</tr>
<tr>
<td><code>__proxy_session</code></td>
<td>Random ID</td>
<td>7 days</td>
<td>pretix Hosted only: Security token to implement capacity management to keep the ticket shop reliable under high load.<br>
We consider the cookie to be technically necessary to provide the desired functionality and therefore not require consent before setting it.
We do not correlate this ID with other data sources and do not use it for tracking.</td>
</tr>
<tr>
<td><code>cookie-consent-&lt;shop&gt;</code><br><small>(Local storage)</small></td>
<td>Consent settings</td>
<td>permanently</td>
<td>If our cookie consent module is used for third-party cookies (e.g. tracking providers), we store what cookies the user did or did not consent to.
This is required to later enforce the consent by loading only appropriate tracking features.
Since this information is stored in local storage and not in a cookie, it is never transmitted to our sever and only managed within the browser.</td>
</tr>
</tbody>
</table>

Additional cookies may occur due to the usage of plugins, e.g. by embedding payment providers or tracking scripts.
pretix includes native functionality to provide a unified cookie consent management to plugins, see also our [developer documentation](https://docs.pretix.eu/dev/development/api/cookieconsent.html).

## pretix Widget

When **loading** the widget on a page, pretix **does not** set any cookies in the user's browser.
Only after the user interacts with the widget (i.e. selects a product and starts the purchase process), a cookie will be set.
In the context of the embedding website, the following cookie will be set:

<table>
<thead>
<tr>
<th>Name</th>
<th>Content</th>
<th>Lifetime</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pretix_widget_&lt;ticketshop_url&gt;</code></td>
<td>Cart ID</td>
<td>30 days</td>
<td>The cookie is used such that the user can resume the purchase after the process was interrupted (e.g. by a browser crash) and does not lose the reserved tickets.<br>
We consider the cookie to be technically necessary to provide the desired functionality and therefore not require consent before setting it.</td>
</tr>
</tbody>
</table>

Additionally, all the cookies mentioned in the "ticket shop" section will be set when using the widget as well.