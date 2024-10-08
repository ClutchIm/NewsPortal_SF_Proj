"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

from django.conf.global_settings import LANGUAGES

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m@toxn_ex4=7ub$zt5gq$==aqqh89gjx0b_$a58&j0f%2o!6u*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'rest_framework',
]

SITE_ID = 1
SITE_URL = 'http://127.0.0.1:8000'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'basic.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get("DB_HOST"),
#         'NAME': os.environ.get("DB_NAME"),
#         'USER': os.environ.get("DB_USER"),
#         'PASSWORD': os.environ.get("DB_PASS"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_REDIRECT_URL = "/news"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "imclutch"
EMAIL_HOST_PASSWORD = "khdreoablywylhpy"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "imclutch@yandex.ru"

SERVER_EMAIL = "imclutch@yandex.ru"

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

REST_FRAMEWORK = {
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
   'PAGE_SIZE': 10
}

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style' : '{',
    'formatters': {
        'debug': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'info':{
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s '
        },
        'error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'formatter': 'debug',
            'class': 'logging.StreamHandler',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'formatter': 'warning',
            'class': 'logging.StreamHandler',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'formatter': 'error',
            'class': 'logging.StreamHandler',
        },
        'general':{
            'level': 'INFO',
            'formatter': 'info',
            'filters': ['require_debug_false'],
            'filename': os.path.join(BASE_DIR, 'general.log'),
            'class': 'logging.FileHandler',
        },
        'errors':{
            'level': 'ERROR',
            'formatter': 'error',
            'filename': os.path.join(BASE_DIR, 'errors.log'),
            'class': 'logging.FileHandler',
        },
        'security': {
            'level': 'INFO',
            'formatter': 'info',
            'filename': os.path.join(BASE_DIR, 'security.log'),
            'class': 'logging.FileHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'warning',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console_error', 'console_warning', 'console_debug', 'general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': False,
        }
    }
}
"""