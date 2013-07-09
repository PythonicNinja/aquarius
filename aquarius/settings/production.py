from aquarius.settings.staging import *

# There should be only minor differences from staging
# Override settings here
import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

DATABASES['default']['NAME'] = 'aquarius_production'

EMAIL_SUBJECT_PREFIX = '[aquarius Prod] '

