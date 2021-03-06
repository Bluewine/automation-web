import dj_database_url
import django_heroku


INSTALLED_APPS.append('whitenoise.runserver_nostatic')

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

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

# Activate Django-Heroku.
django_heroku.settings(locals())

# Configure database for Heroku
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

# Static file handler for Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
