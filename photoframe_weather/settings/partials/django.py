from .paths import *

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

SERVER_ENV = "Development"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'raven.contrib.django.raven_compat',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


# Django rest framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
       'rest_framework.renderers.JSONRenderer',
       'rest_framework.renderers.BrowsableAPIRenderer',
   )
}

# Name and email addresses of recipients
ADMINS = (
    ('Tech', 'tech@penny.co.nz'),
)

# Default from address for CMS auto email messages (logs, errors..)
SERVER_EMAIL = 'errors-%s@penny.co.nz' % SITE_NAME

# Default from address for CMS email messages to users (forgot password etc..)
DEFAULT_FROM_EMAIL = '%s@penny.co.nz' % SITE_NAME

ROOT_URLCONF = SITE_NAME + '.urls'

WSGI_APPLICATION = SITE_NAME + '.wsgi.application'
