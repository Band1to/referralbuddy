from django.utils import unittest
from django.conf import settings
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from paypal.standard.ipn.models import PayPalIPN


from mock import Mock

from referrals import views
import utils

class PayPalIPNTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.factory = RequestFactory()
        cls.user = User(**dict(username='sam@webiken.net', 
            email='sam@webiken.net', 
            first_name='Sample', 
            last_name='Buyer',
            is_active=True,
            is_staff=False,
            is_superuser=False))
        cls.user.save()

        cls.data = {
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

    def test_sigup_ipn(self):
        views.utils.http_utils = Mock(return_value="VERIFIED")

        request = self.factory.post(reverse('paypal_ipn'), data=self.data)
        request.session = dict(ipaddress='192.168.1.1') 
        response = views.paypal_ipn(request)
        print response.content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'ok')
        ipn = PayPalIPN.objects.filter(username=self.data.get('custom'), txn_type='subscr_signup')[0]
        self.assertEqual(ipn.subscr_id, self.data.get('subscr_id'))

    def test_payment_ipn(self):
        views.verify_ipn = Mock(return_value="VERIFIED")
        views.utils.http_utils = Mock(return_value="f74b9f96-f89a-4cfe-813f-5f86df1cb37f")
        self.data = {u'protection_eligibility': [u'Ineligible'], u'last_name': [u'Buyer'], 
        u'txn_id': [u'29B086831A497564T'], u'receiver_email': [u'apps-facilitator@webiken.net'], 
        u'payment_status': [u'Completed'], u'payment_gross': [u'100.00'], u'residence_country': [u'US'], 
        u'payer_status': [u'verified'], u'txn_type': [u'subscr_payment'], 
        u'payment_date': [u'00:21:27 Jul 20, 2013 PDT'], u'first_name': [u'Sample'], 
        u'item_name': [u'Nation Wide Basic Plan'], u'charset': [u'windows-1252'], 
        u'custom': [u'sam@webiken.net'], u'notify_version': [u'3.7'], 
        u'transaction_subject': [u'Nation Wide Basic Plan'], u'test_ipn': [u'1'], 
        u'receiver_id': [u'UJW568NKYXBR8'], u'business': [u'apps-facilitator@webiken.net'], 
        u'payer_id': [u'P9CUA4KE7JPWU'], 
        u'verify_sign': [u'Ai-FzWGYDKmBlnQl-iAuG4atWtVOAYUT5uh0b-cGS1JWp30A6iztyGCO'], 
        u'subscr_id': [u'I-4C7W7BVETGSD'], u'payment_fee': [u'3.20'], 
        u'mc_fee': [u'3.20'], u'mc_currency': [u'USD'], 
        u'payer_email': [u'buyer@referralbuddy.com.au'], u'payment_type': [u'instant'], 
        u'mc_gross': [u'100.00'], u'ipn_track_id': [u'c12713fac59fd']}

        self.data.update({'payer_email' : 'sam@webiken.net'})
        request = self.factory.post(reverse('paypal_ipn'), data=self.data)
        request.session = dict(ipaddress='192.168.1.1') 
        response = views.paypal_ipn(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'ok') 
        ipn = PayPalIPN.objects.filter(username=self.data.get('custom'), txn_type='subscr_payment')[0]
        self.assertEqual(ipn.subscr_id, self.data.get('subscr_id'))
        self.assertEqual(ipn.txn_id, self.data.get('txn_id'))   


    # def test_ipn_activate_subscription(self):
    #     request = self.factory.post(reverse('paypal_ipn'), data=self.data)
    #     request.session = dict(ipaddress='192.168.1.1')
    #     response = views.paypal_ipn(request)
    #     print response.content
    #     self.assertEqual(response.content, 'ok')
