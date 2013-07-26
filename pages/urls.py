from django.conf.urls import patterns, include, url

from referrals.facebook import facebook_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pages.views',
	url(r'', include('social_auth.urls')),

    ###STATIC PAGES
    url(r'^$', "home", name='home'),
    url(r'pages/(?P<page_name>\w*)$', "get_page", name='pages'),

    ###REFERRALS
    url(r'^referrals/', include('referrals.urls')),

    ###ADMIN SITE
    url(r'^admin/', include(admin.site.urls)),

    ###SOCIAL AUTH
    url(r'', include('social_auth.urls')),

    ###FACEBOOK AUTH
    url(r'^fb/', facebook_view, name='fb_app'),

    ###DJANGO-REGISTRATION
    url(r'^accounts/', include('registration.urls')),
    
    ###POSTMAN
    url(r'^messages/', include('postman.urls')),

    (r'^tinymce/', include('tinymce.urls')),
)