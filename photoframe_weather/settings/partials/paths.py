from os.path import abspath, basename, dirname, join
from sys import path

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(dirname(dirname(abspath(__file__)))))

# Absolute filesystem path to the top-level project folder:
PROJECT_ROOT = dirname(DJANGO_ROOT)

PHOTO_ROOT = "/home/photos"
PHOTO_URL_ROOT = "https://dl.dropboxusercontent.com/u/3444322/Photos/Screensaver/"


# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = join(DJANGO_ROOT, 'assets')
STATIC_URL = '/assets/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = ()

MEDIA_ROOT = join(DJANGO_ROOT, 'var', 'media')
MEDIA_URL = '/media/'