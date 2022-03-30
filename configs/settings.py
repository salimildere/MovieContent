import os
import environ

env = environ.Env()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="2l8ecsx$ru29%j!q%#vo)ign&$(mgfm7(8rswa0o+bjhps+!r%"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ["*"]

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
LOCAL_APPS = [
    "movpro.api.apps.ApiConfig",
    "movpro.contents.apps.ContentsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_yasg",
    "django_extensions",
]
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "configs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "configs.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME", default="postgres"),
        "USER": env("DB_USER", default="postgres"),
        "PASSWORD": env("DB_PASSWORD", default="postgres"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "tr-tr"
LANGUAGES = [
    ("tr-tr", "Turkish"),
    # ("en", "English"),
]
TIME_ZONE = "Europe/Istanbul"

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

FIELD = "django.db.models.AutoField"

# REST Framework

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Cache

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "example",
    }
}

CACHE_TTL = 60 * 15
REDIS_HOST = env("REDIS_HOST", default="0.0.0.0")

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Factory for mock db data

IS_ACTIVE_FACTORY = env("IS_ACTIVE_FACTORY", default=True)

try:
    from configs.settings_local import *
except ImportError:
    pass
