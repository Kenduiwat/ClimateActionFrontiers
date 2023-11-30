"""
Django settings for ClimateActionFrontier_EmobilisProjectShowcasing project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3$zye)#0^#t3k*ajee4n6ci!_(=#iexpf*^n3k6zuv7l7md%%_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime}  {process:d}  {message}',
            'style': '{',
        },
    },
    'handlers': {
        'newfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['newfile'],
            'propagate': True,
        },
    },
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'mainapp.apps.MainappConfig',
    "django.contrib.humanize",
    'rest_framework',
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ClimateActionFrontier_EmobilisProjectShowcasing.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = "ClimateActionFrontier_EmobilisProjectShowcasing.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mainapp/assets')
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "vkorir.vkk@gmail.com"
EMAIL_HOST_PASSWORD = "oejprsuffdggbcmq"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field




CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MESSAGE_TAGS = {
    messages.SUCCESS: "alert-success",
    messages.INFO: "alert-info",
    messages.ERROR: "alert-danger",
    messages.DEBUG: "alert-dark",
    messages.WARNING: "alert-warning",
}

LOGIN_URL = "/signin"

handler404 = 'mainapp.views.handler404'
handler500 = 'mainapp.views.handler500'

MPESA_API = {
    "BIZ_SHORT_CODE": "174379",
    "CALLBACK_URL": "https://eo3o20s5sc4h2wk.m.pipedream.net",  # TODO use ngrok
    "CONSUMER_KEY": "9uTfviRT6oGw9N0f2AkAchjJTVOIDPCS",
    "CONSUMER_SECRET": "UsZqMgpiYURy1KFD",
    "CREDENTIALS_URL": "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
    "PAYMENT_URL": "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
    "PASS_KEY": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
}
