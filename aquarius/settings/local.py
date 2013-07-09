from aquarius.settings.dev import *

# Override settings here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aquarius',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {
           "init_command": "SET storage_engine=INNODB",
        }   
    }
}