import os
from decouple import config
from pathlib import Path
import django
from urllib import request
import django_on_heroku
import dj_database_url
import boto3


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config ('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool) 

ALLOWED_HOSTS = ['cyclicpms.herokuapp.com','127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # admin area model config 
    # 'contacts.apps.ContactAdminConfig',

    # django packages
    
    'django.contrib.humanize',
    'ckeditor',

    # my apps 
    'payroll.apps.PayrollConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'confidentials.apps.ConfidentialsConfig',
    'blogs.apps.BlogsConfig',
    'managements.apps.ManagementsConfig',
    'dashboards.apps.DashboardsConfig',
    'leave.apps.LeaveConfig',
    'category.apps.CategoryConfig',
    'directors.apps.DirectorsConfig',
    # for widgets customizations 

    'widget_tweaks',
    'storages',
    # 'django-storages',
]

# Changing the default user model
AUTH_USER_MODEL     = 'accounts.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'managements.LoginCheckMiddleware.LoginCheckMiddleware',
]


ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# AWS BUCKET 

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config( 'AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None 
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False



CORS_ALLOW_ALL_ORIGINS = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

X_FRAME_OPTIONS ='SAMEORIGIN'


LOGIN_REDIRECT_URL = 'accounts-verify'
# LOGOUT_REDIRECT_URL = 'accounts-auth'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Default notifications 
from django.contrib.messages import constants as messages
MESSAGE_TAGS ={
    messages.ERROR:'danger'
}

SUMMERNOTE_THEME = 'bs4'

# SMTP Configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

django_on_heroku.settings(locals())