from datetime import datetime

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from paypal.standard.ipn.models import PayPalIPN

from referrals import models

class CheckProfileMiddleware():

	def process_request(self, request):

		filter_urls = ('/referrals/get_plan_price/', reverse('create_profile'), reverse('auth_logout'), reverse('subscription_pending'))

		request.session['ipaddress'] = request.META['REMOTE_ADDR']

		if request.path in filter_urls or 'admin' in request.path: return None

		if not request.user.is_authenticated(): return None
		
		try:
			profile = models.EntityProfile.objects.get(user__username=request.user.username)

			#now check if this user is an organization
			if profile.entity_type == 'org':
				#check if they have an active subscription
				try:
					subscription = PayPalIPN.objects.get(username=request.user.username).order_by('-time_created')
					if subscription.subscr_effective > datetime.now():
						return None
					else:
						return HttpResponseRedirect(reverse('subscription_inactive'))
				except PayPalIPN.DoesNotExist:
					return HttpResponseRedirect(reverse('subscription_pending'))

			return None
		except models.EntityProfile.DoesNotExist:
			return HttpResponseRedirect(reverse('create_profile'))

