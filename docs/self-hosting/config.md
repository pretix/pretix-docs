# Configuration file

Pretix reads its configuration from a configuration file. It tries to find this file at the following locations. It will try to read the file from the specified paths in the following order. The file that is found *last* will override the settings from the files found before.

1.  `PRETIX_CONFIG_FILE` environment variable
2.  `/etc/pretix/pretix.cfg`
3.  `~/.pretix.cfg`
4.  `pretix.cfg` in the current working directory

The file is expected to be in the INI format as specified in the [Python documentation](https://docs.python.org/3/library/configparser.html?highlight=configparser#supported-ini-file-structure).

The config file may contain the following sections (all settings are optional and have default values). We suggest that you start from the examples given in one of the installation tutorials.

!!! Note

    The configuration file is the recommended way to configure pretix. However, you can also set them through environment variables. In this case, the syntax is `PRETIX_SECTION_CONFIG`. For example, to configure the setting `password_reset` from the `[pretix]` section, set `PRETIX_PRETIX_PASSWORD_RESET=off` in your environment.

## pretix settings

Example:

``` ini
[pretix]
instance_name=pretix.de
url=http://localhost
currency=EUR
datadir=/data
plugins_default=pretix.plugins.sendmail,pretix.plugins.statistics,pretix.plugins.checkinlists
```

`instance_name`

:   The name of this installation. Default: `pretix.de`

`url`

:   The installation's full URL, without a trailing slash.

`currency`

:   The default currency as a three-letter code. Defaults to `EUR`.

`cachedir`

:   The local path to a directory where temporary files will be stored. Defaults to the `cache` directory below the `datadir`.

`datadir`

:   The local path to a data directory that will be used for storing user uploads and similar data. Defaults to the value of the environment variable `DATA_DIR` or `data`.

`logdir`

:   The local path to a directory where log files will be stored. Defaults to the `logs` directory below the `datadir`.

`plugins_default`

:   A comma-separated list of plugins that are enabled by default for all new events. Defaults to `pretix.plugins.sendmail,pretix.plugins.statistics,pretix.plugins.checkinlists`.

`plugins_exclude`

:   A comma-separated list of plugins that are not available even though they are installed. Defaults to an empty string.

`plugins_show_meta`

:   Whether to show authors and versions of plugins, defaults to `on`.

`auth_backends`

:   A comma-separated list of available auth backends. Defaults to `pretix.base.auth.NativeAuthBackend`.

`registration`

:   Enables or disables the registration of new admin users. Defaults to `off`.

`password_reset`

:   Enables or disables password reset. Defaults to `on`.

`long_sessions`

:   Enables or disables the "keep me logged in" button. Defaults to `on`.

`ecb_rates`

:   By default, pretix periodically downloads currency rates from the European Central Bank as well as other authorities that are used to print tax amounts in the customer currency on invoices for some currencies. Set to `off` to disable this feature. Defaults to `on`.

`audit_comments`

:   Enables or disables nagging staff users for leaving comments on their sessions for auditability. Defaults to `off`.

`obligatory_2fa`

:   Enables or disables obligatory usage of two-factor authentication for users of the pretix backend. Can be `True` to make two-factor authentication obligatory for all users or `staff` to make it only obligatory to users with admin permissions. Defaults to `False`.

`trust_x_forwarded_for`

:   Specifies whether the `X-Forwarded-For` header can be trusted. Only set to `on` if you have a reverse proxy that actively removes and re-adds the header to make sure the correct client IP is the first value. Defaults to `off`.

`trust_x_forwarded_proto`

:   Specifies whether the `X-Forwarded-Proto` header can be trusted. Only set to `on` if you have a reverse proxy that actively removes and re-adds the header to make sure the correct value is set. Defaults to `off`.

`trust_x_forwarded_host`

:   Specifies whether the `X-Forwarded-Host` header can be trusted. Only set to `on` if you have a reverse proxy that actively removes and re-adds the header to make sure the correct value is set. Defaults to `off`.

`csp_log`

:   Log violations of the Content Security Policy (CSP). Defaults to `on`.

`csp_additional_header`

:   Specifies a CSP header that will be **merged** with pretix's default header. For example, if you set this to `script-src https://mycdn.com`, pretix will add `https://mycdn.com` as an **additional** allowed source to all CSP headers. Empty by default.

`loglevel`

:   Set console and file log level (`DEBUG`, `INFO`, `WARNING`, `ERROR` or `CRITICAL`). Defaults to `INFO`.

`request_id_header`

:   Specifies the name of a header that should be used for logging request IDs. Off by default.

## Locale settings

Example:

``` ini
[locale]
default=de
timezone=Europe/Berlin
```

`default`

:   The system's default locale. Default: `en`

`timezone`

:   The system's default timezone as a `pytz` name. Default: `UTC`

## Database settings

Example:

``` ini
[database]
backend=postgresql
name=pretix
user=pretix
password=abcd
host=localhost
port=3306
advisory_lock_index=1
disable_server_side_cursors=0
sslmode=require
sslrootcert=/etc/pretix/postgresql-ca.crt
sslcert=/etc/pretix/postgresql-client-crt.crt
sslkey=/etc/pretix/postgresql-client-key.key
```

`backend`

:   One of `sqlite3` and `postgresql`. Default: `sqlite3`.

`name`

:   The database's name. Default: `db.sqlite3`.

`user`, `password`, `host`, `port`

:   Connection details for the database connection. Empty by default.

`advisory_lock_index`

:   On PostgreSQL, pretix uses the "advisory lock" feature. However, advisory locks use a server-wide name space and and are not scoped to a specific database. If you run multiple pretix applications with the same PostgreSQL server, you should set separate values for this setting (integers up to 256).

`disable_server_side_cursors`

:   On PostgreSQL pretix might use server side cursors for certain operations. This is generally fine but will break in specific circumstances, for example when connecting to PostgreSQL through a PGBouncer configured with a transaction pool mode. Off by default (i.e. by default server side cursors will be used).

`sslmode`, `sslrootcert`

:   Connection TLS details for the PostgreSQL database connection. Possible values of `sslmode` are `disable`, `allow`, `prefer`, `require`, `verify-ca`, and `verify-full`. `sslrootcert` should be the accessible path of the ca certificate. Both values are empty by default.

`sslcert`, `sslkey`

:   Connection mTLS details for the PostgreSQL database connection. It's also necessary to specify `sslmode` and `sslrootcert` parameters, please check the correct values from the TLS part. `sslcert` should be the accessible path of the client certificate. `sslkey` should be the accessible path of the client key. All values are empty by default.

## Database replica settings

If you use a replicated database setup, pretix expects that the default database connection always points to the primary database node. Routing read queries to a replica on database layer is **strongly** discouraged since this can lead to inaccurate such as more tickets being sold than are actually available.

However, pretix can still make use of a database replica to keep some expensive queries with that can tolerate some latency from your primary database, such as backend search queries. The `replica` configuration section can have the same settings as the `database` section (except for the `backend` setting) and will default back to the `database` settings for all values that are not given. This way, you just need to specify the settings that are different for the replica.

Example:

``` ini
[replica]
host=192.168.0.2
```

## URLs

Example:

``` ini
[urls]
media=/media/
static=/static/
```

`media`

:   The URL to be used to serve user-uploaded content. You should not need to modify this. Default: `/media/`

`static`

:   The URL to be used to serve static files. You should not need to modify this. Default: `/static/`

## Email

Example:

``` ini
[mail]
from=hello@localhost
host=127.0.0.71
user=pretix
password=foobar
port=1025
tls=on
ssl=off
```

`host`, `port`

:   The SMTP Host to connect to. Defaults to `localhost` and `25`.

`user`, `password`

:   The SMTP user data to use for the connection. Empty by default.

`tls`, `ssl`

:   Use STARTTLS or SSL for the SMTP connection. Off by default.

`from`

:   The email address to set as `From` header in outgoing emails by the system. Default: `pretix@localhost`

`from_notifications`

:   The email address to set as `From` header in admin notification emails by the system. Defaults to the value of `from`.

`from_organizers`

:   The email address to set as `From` header in outgoing emails by the system sent on behalf of organizers. Defaults to the value of `from`.

`custom_sender_verification_required`

:   If this is on (the default), organizers need to verify email addresses they want to use as senders in their event.

`custom_sender_spf_string`

:   If this is set to a valid SPF string, pretix will show a warning if organizers use a sender address from a domain that does not include this value.

`custom_smtp_allow_private_networks`

:   If this is off (the default), custom SMTP servers cannot be private network addresses.

`admins`

:   Comma-separated list of email addresses that should receive a report about every error code 500 thrown by pretix.

## Django settings

Example:

``` ini
[django]
secret=j1kjps5a5&4ilpn912s7a1!e2h!duz^i3&idu@_907s$wrz@x-
debug=off
passwords_argon2=on
```

`secret`

:   The secret to be used by Django for signing and verification purposes. If this setting is not provided, pretix will generate a random secret on the first start and will store it in the filesystem for later usage.

`secret_fallback0` ... `secret_fallback9`

:   Prior versions of the secret to be used by Django for signing and verification purposes that will still be accepted but no longer be used for new signing.

`debug`

:   Whether or not to run in debug mode. Default is `False`.

    !!! Warning

        Never set this to `True` in production!

`passwords_argon`

:   Use the `argon2` algorithm for password hashing. Disable on systems with a small number of CPU cores (currently less than 8).

`profile`

:   Enable code profiling for a random subset of requests. Disabled by default, see [Performance Monitoring](./maintenance.md#performance-monitoring) for details.

## Metrics

If you want to fetch internally collected prometheus-style metrics you need to configure the credentials for the metrics endpoint and enable it:

``` ini
[metrics]
enabled=true
user=your_user
passphrase=mysupersecretpassphrase
```

Currently, metrics-collection requires a redis server to be available.

## Memcached

You can use an existing memcached server as pretix's caching backend:

``` ini
[memcached]
location=127.0.0.1:11211
```

`location`

:   The location of memcached, either a host:port combination or a socket file.

If no memcached is configured, pretix will use redis for caching. If neither is configured, pretix will not use any caching.

!!! Note

    If you use memcached and you deploy pretix across multiple servers, you should use *one* shared memcached instance, not multiple ones, because cache invalidations would not be propagated otherwise.

## Redis

If a redis server is configured, pretix can use it for locking, caching and session storage to speed up various operations:

``` ini
[redis]
location=redis://127.0.0.1:6379/1
sessions=false
sentinels=[
        ["sentinel_host_1", 26379],
        ["sentinel_host_2", 26379],
        ["sentinel_host_3", 26379]
    ]
password=password
ssl_cert_reqs=required
ssl_ca_certs=/etc/pretix/redis-ca.pem
ssl_keyfile=/etc/pretix/redis-client-crt.pem
ssl_certfile=/etc/pretix/redis-client-key.key
```

`location`

:   The location of redis, as a URL of the form `redis://[:password]@localhost:6379/0` or `unix://[:password]@/path/to/socket.sock?db=0`

`sessions`

:   When this is set to `True`, redis will be used as the session storage.

`sentinels`

:   Configures redis sentinels to use. If you don't want to use redis sentinels, you should omit this option. If this is set, redis via sentinels will be used instead of plain redis. In this case the location should be of the form `redis://my_master/0`. The `sentinels` variable should be a json serialized list of sentinels, each being a list with the two elements hostname and port. You cannot provide a password within the location when using sentinels. Note that the configuration format requires you to either place the entire value on one line or make sure all values are indented by at least one space.

`password`

:   If your redis setup doesn't require a password or you already specified it in the location you can omit this option. If this is set it will be passed to redis as the connection option PASSWORD.

`ssl_cert_reqs`

:   If this is set it will be passed to redis as the connection option `SSL_CERT_REQS`. Possible values are `none`, `optional`, and `required`.

`ssl_ca_certs`

:   If your redis setup doesn't require TLS you can omit this option. If this is set it will be passed to redis as the connection option `SSL_CA_CERTS`. Possible value is the ca path.

`ssl_keyfile`

:   If your redis setup doesn't require mTLS you can omit this option. If this is set it will be passed to redis as the connection option `SSL_KEYFILE`. Possible value is the keyfile path.

`ssl_certfile`

:   If your redis setup doesn't require mTLS you can omit this option. If this is set it will be passed to redis as the connection option `SSL_CERTFILE`. Possible value is the certfile path.

If redis is not configured, pretix will store sessions and locks in the database. If memcached is configured, memcached will be used for caching instead of redis.

## Translations

pretix comes with a number of translations. All languages are enabled by default. If you want to limit the languages available in your installation, you can enable a set of languages like this:

``` ini
[languages]
enabled=en,de
```

Some of the languages them are marked as "incubating", which means they can usually only be selected in development mode. If you want to use them nevertheless, you can activate them like this:

``` ini
[languages]
allow_incubating=pt-br,da
```

You can also tell pretix about additional paths where it will search for translations:

``` ini
[languages]
path=/path/to/my/translations
```

For a given language (e.g. `pt-br`), pretix will then look in the specific sub-folder, e.g. `/path/to/my/translations/pt_BR/LC_MESSAGES/django.po`.

## Celery task queue

For processing long-running tasks asynchronously, pretix requires the celery task queue. For communication between the web server and the task workers in both direction, a messaging queue and a result backend is needed. You can use a redis database for both directions, or an AMQP server (e.g. RabbitMQ) as a broker and redis or your database as a result backend:

``` ini
[celery]
broker=amqp://guest:guest@localhost:5672//
backend=redis://localhost/0
broker_transport_options="{}"
backend_transport_options="{}"
```

RabbitMQ might be the better choice if you have a complex, multi-server, high-performance setup, but as you already should have a redis instance ready for session and lock storage, we recommend redis for convenience. See the [Celery documentation](http://docs.celeryproject.org/en/latest/userguide/configuration.html) for more details.

The two `transport_options` entries can be omitted in most cases. If they are present they need to be a valid JSON dictionary. For possible entries in that dictionary see the [Celery documentation](http://docs.celeryproject.org/en/latest/userguide/configuration.html).

It is possible the use Redis with TLS/mTLS for the broker or the backend. To do so, it is necessary to specify the TLS identifier `rediss`, the ssl mode `ssl_cert_reqs` and optionally specify the CA (TLS) `ssl_ca_certs`, cert `ssl_certfile` and key `ssl_keyfile` (mTLS) path as encoded string. the following uri describes the format and possible parameters:

    rediss://0.0.0.0:6379/1?ssl_cert_reqs=required&ssl_ca_certs=%2Fetc%2Fpretix%2Fredis-ca.pem&ssl_certfile=%2Fetc%2Fpretix%2Fredis-client-crt.pem&ssl_keyfile=%2Fetc%2Fpretix%2Fredis-client-key.key

To use redis with sentinels set the broker or backend to `sentinel://sentinel_host_1:26379;sentinel_host_2:26379/0` and the respective transport_options to `{"master_name":"mymaster"}`. If your redis instances behind the sentinel have a password use `sentinel://:my_password@sentinel_host_1:26379;sentinel_host_2:26379/0`. If your redis sentinels themselves have a password set the transport_options to `{"master_name":"mymaster","sentinel_kwargs":{"password":"my_password"}}`.

## Sentry

pretix has native support for sentry, a tool that you can use to track errors in the application. If you want to use sentry, you need to set a DSN in the configuration file:

``` ini
[sentry]
dsn=https://<key>:<secret>@sentry.io/<project>
traces_sample_rate=0.5
traces_sample_token=xyz
```

`dsn`

:   You will be given this value by your sentry installation.

`traces_sample_rate`

:   Sample rate for performance monitoring.

`traces_sample_token`

:   If this token is found in a query string, a trace will always be sampled.

## Caching

You can adjust some caching settings to control how much storage pretix uses:

``` ini
[cache]
tickets=48  ; Number of hours tickets (PDF, passbook, …) are cached
```

## Secret length

If you are really paranoid, you can increase the length of random strings pretix uses in various places like order codes, secrets in the ticket QR codes, etc. Example:

``` ini
[entropy]
; Order code needs to be < 16 characters, default is 5
order_code=5
; Ticket secret needs to be < 64 characters, default is 32
ticket_secret=32
; Voucher code needs to be < 255 characters, default is 16
voucher_code=16
```

## External tools

pretix can make use of some external tools if they are installed. Currently, they are all optional. Example:

``` ini
[tools]
pdftk=/usr/bin/pdftk
```

## Maximum upload file sizes

You can configure the maximum file size for uploading various files:

``` ini
[pretix_file_upload]
; Max upload size for images in MiB, defaults to 10 MiB
max_size_image = 12
; Max upload size for favicons in MiB, defaults to 1 MiB
max_size_favicon = 2
; Max upload size for email attachments of manually sent emails in MiB, defaults to 10 MiB
max_size_email_attachment = 15
; Max upload size for email attachments of automatically sent emails in MiB, defaults to 1 MiB
max_size_email_auto_attachment = 2
; Max upload size for other files in MiB, defaults to 10 MiB
; This includes all file upload type order questions
max_size_other = 100
```

## GeoIP

pretix can optionally make use of a GeoIP database for some features. It needs a file in `mmdb` format, for example [GeoLite2](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) or [GeoAcumen](https://github.com/geoacumen/geoacumen-country):

``` ini
[geoip]
path=/var/geoipdata/
filename_country=GeoLite2-Country.mmdb
```
