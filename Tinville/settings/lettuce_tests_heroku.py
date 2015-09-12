# Django settings for Tinville project.

from .base import *  # Start with base settings
import urlparse

import dj_database_url

# HEROKU Change!!!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['tinville-lettuce.herokuapp.com']

DATABASES = {'default': dj_database_url.config(default=env('DATABASE_URL'))}
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}

DATABASE_POOL_ARGS = {
    'max_overflow': 0,
    'pool_size': env('PG_DB_POOL_SIZE_PER_DYNO', 20),  # Heroku's Standard 0 connection limit (up to 6 dynos * 20 = 120 connections)
    'recycle': 300
}

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.remove('django.middleware.csrf.CsrfViewMiddleware')

DEFAULT_FILE_STORAGE = 'common.s3utils.MediaS3BotoStorage'
STATICFILES_STORAGE = 'common.s3utils.StaticS3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = 'common.s3utils.MediaS3BotoStorage'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = True
AWS_IS_GZIPPED = env('AWS_IS_GZIPPED', True)
AWS_QUERYSTRING_EXPIRE = env('AWS_QUERYSTRING_EXPIRE', 63115200)
AWS_HEADERS = {
    'Cache-Control': str(env('AWS_CACHE_CONTROL', 'public, max-age=2592000')),
}
AWS_S3_FILE_OVERWRITE = env('AWS_S3_FILE_OVERWRITE', False)

S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY

COMPRESS_STORAGE = 'common.s3utils.CompressorS3BotoStorage'
COMPRESS_URL = STATIC_URL
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'GOOGLE_ANALYTICS_TRACKING_ID': GOOGLE_ANALYTICS_TRACKING_ID,
    'MEDIA_URL': MEDIA_URL,
}

SSLIFY_DISABLE = False

SESSION_COOKIE_SECURE = env('SESSION_COOKIE_SECURE', False)
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE', False)

redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL', 'redis://localhost:6959'))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': env('REDIS_POOL_MAX_CONNECTIONS', 50),
                'timeout': env('REDIS_POOL_TIMEOUT', 30),
            }
        }
    }
}





LETTUCE_APPS = (
    'Tinville',
    'designer_shop',
    'user',
    'basket',
    'custom_oscar.apps.customer',
    'custom_oscar.apps.checkout',
    'custom_oscar.apps.dashboard',
    'dashboard',
    'checkout',
)

INSTALLED_APPS = INSTALLED_APPS + ['lettuce',  'django_nose',] + ['extensions',]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'



########## TEST SETTINGS
#TEST_RUNNER = "discover_runner.DiscoverRunner"
#TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
#TEST_DISCOVER_ROOT = PROJECT_DIR
#TEST_DISCOVER_PATTERN = "test_*"
########## IN-MEMORY TEST DATABASE

LETTUCE_TEST_SERVER = env('LETTUCE_TEST_SERVER', 'common.lettuce_extensions.DefaultServer')

TEST_SERVER_ADDRESS = env('TEST_SERVER_ADDRESS', '0.0.0.0')

LETTUCE_RUN_ON_HEROKU = env('LETTUCE_RUN_ON_HEROKU', True)
