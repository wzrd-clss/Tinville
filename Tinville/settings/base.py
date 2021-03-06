# Django settings for Tinville project.
from decimal import Decimal
import os
import os.path
from celery.schedules import crontab
from getenv import env
from unipath import Path
from django.utils.translation import ugettext_lazy as _
from oscar import get_core_apps
from oscar.defaults import *


# HEROKU Change!!!
DEBUG = env('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Jon Meran', 'jon.meran@tinville.com')
)

MANAGERS = ADMINS

AUTH_USER_MODEL = 'user.TinvilleUser'

PROJECT_DIR = Path(__file__).ancestor(2)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This assumes the first Site in the database will be used!!
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

USE_THOUSAND_SEPARATOR = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_DIR.child("media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ""

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child("static"),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'minidetector.Middleware',
    # The below clickjacking middleware must be last in the list.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.middleware.PromoterMiddleware',

)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'Tinville.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Tinville.wsgi.application'

from oscar import OSCAR_MAIN_TEMPLATE_DIR
location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child("templates"),
    PROJECT_DIR.parent.child("custom_oscar").child("apps").child("dashboard").child("templates"),
    PROJECT_DIR.parent.child("custom_oscar").child("apps").child("customer").child("templates"),
    PROJECT_DIR.parent.child("custom_oscar").child("apps").child("catalogue").child("templates"),
    PROJECT_DIR.parent.child("partials"),
    OSCAR_MAIN_TEMPLATE_DIR
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'user.context_processors.include_login_form',
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
    'Tinville.context_processors.google_analytics_id',
    'Tinville.context_processors.include_shops',
    'user.context_processors.get_user_shop',
    )

# Actual Tinville business logic
# django-jenkins needs it defined in this variable
PROJECT_APPS = [
    'Tinville',
    'user',
    'basket',
    'designer_shop',
    'common'
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'crispy_forms',
    'braces',
    'parsley',
    'django_jenkins',
    'fixture_media',
    'django_extensions',
    'compressor',
    'tinymce',
    # 'sorl.thumbnail',
    'django_basic_feedback',
    'debug_toolbar',
    'oscar_stripe',
    'kombu.transport.django',
    'djcelery',
    'raven.contrib.django.raven_compat',
    'django_bleach',
    'easy_thumbnails',
    'image_cropping',
    'smart_load_tag',
    'floppyforms',
    'endless_pagination',
    'django.contrib.sitemaps',
    'robots',
    'rollyourown.seo',
    'django_dowser',
    'filer',
    'mptt',
    'flatpages_filer',
    'markitup',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'bootstrapform',
] + PROJECT_APPS + get_core_apps(['custom_oscar.apps.catalogue',
                                  # 'custom_oscar.apps.basket',
                                  'custom_oscar.apps.customer',
                                  'custom_oscar.apps.checkout',
                                  'custom_oscar.apps.dashboard',
                                  'custom_oscar.apps.dashboard.orders',
                                  'custom_oscar.apps.dashboard.pages',
                                  'custom_oscar.apps.order'])


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': env('LOGGING_HANDLER_SENTRY_LEVEL', 'WARNING'),
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'level': env('LOGGING_LOGGER_DJANGO_REQUEST_LEVEL', 'WARNING'),
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'django.db.backends': {
            'level': env('LOGGING_LOGGER_DJANGO_DB_BACKENDS_LEVEL', 'WARNING'),
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'django.security': {
            'level': env('LOGGING_LOGGER_DJANGO_SECURITY_LEVEL', 'WARNING'),
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'celery': {
            'level': 'WARNING',
            'handlers': ['sentry'],
            'propagate': False,
        },
    },
}

ENDLESS_PAGINATION_PER_PAGE = 20
ENDLESS_PAGINATION_LOADING = """<div class="well col-md-offset-4 col-xs-12 col-md-4"><div class="row"><div class="col-xs-12 fa fa-spinner fa-spin center-block" style="text-align: center;"></div></div></div>"""

# For django-oscar search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# DJANGO OSCAR SETTINGS
OSCAR_HOMEPAGE = "/"
OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:order-list'
OSCAR_DEFAULT_CURRENCY = '$'
OSCAR_INITIAL_ORDER_STATUS = 'Ready for Shipment'
OSCAR_INITIAL_LINE_STATUS = 'Ready for Shipment'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Ready for Shipment': ('Partially Shipped', 'Shipped', 'Cancelled'),
    'Partially Shipped': ('Shipped', 'Returned', 'Partially Cancelled'),
    'Shipped': ('Returned', 'Partially Shipped'),
    'Cancelled': (),
}

