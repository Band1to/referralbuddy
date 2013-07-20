# Django settings for referralbuddy project.
import os
from django.core.urlresolvers import reverse_lazy

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    
)

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

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
    'middleware.checkprofile.CheckProfileMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'referrals.context_processors.paypal_button_image',
    'referrals.context_processors.paypal_cc_image',
    'referrals.context_processors.paypal_action_url',
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
    'tinymce',
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
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level':'WARN',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '%s/logs/rb.log' % (SITE_DIR),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'WARN',
        },
    }
}



ACCOUNT_ACTIVATION_DAYS = 7


BROKER_URL = 'django://'

AUTH_PROFILE_MODULE = 'referrals.EntityProfile'

LOGIN_REDIRECT_URL = reverse_lazy('home')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_buttons3_add' : "forecolor,backcolor, textcolor",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'convert_urls' : False
}

SITE_EMAIL_ADDRESS = 'info@referralbuddy.com.au'

SITE_ADMIN_NAME = 'Referral Buddy'

NO_REPLY_EMAIL = 'noreply@referralbuddy.com.au'

NO_REPLY_NAME = 'Do Not Reply'

ELASIC_EMAIL_API_SERVER = 'api.elasticemail.com'

ELASTIC_EMAIL_API_URL = '/mailer/send'

ELASTIC_EMAIL_SUCCESS_MATCH_PATTERN = '^[0-9|a-f]{8}-[0-9|a-f]{4}-[0-9|a-f]{4}-[0-9|a-f]{4}-[0-9|a-f]{12}$' 

ELASTIC_EMAIL_ERROR_MATCH_PATTERN = '^Error:'

try:
    from local_settings import *
except ImportError, e:
    pass