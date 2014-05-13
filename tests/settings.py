import getpass
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ['*']

# Make sure the copy of pgcrypto in the directory above this one is used.
sys.path.insert(0, BASE_DIR)

SECRET_KEY = 'django_pgcrypto_tests__this_is_not_very_secret'

INSTALLED_APPS = (
    'core',
)

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgcrypto',
        'USER': getpass.getuser(),
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

PGCRYPTO_DEFAULT_KEY = 'secret'
