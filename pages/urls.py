from django.conf.urls import patterns, include, url

from referrals.facebook import facebook_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pages.views',
	url(r'', include('social_auth.urls')),

    ###STATIC PAGES
    url(r'^$', "home", name='home'),
    url(r'support/$', "support", name='support'),
    url(r'features/$', "features", name='features'),
    url(r'privacy_policy/$', "privacy_policy", name='privacy_policy'),
    url(r'terms_conditions/$', "terms_conditions", name='terms_conditions'),
    url(r'disclaimer/$', "disclaimer", name='disclaimer'),
    url(r'site_map/$', "site_map", name='site_map'),

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