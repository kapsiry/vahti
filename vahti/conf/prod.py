import os
import email.utils

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'vahti.sqlite3',
    }
}

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/users/joneskoo/sites/joneskoo.kapsi.fi/secure-www/vahti-static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['SECRET_KEY']

admin_email_list = os.environ['ADMIN_EMAIL'].split(',')
ADMINS = [email.utils.parseaddr(x) for x in admin_email_list]
MANAGERS = ADMINS
