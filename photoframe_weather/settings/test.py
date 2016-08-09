from .base import *


CACHE_MIDDLEWARE_SECONDS = 0
COMPRESS_ENABLED = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'var/api_piggy.db'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TOKEN_JWT_EXPIRATION_TIME = 9000
TOKEN_JWT_REFRESH_EXPIRATION_TIME = 24000
TOKEN_JWT_LEEWAY = 0
TOKEN_JWT_ISSUER = "test"
TOKEN_JWT_AUDIENCE = "test"
TOKEN_JWT_SECRET_KEY = "test"
TOKEN_JWT_ALGORITHM = "HS256"
