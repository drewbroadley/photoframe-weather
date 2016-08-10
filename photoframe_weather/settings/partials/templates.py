from .paths import *

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            DJANGO_ROOT + '/photoframe_weather/templates'
        ]
    },
]