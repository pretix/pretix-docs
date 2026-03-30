## Security of local services

pretix includes features that make HTTP requests to user-specified locations, such as webhooks.
If you have untrusted users with backend access, they could create webhooks that point to private URLs, such as `http://localhost`.
This could create a [Server-side request forgery](https://en.wikipedia.org/wiki/Server-side_request_forgery) attack vector against local network services.

Do not run any HTTP services that are accessible without authentication on the same machine or on the same private network as pretix.
If you cannot ensure this, we recommend using an outgoing HTTP proxy like [smokescreen](https://github.com/stripe/smokescreen) and set the `http_proxy` and `https_proxy` environment variables to point to the proxy.