OSCAR_LINE_STATUS_PIPELINE = {
    'Ready for Shipment': ('Partially Shipped', 'Shipped', 'Cancelled'),
    'Partially Shipped': ('Shipped', 'Returned', 'Partially Cancelled'),
    'Shipped': ('Returned', 'Partially Shipped'),
    'Cancelled': (),
}
OSCAR_ALLOW_ANON_CHECKOUT = True

# Menu structure of the dashboard navigation
OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'glyphicon-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'glyphicon-book',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'glyphicon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.heroku.com', 'herokuapp.com', 'www.tinville.com']

STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'menubar': True,
    'statusbar': False,
    'width': "75%",
    'height': "250px",
    'font-size': '22',
    'plugins': "spellchecker, paste, searchreplace, advimage",  
    'theme_advanced_buttons1': "fontsizeselect, separator, bold, italic, underline, separator, outdent, indent",
    'cleaup_on_startup': True,
    'theme_advanced_path': False
    
}
TINYMCE_SPELLCHECKER = True
TINYMCE_PASTE = True

# to be overridden in other settings files
GOOGLE_ANALYTICS_TRACKING_ID = ''

STRIPE_PUBLISHABLE_KEY = env('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_CURRENCY = 'USD'

#TODO change easy post api key
EASYPOST_API_KEY = env('EASYPOST_API_KEY')

# Celery settings
BROKER_URL = 'django://'
import djcelery
djcelery.setup_loader()

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_BACKEND= 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERYBEAT_SCHEDULE = {
    # Pay designers twice a week, Tuesday at 1AM EST
    'pay-designers-on-tuesdays-midnight': {
        'task': 'custom_oscar.apps.order.tasks.pay_designers',
        'schedule': crontab(hour=1, minute=0, day_of_week=2)
    },
}

TINVILLE_ORDER_SALES_CUT = Decimal(0.20)  # Tinville takes 20% of designer sales
TINVILLE_PROMOTER_SALES_CUT = Decimal(0.03)  # Tinville pays our 3% of sales to promoters
TINVILLE_PROMOTER_MINIMUM_PAYOUT = Decimal(10.00)  # Tinville pays out only after $10 in promotion sales have been made

# Sentry Logging parameters
RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN'),
}
SENTRY_AUTO_LOG_STACKS = True


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'span']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style']

# Which CSS properties are allowed in 'style' attributes (assuming
# style is an allowed attribute)
BLEACH_ALLOWED_STYLES = [
    'font-family', 'font-weight', 'text-decoration', 'font-variant', 'font-size', 'padding-left', 'padding-right']

# Strip unknown tags if True, replace with HTML escaped characters if
# False
BLEACH_STRIP_TAGS = True

# Strip comments, or leave them in.
BLEACH_STRIP_COMMENTS = True

BLEACH_DEFAULT_WIDGET = 'tinymce.widgets.TinyMCE'


# Django Debug Toolbar
def show_toolbar(request):
    if env('SHOW_DEBUG_TOOLBAR_FOR_ALL', False):
        return True
    if request.user.is_authenticated():
        return request.user.is_staff and env('SHOW_DEBUG_TOOLBAR_FOR_STAFF', False)
    else:
        return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'Tinville.settings.base.show_toolbar'
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

COMPRESS_ENABLED = env("COMPRESS_ENABLED", False)
COMPRESS_OFFLINE = env("COMPRESS_OFFLINE", False)
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'GOOGLE_ANALYTICS_TRACKING_ID': GOOGLE_ANALYTICS_TRACKING_ID,
    'MEDIA_URL': MEDIA_URL,
}

THUMBNAIL_DEBUG = env("THUMBNAIL_DEBUG", False)

DISABLE_BETA_ACCESS_CHECK = env('DISABLE_BETA_ACCESS_CHECK', True)

from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

LOCAL_STATIC_SERVE = env("LOCAL_STATIC_SERVE", False)

#Overriding oscars required address fields for custom validation
OSCAR_REQUIRED_ADDRESS_FIELDS = {}

OSCAR_HIDDEN_FEATURES = ["reviews"]


# needed to make this work with bootstrap labels
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/markitup'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})

# all_auth
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "none"

FACEBOOK_CLIENT_ID = env('FACEBOOK_CLIENT_ID')
FACEBOOK_SECRET = env('FACEBOOK_SECRET')
INSTAGRAM_CLIENT_ID = env('INSTAGRAM_CLIENT_ID')
INSTAGRAM_SECRET = env('INSTAGRAM_SECRET')