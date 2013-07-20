import urllib, urllib2
import httplib, re

from referrals import models

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

        response = conn.getresponse() 
        log.warn('opening connection to %s' % url)
        ret = response.read() 
        conn.close()
        log.warn('closed connection to %s' % url)
        return ret
    except Exception, e: 
        log.error("error opening connection to %s : message : %s" % (url, e))
        raise RuntimeError(e.message)