from .base import *

ALLOWED_HOSTS = ['*']

SERVER_ENV = "Production"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True
COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True

# Make sure we include the needed Middleware apps
# Excluding logged in (admin) requests
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

LOGGING['loggers']['core']['handlers'].append('mail_admins')
LOGGING['loggers']['django']['handlers'].append('mail_admins')

DEFAULT_FROM_EMAIL = 'no-reply@broadleyspeaking.co.nz'

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'

LOGGING['loggers']['core']['handlers'] = ['sentry']
LOGGING['loggers']['core']['level'] = 'ERROR'
LOGGING['loggers']['django']['handlers'] = ['sentry']
LOGGING['loggers']['django']['level'] = 'ERROR'
LOGGING['loggers']['oauth']['handlers'] = ['sentry']
LOGGING['loggers']['oauth']['level'] = 'ERROR'
LOGGING['loggers']['celery']['handlers'] = ['sentry']
LOGGING['loggers']['celery']['level'] = 'ERROR'

try:
    from .local import *
except ImportError:
    pass
