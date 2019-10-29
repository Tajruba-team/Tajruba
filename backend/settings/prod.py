""" Production Settings """
import os
import dj_database_url

from .dev import *


############
# APPS     #
############
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'knox',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',

    'backend.api',
    'backend.api.core',
    'backend.api.accounts',
    'backend.api.experiences',
]

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

############
# SECURITY #
############
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ['tajruba1.herokuapp.com', '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True

############
# EMAIL    #
############
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = os.environ.get('SERVER_EMAIL')
