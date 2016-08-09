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
    'corsheaders',
    'core',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


# Django rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'api_partial_authentication.oauth_consumer.services.JWTTokenAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'ALLOWED_VERSIONS':  ('v1',  'v2'),
    'DEFAULT_VERSION':  'v1',
    'VERSION_PARAM': None
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

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE'
)
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding'
)