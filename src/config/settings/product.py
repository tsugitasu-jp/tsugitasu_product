# base.pyから共通設定をインポート
from .base import *

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