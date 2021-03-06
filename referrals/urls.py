from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('referrals.views',
	url(r'^create-profile/$', 'create_profile', name='create_profile'),
	url(r'^edit_profile/$', 'edit_profile', name='edit_profile'),
	url(r'^add_referral/$', 'add_referral', name='add_referral'),
	#url(r'^add_referred/(?P<user_id>\d+)/$', 'add_referred', name='add_referred'),
	url(r'^calculate_gifts/$', 'calculate_gifts',name='calculate_gifts'),
	url(r'^calculate_gifts_check/$', 'calculate_gifts_check',name='calculate_gifts_check'),
	url(r'^first_login/(?P<b64email>(\w*\W*)*)$', 'referrer_first_login', name='referrer_first_login'),
	url(r'^view_referrers/', 'view_referrers', name='view_referrers'),
	url(r'^view_referred/', 'view_referred', name='view_referred'),
	url(r'^add_referral_autocomplete/', 'add_referral_autocomplete', name='add_referral_autocomplete'),
	url(r'^post_to_facebook/', 'post_to_facebook', name='post_to_facebook'),
	url(r'^post_to_twitter/', 'post_to_twitter', name='post_to_twitter'),
	url(r'^search_referrers/', 'search_referrers', name='search_referrers'),
	url(r'^search_organization/', 'search_organization', name='search_organization'),
	url(r'^get_plan_price/', 'get_plan_price', name='get_plan_price'),
	url(r'^send_message/', 'send_message', name='send_message'),
	url(r'^rb-nwf-pp-ipn/', 'paypal_ipn', name='paypal_ipn'),
	url(r'^subscription-pending', 'subscription_pending',  name='subscription_pending'),
	url(r'^subscription-inactive', 'subscription_inactive',  name='subscription_inactive'),
	url(r'^rb-paypal-return/', 'rb_paypal_return', name='rb_paypal_return'),
	url(r'^rb-paypal-cancel/', 'rb_paypal_cancel', name='rb_paypal_cancel'),
	
)
