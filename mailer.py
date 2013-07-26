import urllib, urllib2
import httplib, re, base64

from django.template.loader import get_template
from django.utils.html import strip_tags
from django.contrib.sites.models import Site
from django.template import Context
from django.core import mail
from django.conf import settings
from django.core.urlresolvers import reverse

import utils

import logging
log = logging.getLogger(__file__)

def send_email(template=None, subject=None, to_email=None, params=None): 

    if template is None:
        raise RuntimeError("YOU ARE MISSING THE TEMPLATE NAME")

    # Build message structure 
    msg_info = {} 
    msg_info['username'] = settings.ELASTIC_EMAIL_USERNAME  
    msg_info['api_key'] = settings.ELASTIC_EMAIL_API_KEY 
    msg_info['from'] = settings.SITE_EMAIL_ADDRESS 
    msg_info['from_name'] = settings.SITE_ADMIN_NAME 
    msg_info['to'] = ';'.join(to_email)
    msg_info['subject'] = subject 
    # msg_info['body_text'] = "html body"
    # msg_info['body_html'] = body 
    msg_info['template'] = template
    msg_info['reply_to'] = settings.NO_REPLY_EMAIL
    msg_info['reply_to_name'] = settings.NO_REPLY_NAME 
    msg_info['channel'] = 'Channel Name'

    if params:
        msg_info.update(params)

    log.warn("sending email to %s" % to_email)

    ret = utils.http_utils(settings.ELASIC_EMAIL_API_SERVER, settings.ELASTIC_EMAIL_API_URL, msg_info)

     # Check return value 
    if re.search(settings.ELASTIC_EMAIL_SUCCESS_MATCH_PATTERN, ret): 
        return True
    else:
        raise RuntimeError("please contact admins") 
        


def send_new_user_email(referrer=None, referred=None, business_name=None):
    site = Site.objects.get_current()
    subject = 'ReferrerBuddy Referral'
    
    try:
        template1 = 'new_referrer'
        b64_email1 = base64.b64encode(referrer.email)
        params1 = dict(merge_first_name=referrer.first_name, merge_email=referrer.email, merge_business_name=business_name, merge_site=site, merge_url=reverse('referrer_first_login', args=(b64_email1,)))
        if not referrer.is_active: send_email(template=template1, subject=subject, to_email=[referrer.email], params=params1)
    except Exception, e:
        log.error('exception while sending referrer email %s' % e)

    try:
        template2 = 'new_referred'
        b64_email2 = base64.b64encode(referred.email)
        params2 = dict(merge_first_name=referred.first_name, merge_email=referred.email, merge_business_name=business_name, merge_site=site, merge_url=reverse('referrer_first_login', args=(b64_email2,)))
        if not referred.is_active: send_email(template=template2, subject=subject, to_email=[referred.email], params=params2)
    except Exception, e:
        log.error('exception while sending ReferrerBuddy email %s' % e)

