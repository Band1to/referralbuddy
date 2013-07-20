import urllib, urllib2
import httplib, re

from django.template.loader import get_template
from django.utils.html import strip_tags
from django.contrib.sites.models import Site
from django.template import Context
from django.core import mail
from django.conf import settings

import utils

import logging
log = logging.getLogger(__file__)


# def send_email(subject=None, body=None, to_email=None, fail_silently=False):
#     params = dict(
#         subject = subject,
#         body = body,
#         from_email = 'info@referralbuddy.com.au',
#         to = to_email,
#     )
#     try:
#         connection = mail.get_connection(fail_silently=fail_silently)
#         connection.open()
#         email = mail.EmailMessage(**params)
#         email.content_subtype = "html"
#         email.send()
#         connection.close()
#     except ValueError, e:
#         raise ValueError('Invalid backend argument')

def send_email(template=None, subject=None, to_email=None): 

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

    log.warn("sending email to %s" % to_email)

    ret = utils.http_utils(settings.ELASIC_EMAIL_API_SERVER, settings.ELASTIC_EMAIL_API_URL, msg_info)

     # Check return value 
    if re.search(settings.ELASTIC_EMAIL_SUCCESS_MATCH_PATTERN, ret): 
        return True
    else:
        raise RuntimeError("please contact admins") 
        


def send_new_user_email(referrer=None, referred=None, business_name=None):
    t = get_template('new_referrer_email.html')

    site = Site.objects.get_current()

    c1 = Context(dict(user = referrer, business_name = business_name, site = site))
    c2 = Context(dict(user = referred, business_name = business_name, site = site))

    body1 = t.render(c1)
    body2 = t.render(c2)

    subject = 'Welcome to Nationwide Finance'

    if not referrer.is_active: send_email(subject=subject, body=body1, to_email=[referrer.email])
    if not referred.is_active: send_email(subject=subject, body=body2, to_email=[referred.email])

