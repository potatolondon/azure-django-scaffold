from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
