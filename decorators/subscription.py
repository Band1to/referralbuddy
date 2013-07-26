from datetime import datetime

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from paypal.standard.ipn.models import PayPalIPN

from referrals import models

def check_subscription(func):
	def wrap(request, *args, **kwargs):
		profile = models.EntityProfile.objects.get(user__username=request.user.username)
		#now check if this user is an organization
		if profile.entity_type == 'org':
			#check if they have an active subscription
			subscription = PayPalIPN.objects.filter(username=request.user.username, txn_type='subscr_payment').order_by('-time_created')

			if len(subscription) == 0:
				return HttpResponseRedirect(reverse('subscription_pending'))

			if subscription[0].subscr_effective > datetime.now():
				return func(request, *args, **kwargs)
			else:
				return HttpResponseRedirect(reverse('subscription_inactive'))
	return wrap