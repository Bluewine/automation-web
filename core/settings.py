"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wi5%3e1_fpxq+fm8sowdg0^(0vz*qv0oryh3ww+adav$+v$e4%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

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
    # 'channels',
    'django_extensions',
    'libs.interactor.interactor',
    'rest_framework',

    # Created apps
    # 'chat',
    'libs',
    'libs.diff2htmlcompare',
    'libs.tcrm_automation',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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

# Login
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
PUBLIC_PATHS = [
    #     # '^%s.*' % MEDIA_URL, # allow public access to any media on your application
    r'^/admin/',
    r'^/admin/login',
    r'^/login/',
    r'^/logout/',
    r'^/register/',
    r'^/rest/.*',
    # r'^/sfdc/authenticate/',
]
# PUBLIC_VIEWS = [
#     'main.views.LoginView',
# ]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "main/templates",
            BASE_DIR / "libs",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # My custom context processors
                'main.context_processors.show_notifications',
            ],
        },
    },
]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAdminUser'
    # ),
}

WSGI_APPLICATION = 'core.wsgi.application'

# # For Websocket using channels package:
# ASGI_APPLICATION = "core.asgi.application"
# # Channel backing store. You have to start first your redis docker or app.
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('localhost', 6379)],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Recomended by Heroku. This is "production" configuration.

static_dir = os.path.join(BASE_DIR, "main/static")  # Static files for development mode
jdd_static_dir = os.path.join(BASE_DIR, "libs/jdd")
jsl_static_dir = os.path.join(BASE_DIR, "libs/jdd/jsl")
STATICFILES_DIRS = [
    static_dir,
    jdd_static_dir,
    jsl_static_dir,
]

# File Upload managers
FILE_UPLOAD_HANDLERS = [
    # "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]

# File storage manager
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# Media files (file uploaded, etc)
# https://docs.djangoproject.com/en/3.2/ref/files/storage/#django.core.files.storage.FileSystemStorage.location
# https://docs.djangoproject.com/en/3.2/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'  # It must end in a slash if set to a non-empty value.

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom configs
SALESFORCE_INSTANCE_URLS = {
    'Sandbox': 'https://test.salesforce.com',
    'Production': 'https://login.salesforce.com',
}
