from aquarius.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_SUBJECT_PREFIX = '[aquarius Staging] '

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = False

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = ('.examplewww.com',)
SESSION_COOKIE_DOMAIN = '.examplewww.com'

WSGI_APPLICATION = 'aquarius.wsgi.staging.application'