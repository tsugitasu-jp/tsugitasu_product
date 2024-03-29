"""
Django settings for project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from drf_firebase_auth.utils import map_firebase_uid_to_username
from pymongo import MongoClient

import os
import configparser

SECRET_KEY = 'qn7y!5zf$u#l*z4*ndp6jq#l#u38=fm!60s40%+6p_9r$#+-^2'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conf = configparser.ConfigParser()
settingsFilePath = os.path.join(BASE_DIR, "settings.ini")
conf.read_file(open(settingsFilePath, "r"))

env = conf['os']['user']

# 環境の切り分け
if env == "test":
    ALLOWED_HOSTS = ['*']

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'drf_firebase_auth',
        'rest_framework',
        'users',
        'apiv1',
        'storages',
        'corsheaders'
    ]

    # S3 config
    AWS_STORAGE_BUCKET_NAME = conf['s3']['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': conf['s3']['CacheControl-max-age'],
    }
    AWS_LOCATION = 'static'
    AWS_DEFAULT_ACL = None

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

elif env == "local":
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'drf_firebase_auth',
        'rest_framework',
        'users',
        'apiv1',
        'corsheaders'
    ]

    STATIC_URL = '/static/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# 追記
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'drf_firebase_auth.authentication.FirebaseAuthentication',
    ]
}

DRF_FIREBASE_AUTH = {
    # allow anonymous requests without Authorization header set
    'ALLOW_ANONYMOUS_REQUESTS': os.getenv('ALLOW_ANONYMOUS_REQUESTS', False),
    # path to JSON file with firebase secrets
    'FIREBASE_SERVICE_ACCOUNT_KEY':
        os.getenv('FIREBASE_SERVICE_ACCOUNT_KEY', conf['firebase']['account_key']),
    # allow creation of new local users in db
    'FIREBASE_CREATE_LOCAL_USER':
        os.getenv('FIREBASE_CREATE_LOCAL_USER', True),
    # attempt to split firebase users.display_name and set local users
    # first_name and last_name
    'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME':
        os.getenv('FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME', False),
    # commonly JWT or Bearer (e.g. JWT <token>)
    'FIREBASE_AUTH_HEADER_PREFIX':
        os.getenv('FIREBASE_AUTH_HEADER_PREFIX', 'JWT'),
    # verify that JWT has not been revoked
    'FIREBASE_CHECK_JWT_REVOKED':
        os.getenv('FIREBASE_CHECK_JWT_REVOKED', True),
    # require that firebase users.email_verified is True
    'FIREBASE_AUTH_EMAIL_VERIFICATION':
        os.getenv('FIREBASE_AUTH_EMAIL_VERIFICATION', False),
    # function should accept firebase_admin.auth.UserRecord as argument
    # and return str
    'FIREBASE_USERNAME_MAPPING_FUNC': map_firebase_uid_to_username
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': conf['db']['name'], # 初回migrateでdb作成
        'CLIENT': {
            'host': conf['db']['host'], # ホスト名はdocker imageに合わせる
            'username': conf['db']['user'],
            'password': conf['db']['pass'],
        }
    }
}

# pymongo経由でのアクセス
client = MongoClient(f"mongodb://{conf['db']['user']}:{conf['db']['pass']}@mongo:{conf['db']['port']}")
tsugitasu_db = client['tsugitasu']

# Application definition
AUTH_USER_MODEL = 'users.User'

# Celery設定
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/1')
#CELERY_RESULT_BACKEND = "task_management"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS config
AWS_ACCESS_KEY_ID = conf['aws']['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = conf['aws']['AWS_SECRET_ACCESS_KEY']


# CORS
CORS_ORIGIN_ALLOW_ALL=False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'http://localhost',
    'http://127.0.0.1',
]
