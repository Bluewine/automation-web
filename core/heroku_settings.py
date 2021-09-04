"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import dj_database_url
import django_heroku
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra apps
    'apscheduler',
    'bootstrap4',
    'django_apscheduler',
    'django_extensions',
    'libs.interactor.interactor',
    'mathfilters',
    'rest_framework',
    'whitenoise.runserver_nostatic',

    # Created apps
    'libs',
    'libs.diff2htmlcompare',
    'libs.tcrm_automation',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise for Heroku
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Rest of the default middlewares
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Global Login required
    'global_login_required.GlobalLoginRequiredMiddleware',

    # Custom Middlewares
    'main.middleware.SfdcCRUDMiddleware',
    'main.middleware.TimezoneMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tcrm_db',
        'USER': 'tcrm_user',
        'PASSWORD': '7YjvxvWLC8',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Activate Django-Heroku.
django_heroku.settings(locals())

# Configure database for Heroku
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

# Static file handler for Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
