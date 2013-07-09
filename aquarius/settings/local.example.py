from aquarius.settings.dev import *

# Override settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aquarius',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
           "init_command": "SET storage_engine=INNODB",
        }   
    }
}