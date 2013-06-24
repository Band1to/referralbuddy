from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from referrals import models

class CheckProfileMiddleware():

	def process_request(self, request):

		if request.path == '/referrals/get_plan_price/' or request.path == reverse('create_profile') or request.path == reverse('auth_logout') or 'admin' in request.path: return None

		if not request.user.is_authenticated(): return None
		
		try:
			profile = models.EntityProfile.objects.get(user__username=request.user.username)
			return None
		except models.EntityProfile.DoesNotExist:
			return HttpResponseRedirect(reverse('create_profile'))

