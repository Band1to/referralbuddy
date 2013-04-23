# Django settings for referralbody project.
import os

from local_settings import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pages.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pages.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

AUTHENTICATION_BACKENDS = (
    'backends.emailbackend.EmailBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    ###DJANGO-APPS
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    ###THIRD PARTY LIBRARIES
    'django_openid_auth',
    'django.contrib.admin',
    'social_auth',
    'djcelery',
    'kombu.transport.django',
    'paypal.standard.ipn',
    'postman',
    'pagination',
    ###LOCAL APPS
    'pages',
    'referrals',
    'registration',
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



FACEBOOK_APP_ID                   = '361510763943252'
FACEBOOK_API_SECRET               = '2f02398f50a91ac1aea21676a098c53b'
FACEBOOK_EXTENDED_PERMISSIONS     = ['email', 'publish_stream']

TWITTER_CONSUMER_KEY              = 'brWqfOYENR4q5VMGSTw'
TWITTER_CONSUMER_SECRET           = 'eVqv0sxKta5bgbitKAGpiBnm9XCLGS0mCJSggB3GYJI'

ACCOUNT_ACTIVATION_DAYS = 7


BROKER_URL = 'django://'

from django.contrib.sites.models import Site

HOSTNAME = Site.objects.get_current()

PAYPAL_RECEIVER_EMAIL = "seller_1355087471_biz@webiken.net"

PAYPAL_BUTTON_IMAGE = "https://www.sandbox.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif"

PAYPAL_CC_IMAGE = "https://www.sandbox.paypal.com/en_US/i/scr/pixel.gif"

PAYPAL_ACTION_URL = "https://www.sandbox.paypal.com/cgi-bin/webscr"

PAYPAL_NOTIFY_URL = "http://%s/referrals/nationwide_paypal_ipn" % HOSTNAME

PAYPAL_CANCEL_RETURN_URL = "http://%s/referrals/nationwdide_paypal_cancel" % HOSTNAME

PAYPAL_RETURN_URL = "http://%s:8000/referrals/nationwide_paypal_return" % HOSTNAME

PAYPAL_TEST = True

PAYPAL_ITEM_NAME = "Nationwide Finance"

AUTH_PROFILE_MODULE = 'referrals.EntityProfile'