# Vahti #

Host/IP address pool monitoring daemon and visualization.

## Idea ##

The idea is to monitor used/unused pool of IP addresses. If the address
becomes used, it will be recorded. The tool will list hosts and their
DNS names and record changes.

## Requirements ##

The following tools are required.

 * Foreman (only for starting processes)
 * sqlite3 (for development database)

Additionally some Python libs need to be installed  with pip into a virtualenv
environment.

## Usage ##

    $ mkvirtualenv vahti --no-site-packages
    $ workon vahti
    (vahti) $ cdvirtualenv 
    (vahti) $ echo "export DJANGO_SETTINGS_MODULE=vahti.conf.dev" > bin/postactivate
    (vahti) $ echo "unset DJANGO_SETTINGS_MODULE" > bin/postdeactivate
    # Reload virtualenv hooks
    (vahti) $ workon vahti

    (vahti) $ pip install -r requirements.txt
    (vahti) $ ./manage.py pinghosts --loop &
    (vahti) $ ./manage.py runserver &    

For live deployments, use of supervisord is recommended.

For production, set the environment variable _DJANGO\_SETTINGS\_MODULE_
and create _vahti/conf/private.json_ with content:

    {
        "ADMIN_EMAIL": [
            "foo <foo@example.com>"
        ],
        "SECRET_KEY": "generate a secret random key here"
    }

![Vahti screenshot](http://joneskoo.kapsi.fi/tmp/vahti.png)
