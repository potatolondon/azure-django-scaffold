from .base import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0'
        }
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{}:6379'.format(os.environ['REDIS_HOST']),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': os.environ['REDIS_PASSWORD'],
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        },
        'TIMEOUT': None
    },
}

LOG_FILE_NAME = '{}.log'.format(os.environ['WEBSITE_INSTANCE_ID'])
LOG_FILE_PATH = os.path.join('d:/', 'home', 'LogFiles', 'Application', LOG_FILE_NAME)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s'
        }
    },
    'handlers': {
        'logfile': {
            'class': '{{ project_name }}.core.utils.NonLockingFileHandler',
            'filename': LOG_FILE_PATH,
            'formatter': 'simple',
            'delay': '1'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# azure
AZURE_ACCOUNT_NAME = os.environ['BLOBSTORE_ACCOUNT_NAME']
AZURE_ACCOUNT_KEY = os.environ['BLOBSTORE_ACCOUNT_KEY']
AZURE_CONTAINER_STATIC = 'public'
AZURE_CONTAINER_MEDIA = 'media'
AZURE_URL = 'https://{{ project_name }}.blob.core.windows.net/'

# storage
DEFAULT_FILE_STORAGE = '{{ project_name }}.core.storage_backends.AzureMediaStorage'
STATICFILES_STORAGE = '{{ project_name }}.core.storage_backends.AzureStaticStorage'
MEDIA_URL = AZURE_URL + AZURE_CONTAINER_MEDIA + '/'
STATIC_URL = AZURE_URL + AZURE_CONTAINER_STATIC + '/'

# cache the template
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
