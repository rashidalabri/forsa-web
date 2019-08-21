"""
Django settings for forsa project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Common(Configuration):

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)
    DEBUG_TOOLBAR = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        'django.contrib.humanize',
        'django.contrib.postgres',
        'django.contrib.sites',
        'django.contrib.sitemaps',

        'django_extensions',
        'debug_toolbar',

        'crispy_forms',
        'bootstrap_pagination',

        'sorl.thumbnail',

        'storages',

        'django_hashedfilenamestorage',

        'forsa.users',

        'wajiha'
    ]

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    ]

    ROOT_URLCONF = 'forsa.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.request',
                    'wajiha.context_processors.google_keys',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'forsa.wsgi.application'

    # Password validation
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
    LANGUAGE_CODE = 'ar-om'

    TIME_ZONE = 'Asia/Muscat'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Authentication
    AUTH_USER_MODEL = 'users.User'

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

    DATABASES = values.DatabaseURLValue(environ_name='DATABASE_URL')

    SITE_ID = 1

    GOOGLE_ANALYTICS_KEY = values.Value('')
    GTM_KEY = values.Value('')

    ADMIN_URL = values.Value('admin/')

    # Hacky solution to a problem
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = 'media/'



class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = values.BooleanValue(True)
    DEBUG_TOOLBAR = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(
        ['dev.forsa.om', 'forsa-development.herokuapp.com', '127.0.0.1'])

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    DEFAULT_FILE_STORAGE = 'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage'

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


class Staging(Common):
    """
    The in-staging settings.
    """
    ALLOWED_HOSTS = ['forsa-staging.herokuapp.com', 'staging.forsa.om']

    DEBUG = values.BooleanValue(True)
    DEBUG_TOOLBAR = values.BooleanValue(True)

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    INTERNAL_IPS = [
        '*'
    ]

    # Security
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    X_FRAME_OPTIONS = 'DENY'

    # Amazon S3 settings
    AWS_ACCESS_KEY_ID = values.Value()
    AWS_SECRET_ACCESS_KEY = values.Value()
    AWS_STORAGE_BUCKET_NAME = values.Value()
    AWS_S3_CUSTOM_DOMAIN = values.Value()

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # Static assets
    AWS_LOCATION = 'static'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

    # Media assets
    DEFAULT_FILE_STORAGE = 'forsa.storage_backends.S3HashedFilenameStorage'

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
        }
    }

    THUMBNAIL_FORCE_OVERWRITE = True

    ADMIN_URL = values.Value()


class Production(Staging):
    """
    The in-production settings.
    """

    DEBUG_TOOLBAR = values.BooleanValue(False)

    MIDDLEWARE = Common.MIDDLEWARE

    ALLOWED_HOSTS = ['forsa-production.herokuapp.com',
                     'forsa.om', 'www.forsa.om']

    GOOGLE_ANALYTICS_KEY = 'UA-145916646-1'
    GTM_KEY = 'GTM-M7NRK2P'
