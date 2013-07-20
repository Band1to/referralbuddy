from django.utils import unittest
from django.conf import settings
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


from mock import Mock

from referrals import views

class ManualRetrieveTests(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        self.factory = RequestFactory()
        self.user = User(**dict(username='sam@webiken.net', 
            email='sam@webiken.net', 
            first_name='Sample', 
            last_name='Buyer',
            is_active=True,
            is_staff=False,
            is_superuser=False))
        self.user.save()

        self.data = {
    u'last_name': [u'Buyer'], 
    u'receiver_email': [u'apps-facilitator@webiken.net'],
    u'residence_country': [u'US'], 
    u'payer_status': [u'verified'], 
    u'txn_type': [u'subscr_signup'], 
    u'first_name': [u'Sample'], 
    u'item_name': [u'Nation Wide Premium Plan'], 
    u'charset': [u'windows-1252'], 
    u'notify_version': [u'3.7'], 
    u'recurring': [u'1'], 
    u'test_ipn': [u'1'], 
    u'business': [u'apps-facilitator@webiken.net'], 
    u'payer_id': [u'P9CUA4KE7JPWU'], 
    u'period3': [u'1 M'], 
    u'verify_sign': [u'APCnqfPpFQ5oEvvR7qWuBqX3RyvrARZCns9PkTZ8tXuNB19iWEuilBdB'], 
    u'subscr_id': [u'I-3GHLTP2JW2ED'], 
    u'amount3': [u'200.00'], 
    u'mc_amount3': [u'200.00'], 
    u'mc_currency': [u'USD'], 
    u'subscr_date': ['20:54:55 Jul 19, 2013 PDT'], 
    u'payer_email': [u'sam@webiken.net'], 
    u'ipn_track_id': [u'a0911c4741c08'],
    'custom' : ['sam@webiken.net'],
    u'reattempt': [u'1']}

    def test_ipn_activate_subscription(self):
        request = self.factory.post(reverse('paypal_ipn'), data=self.data)
        request.session = dict(ipaddress='192.168.1.1')
        response = views.paypal_ipn(request)
        print response.content
        self.assertEqual(response.content, 'ok')
