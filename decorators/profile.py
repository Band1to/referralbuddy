from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from referrals import models

def check_profile(func):
	def wrap(request, *args, **kwargs):
		try:
			profile = models.EntityProfile.objects.get(user__username=request.user.username)
			return func(request, *args, **kwargs)
		except Exception, e:
			return HttpResponseRedirect(reverse('create_profile'))
	return wrap

def home(func):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated():
			home_view = check_profile(func)
			return home_view(request, *args, **kwargs)
		else:
			return func(request, *args, **kwargs)
	return wrap