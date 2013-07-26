import dateutil
from datetime import timedelta
import urllib, urllib2
import httplib, re

from django.conf import settings

from referrals import models
from paypal.standard.ipn.models import PayPalIPN

import logging
log = logging.getLogger(__name__)



def calculate_points(referred_list, processed=None, value=None):
    referrals = models.EntityReferral.objects.filter(referred__pk__in=referred_list)
    if len(referrals) == 0: return
    referred_list = []
    for referral in referrals:
        referred_list.append(referral.referrer.pk)

        try:
            referral_point = models.ReferrerPoints.objects.get(referrer__pk=referral.referrer.pk)
            referral_point.value += value
        except models.ReferrerPoints.DoesNotExist:
            referral_point = models.ReferrerPoints(referrer=referral.referrer, entity_active=True, value=value)

        referral_point.save()
    if not processed: 
        processed = set([entity['id'] for referral in referrals for entity in referral.referred.values()])
    else: 
        processed|=set([entity['id'] for referral in referrals for entity in referral.referred.values()])
    print processed
    print referred_list

    return calculate_points([referral.referrer.id for referral in referrals if referral.referrer.id not in processed], processed=processed, value=value)

def http_utils(connection, url, data=None, method='POST', https=True):
    try: 
        if https:
            conn = httplib.HTTPSConnection(connection)
        else:
            conn = httplib.HTTPConnection(connection)

        if method == 'POST':
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'} 
            params = urllib.urlencode(data)
            conn.request(method, url, params, headers) 
        else:
            conn.request(method, url)

        log.warn('opening connection to %s' % url)
        response = conn.getresponse() 
        ret = response.read() 
        log.warn('received response %s from %s ' % (ret, url))
        conn.close()
        log.warn('closed connection to %s' % url)
        log.warn('returned after connection closed is %s' % ret)
        return ret
    except Exception, e: 
        log.error("error opening connection to %s : message : %s" % (url, e))
        raise RuntimeError(e.message)

def create_subscription(user, data, ipaddress):

    subscr_date =  dateutil.parser.parse(data.get('subscr_date'))
    subscr_effective = subscr_date + timedelta(days=30)
    _dict = dict(
            subscr_id = data.get('subscr_id'),
            business = settings.PAYPAL_ITEM_NAME,
            first_name = data.get('first_name', user.first_name),
            last_name = data.get('last_name', user.last_name),
            payer_email = data.get('payer_email'),
            payer_id = data.get('payer_id'),
            amount1 = data.get('amount1', 0.0),
            amount2 = data.get('amount2', 0.0),
            amount3 = data.get('amount3', 0.0),
            mc_amount1 = data.get('mc_amount1', 0.0),
            mc_amount2 = data.get('mc_amount2', 0.0),
            mc_amount3 = data.get('mc_amount3', 0.0),
            subscr_date = subscr_date,
            username = user.username,
            notify_version = data.get('notify_version'),
            receiver_email = 'info@referralbuddy.com.au',
            txn_type = data.get('txn_type'),
            mc_currency = data.get('mc_currency'),
            recurring = data.get('recurring'),
            test_ipn = data.get('test_ipn', False),
            subscr_effective = None,
            next_payment_date = subscr_effective,
            time_created = datetime.now(),
            ipaddress = ipaddress,
    )
        
    log.warn("saving subscription information for %s from IPN" % user.username)
    ipn = PayPalIPN(**_dict)
    ipn.save()

def activate_subscription(user, data, ipaddress):
    subscr_date =  dateutil.parser.parse(data.get('payment_date'))
    subscr_effective = subscr_date + timedelta(days=30)

    _dict = dict(
            subscr_id = data.get('subscr_id'),
            business = settings.PAYPAL_ITEM_NAME,
            first_name = data.get('first_name', user.first_name),
            last_name = data.get('last_name', user.last_name),
            payer_email = data.get('payer_email'),
            payer_id = data.get('payer_id'),
            amount1 = data.get('amount1', 0.0),
            amount2 = data.get('amount2', 0.0),
            amount3 = data.get('amount3', 0.0),
            mc_amount1 = data.get('mc_amount1', 0.0),
            mc_amount2 = data.get('mc_amount2', 0.0),
            mc_amount3 = data.get('mc_amount3', 0.0),
            subscr_date = subscr_date,
            username = user.username,
            notify_version = data.get('notify_version'),
            receiver_email = 'info@referralbuddy.com.au',
            txn_type = data.get('txn_type'),
            mc_currency = data.get('mc_currency'),
            recurring = 1,
            test_ipn = data.get('test_ipn', False),
            subscr_effective = subscr_effective,
            next_payment_date = subscr_effective,
            time_created = datetime.now(),
            ipaddress = ipaddress,
    )
        
    log.warn("saving subscription information for %s from IPN" % user.username)
    ipn = PayPalIPN(**_dict)
    ipn.save()