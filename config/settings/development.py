# SPDX-FileCopyrightText: Copyright (C) 2023 Opal Health Informatics Group at the Research Institute of the McGill University Health Centre <john.kildea@mcgill.ca>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Settings for development.

Inspired by cookiecutter-django: https://cookiecutter-django.readthedocs.io/en/latest/index.html
"""

from .base import *  # noqa: F403
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env.str(
    'DJANGO_SECRET_KEY',
    default='OsHmhT0jxfCjlh6MXlsOuDDWiaTe4WLzH2B0NS4Uhq3HDoM6LuMwbEC9Ig1KchNu',
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '44.227.113.66', 'opaladmin.shoprideon.com', '.localhost', '127.0.0.1', '[::1]', 'host.docker.internal'
]

# CACHES
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/cache/
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    },
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env.str('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ['whitenoise.runserver_nostatic', *INSTALLED_APPS]  # noqa: F405


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ['django_extensions']
