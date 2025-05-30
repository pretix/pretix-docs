# Small-scale manual deployment

This guide describes the installation of a small-scale installation of pretix from source. By small-scale, we mean that everything is being run on one host and you don't expect thousands of participants trying to get a ticket within a few minutes. In this setup, you will have to perform a number of manual steps. If you prefer using a container solution with many things readily set-up, look at [Small-scale deployment with docker](./docker_smallscale.md).

!!! Warning

    Even though we try to make it straightforward to run pretix, it still requires some Linux experience to get it right. If you're not feeling comfortable managing a Linux server, check out our hosting and service offers at [pretix.eu](https://pretix.eu/).

We tested this guide on the Linux distribution **Debian 12** but it should work very similar on other modern distributions, especially on all systemd-based ones.

## Requirements

Please set up the following systems beforehand, we'll not explain them here in detail (but see these links for external installation guides):

-   A python 3.9+ installation
-   A SMTP server to send out mails, e.g. [Postfix](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-22-04) on your machine or some third-party server you have credentials for
-   A HTTP reverse proxy, e.g. [nginx](https://botleg.com/stories/https-with-lets-encrypt-and-nginx/) or Apache to allow HTTPS connections
-   A [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-22-04) 12+ database server
-   A [redis](https://blog.programster.org/debian-8-install-redis-server/) server
-   A [nodejs](https://github.com/nodesource/distributions/blob/master/README.md#deb) installation

We also recommend that you use a firewall, although this is not a pretix-specific recommendation. If you're new to Linux and firewalls, we recommend that you start with [ufw](https://en.wikipedia.org/wiki/Uncomplicated_Firewall).

!!! Note

    Please, do not run pretix without HTTPS encryption. You'll handle user data and thanks to [Let's Encrypt](https://letsencrypt.org/) SSL certificates can be obtained for free these days. We also *do not* provide support for HTTP-only installations except for evaluation purposes.

## Unix user

As we do not want to run pretix as root, we first create a new unprivileged user:

``` console
# adduser pretix --disabled-password --home /var/pretix
```

In this guide, all code lines prepended with a `#` symbol are commands that you need to execute on your server as `root` user (e.g. using `sudo`); all lines prepended with a `$` symbol should be run by the unprivileged user.

## Database

Having the database server installed, we still need a database and a database user. We can create these with any kind of database managing tool or directly on our database's shell. Please make sure that UTF8 is used as encoding for the best compatibility. You can check this with the following command:

``` console
# sudo -u postgres psql -c 'SHOW SERVER_ENCODING'
```

For PostgreSQL database creation, we would do:

``` console
# sudo -u postgres createuser pretix
# sudo -u postgres createdb -O pretix pretix
```

## Package dependencies

To build and run pretix, you will need the following debian packages:

``` console
# apt-get install git build-essential python3-dev python3-venv python3 \
                  python3-pip libxml2-dev libxslt1-dev libffi-dev \
                  zlib1g-dev libssl-dev gettext libpq-dev libjpeg-dev \
                  libopenjp2-7-dev
```

## Config file

We now create a config directory and config file for pretix:

``` console
# mkdir /etc/pretix
# touch /etc/pretix/pretix.cfg
# chown -R pretix:pretix /etc/pretix/
# chmod 0600 /etc/pretix/pretix.cfg
```

Fill the configuration file `/etc/pretix/pretix.cfg` with the following content (adjusted to your environment):

``` ini
[pretix]
instance_name=My pretix installation
url=https://pretix.mydomain.com
currency=EUR
datadir=/var/pretix/data
trust_x_forwarded_for=on
trust_x_forwarded_proto=on

[database]
backend=postgresql
name=pretix
user=pretix
; For PostgreSQL on the same host, we don't need a password because we can use
; peer authentication if our PostgreSQL user matches our unix user.
password=
; For local postgres authentication, you can leave it empty
host=

[mail]
; See config file documentation for more options
from=tickets@yourdomain.com
host=127.0.0.1

[redis]
location=redis://127.0.0.1/0
sessions=true

[celery]
backend=redis://127.0.0.1/1
broker=redis://127.0.0.1/2
```

See [Email settings](../config.md#email) to learn more about configuring mail features.

## Install pretix from PyPI

Now we will install pretix itself. The following steps are to be executed as the `pretix` user. Before we actually install pretix, we will create a virtual environment to isolate the python packages from your global python installation:

``` console
# sudo -u pretix -s
$ python3 -m venv /var/pretix/venv
$ source /var/pretix/venv/bin/activate
(venv)$ pip3 install -U pip setuptools wheel
```

We now install pretix, its direct dependencies and gunicorn:

``` console
(venv)$ pip3 install pretix gunicorn
```

Note that you need Python 3.9 or newer. You can find out your Python version using `python -V`.

We also need to create a data directory and allow your webserver to traverse to the root directory:

``` console
(venv)$ mkdir -p /var/pretix/data/media
(venv)$ chmod +x /var/pretix
```

Finally, we compile static files and translation data and create the database structure:

``` console
(venv)$ python -m pretix migrate
(venv)$ python -m pretix rebuild
```

## Start pretix as a service

We recommend starting pretix using systemd to make sure it runs correctly after a reboot. Create a file named `/etc/systemd/system/pretix-web.service` with the following content:

``` systemd
[Unit]
Description=pretix web service
After=network.target

[Service]
User=pretix
Group=pretix
Environment="VIRTUAL_ENV=/var/pretix/venv"
Environment="PATH=/var/pretix/venv/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/var/pretix/venv/bin/gunicorn pretix.wsgi \
                      --name pretix --workers 5 \
                      --max-requests 1200  --max-requests-jitter 50 \
                      --log-level=info --bind=127.0.0.1:8345
WorkingDirectory=/var/pretix
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

For background tasks we need a second service `/etc/systemd/system/pretix-worker.service` with the following content:

``` systemd
[Unit]
Description=pretix background worker
After=network.target

[Service]
User=pretix
Group=pretix
Environment="VIRTUAL_ENV=/var/pretix/venv"
Environment="PATH=/var/pretix/venv/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/var/pretix/venv/bin/celery -A pretix.celery_app worker -l info
WorkingDirectory=/var/pretix
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

You can now run the following commands to enable and start the services:

``` console
# systemctl daemon-reload
# systemctl enable pretix-web pretix-worker
# systemctl start pretix-web pretix-worker
```

## Cronjob

You need to set up a cronjob that runs the management command `runperiodic`. The exact interval is not important but should be something between every minute and every hour. You could for example configure cron like this:

``` none
15,45 * * * * export PATH=/var/pretix/venv/bin:$PATH && cd /var/pretix && python -m pretix runperiodic
```

The cronjob should run as the `pretix` user (`crontab -e -u pretix`).

## SSL

The following snippet is an example on how to configure a nginx proxy for pretix:

``` nginx
server {
    listen 80 default_server;
    listen [::]:80 ipv6only=on default_server;
    server_name pretix.mydomain.com;
    location / {
        return 301 https://$host$request_uri;
    }
}
server {
    listen 443 ssl default_server;
    listen [::]:443 ipv6only=on ssl default_server;
    server_name pretix.mydomain.com;

    ssl_certificate /path/to/cert.chain.pem;
    ssl_certificate_key /path/to/key.pem;

    add_header Referrer-Policy same-origin;
    add_header X-Content-Type-Options nosniff;

    location / {
        proxy_pass http://localhost:8345;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header Host $http_host;
    }

    location /media/ {
        alias /var/pretix/data/media/;
        expires 7d;
        access_log off;
    }

    location ^~ /media/cachedfiles {
        deny all;
        return 404;
    }
    location ^~ /media/invoices {
        deny all;
        return 404;
    }

    location /static/staticfiles.json {
        deny all;
        return 404;
    }
    location /static/CACHE/manifest.json {
        deny all;
        return 404;
    }
    location /static/ {
        alias /var/pretix/venv/lib/python3.11/site-packages/pretix/static.dist/;
        access_log off;
        expires 365d;
        add_header Cache-Control "public";
    }
}
```

!!! Note

    Remember to replace the `python3.11` in the `/static/` path in the config above with your python version.

We recommend reading about setting [strong encryption settings](https://mozilla.github.io/server-side-tls/ssl-config-generator/) for your web server.

## Next steps

Yay, you are done! You should now be able to reach pretix at <https://pretix.yourdomain.com/control/> and log in as *admin@localhost* with a password of *admin*. Don't forget to change that password! Create an organizer first, then create an event and start selling tickets!

You should probably read [Backups and monitoring](../maintenance.md) next.

## Updates

!!! Warning

    While we try hard not to break things, **please perform a backup before every upgrade**.

To upgrade to a new pretix release, pull the latest code changes and run the following commands:

``` console
# sudo -u pretix -s
$ source /var/pretix/venv/bin/activate
(venv)$ pip3 install -U --upgrade-strategy eager pretix gunicorn
(venv)$ python -m pretix migrate
(venv)$ python -m pretix rebuild
(venv)$ python -m pretix updateassets
# systemctl restart pretix-web pretix-worker
```

Make sure to also read [Update notes](../updates.md) and the release notes of the version you are updating to. Pay special attention to the "Runtime and server environment" section of all release notes between your current and new version.

## Install a plugin

To install a plugin, just use `pip`! Depending on the plugin, you should probably apply database migrations and rebuild the static files afterwards. Replace `pretix-passbook` with the plugin of your choice in the following example:

``` console
$ source /var/pretix/venv/bin/activate
(venv)$ pip3 install pretix-passbook
(venv)$ python -m pretix migrate
(venv)$ python -m pretix rebuild
# systemctl restart pretix-web pretix-worker
```

## System updates

After system updates, such as updates to a new Ubuntu or Debian release, you might be using a new Python version. That's great, but requires some adjustments. First, adjust any old version paths in your nginx configuration file. Then, re-create your Python environment:

``` console
$ source /var/pretix/venv/bin/activate
(venv)$ pip3 freeze > /tmp/pip-backup.txt
$ rm -rf /var/pretix/venv
$ python3 -m venv /var/pretix/venv
$ source /var/pretix/venv/bin/activate
(venv)$ pip3 install -U pip wheel setuptools
(venv)$ pip3 install -r /tmp/pip-backup.txt
```

Then, proceed like after any plugin installation:

``` console
(venv)$ python -m pretix migrate
(venv)$ python -m pretix rebuild
(venv)$ python -m pretix updateassets
# systemctl restart pretix-web pretix-worker
```
