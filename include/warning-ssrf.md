## Security of local services

pretix includes features that make HTTP requests to user-specified locations, such as webhooks.
If you have untrusted users with backend access, they could create webhooks that point to private URLs, such as `http://localhost`.
This could create a [Server-Side Request Forgery](https://en.wikipedia.org/wiki/Server-side_request_forgery) attack vector against local network services.

Please make sure that you are not running any HTTP services on the same machine or private network as pretix that are accessible without authentication.
If you cannot ensure this, we recommend using an outgoing HTTP proxy like [smokescreen](https://github.com/stripe/smokescreen) and set the `http_proxy` and `https_proxy` environment variables to point to the proxy.