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
    'backend.api.accounts',
    'backend.api.experiences',
]

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

############
# SECURITY #
############
DEBUG = False

ALLOWED_HOSTS = ['tajruba1.herokuapp.com/', '*']

CORS_ORIGIN_ALLOW_ALL = True
