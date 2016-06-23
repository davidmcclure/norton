

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'norton',
        'USER': 'norton',
        'PASSWORD': 'Um4xQLw2^Gnw*f*p',
    }
}


RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
}


STATIC_ROOT = '/opt/norton/static'
