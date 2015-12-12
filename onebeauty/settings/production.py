import os
import dj_database_url
from shoop.addons import add_enabled_addons
from django.utils.crypto import get_random_string

DEBUG = False
TEMPLATE_DEBUG = False


SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BASE_DIR = os.path.abspath(os.path.join(SITE_ROOT, ".."))

# Application definition
SHOOP_ENABLED_ADDONS_FILE = os.getenv("SHOOP_ENABLED_ADDONS_FILE") or (
    os.path.join(BASE_DIR, "var", "enabled_addons"))


DATABASES = {
    "default": dj_database_url.config(default="postgresql://"),
}

# Enable Connection Pooling (if desired)
DATABASES['default']['CONN_MAX_AGE'] = 500

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SITE_NAME = "One beauty"
SITE_DOMAIN = "onebeauty.herokuapp.com"
PREPEND_WWW = False

INSTALLED_APPS = add_enabled_addons(SHOOP_ENABLED_ADDONS_FILE, [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # custom shop
    'shop',
    # shoop themes
    'shoop.themes.classic_gray',
    # shoop
    'shoop.addons',
    'shoop.admin',
    'shoop.api',
    'shoop.core',
    'shoop.default_tax',
    'shoop.front',
    'shoop.front.apps.auth',
    'shoop.front.apps.customer_information',
    'shoop.front.apps.personal_order_history',
    'shoop.front.apps.registration',
    'shoop.front.apps.simple_order_notification',
    'shoop.front.apps.simple_search',
    'shoop.notify',
    'shoop.simple_cms',
    'shoop.simple_pricing',
    'shoop.simple_supplier',
    'shoop.testing',
    'shoop.utils',
    'shoop.xtheme',
    # external apps
    'bootstrap3',
    'django_jinja',
    'easy_thumbnails',
    'filer',
    'registration',
    'rest_framework',

    'shoop.discount_pricing',
    'herokuapp',
    'storages',
])

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'shoop.front.middleware.ProblemMiddleware',
    'shoop.front.middleware.ShoopFrontMiddleware',
)


_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.request",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages"
            ],
            "newstyle_gettext": True,
            "environment": "shoop.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.request",
                "django.core.context_processors.tz",
                "django.contrib.messages.context_processors.messages"
            ],
            "debug": DEBUG
        }
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'
SOUTH_TESTS_MIGRATE = False  # Makes tests that much faster.
ROOT_URLCONF = 'onebeauty.urls'
WSGI_APPLICATION = 'onebeauty.wsgi.application'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    )
}

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('ja', 'Japanese'),
]

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"


# SHOOP
SHOOP_ENABLED_ADDONS_FILE = os.path.join(BASE_DIR,"..", "var", "enabled_addons")
SHOOP_PRICING_MODULE = "simple_pricing"

HEROKU_APP_NAME = "onebeauty"
# Allow all host headers
# Change it later for real production
ALLOWED_HOSTS = [
                SITE_DOMAIN,
                "{HEROKU_APP_NAME}.herokuapp.com".format(
                    HEROKU_APP_NAME=HEROKU_APP_NAME,)]



# Amazon S3 settings.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_AUTO_CREATE_BUCKET = True
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}

AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = True
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Use Amazon S3 for storage for uploaded media files.
MEDIAFILES_LOCATION ='media'
DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
MEDIA_ROOT = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# Use Amazon S3 for static files storage.
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = "onebeauty.storage.StaticStorage"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


# Additional static file locations.

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

# Email settings.

EMAIL_HOST = "smtp.sendgrid.net"

EMAIL_HOST_USER = os.environ.get("SENDGRID_USERNAME")

EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_PASSWORD")

EMAIL_PORT = 25

EMAIL_USE_TLS = False

SERVER_EMAIL = u"{name} <notifications@{domain}>".format(
    name = SITE_NAME,
    domain = SITE_DOMAIN,
)

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_SUBJECT_PREFIX = "[%s] " % SITE_NAME


# Error reporting settings.  Use these to set up automatic error notifications.

ADMINS = ()

MANAGERS = ()

SEND_BROKEN_LINK_EMAILS = False

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Cache settings.
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # Long cache timeout for staticfiles, since this is used heavily by the optimizing storage.
    "staticfiles": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 60 * 60 * 24 * 365,
        "LOCATION": "staticfiles",
    },
}


# A secret key used for cryptographic algorithms.

SECRET_KEY = os.environ.get("SECRET_KEY", get_random_string(50, "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"))

# Logging configuration.

LOGGING = {
    "version": 1,
    # Don't throw away default loggers.
    "disable_existing_loggers": False,
    "handlers": {
        # Redefine console logger to run in production.
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        # Redefine django logger to use redefined console logging.
        "django": {
            "handlers": ["console"],
        }
    }
}

if os.environ.get("SHOOP_WORKBENCH_DISABLE_MIGRATIONS") == "1":
    from .utils import DisableMigrations
    MIGRATION_MODULES = DisableMigrations()


def configure(setup):
    setup.commit(globals())