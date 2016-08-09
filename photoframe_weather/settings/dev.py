from .base import *

import raven

from .partials.sentry import RAVEN_CONFIG
from .partials.paths import *

# "Dev catch all" property key by default in development
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'photoframe_weather',
        'USER': 'photoframe_weather',
        'HOST': 'localhost',
        'PORT': '',           # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

DEFAULT_FROM_EMAIL = 'no-reply@broadleyspeaking.co.nz'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# As required by debug_toolbar
INTERNAL_IPS = (
    '10.0.2.2', # external
    '127.0.0.1' # localhost
)

INSTALLED_APPS += (
    'debug_toolbar',
    # 'debug_panel',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'debug_panel.middleware.DebugPanelMiddleware',
) + MIDDLEWARE_CLASSES

LOGGING['loggers']['core']['handlers'] = ['console']
LOGGING['loggers']['core']['level'] = 'DEBUG'
LOGGING['loggers']['django']['handlers'] = ['console']
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['oauth']['handlers'] = ['console']
LOGGING['loggers']['oauth']['level'] = 'DEBUG'
LOGGING['loggers']['celery']['handlers'] = ['celery']
LOGGING['loggers']['celery']['level'] = 'DEBUG'

API_SERVICE_CARETAKER = 'caretaker'
API_SERVICE_APP = 'app'

API_SERVICES = {
    API_SERVICE_CARETAKER: 'http://10.0.2.2:8081',
    API_SERVICE_APP: 'http://10.0.2.2:8082'
}

RAVEN_CONFIG.update({
    'release': raven.fetch_git_sha(DJANGO_ROOT)
})

try:
    from .local import *
except ImportError:
    pass
