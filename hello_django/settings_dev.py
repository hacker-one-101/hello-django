from hello_django.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hellodb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# STATIC_ROOT = '/var/www/app/static'
