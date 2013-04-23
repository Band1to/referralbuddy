from django import shortcuts
from django.http import HttpResponse
from django.template import RequestContext

from pages.models import Page, PageContent


def home(request, template='index.html'):
    try:
        content = PageContent.objects.filter(page__page_name='home_page', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome", 
                content = content
            ),
            context_instance=RequestContext(request))

def support(request, template='support.html'):
    try:
        content = PageContent.objects.filter(page__page_name='support', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome to support page", 
                content = content
            ),
            context_instance=RequestContext(request))


def features(request,template='features.html'):
    try:
        content = PageContent.objects.filter(page__page_name='features', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome to features page", 
                content = content
            ),
            context_instance=RequestContext(request))

def privacy_policy(request,template='privacy_policy.html'):
    try:
        content = PageContent.objects.filter(page__page_name='privacy_po', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome to Privacy Policy page", 
                content = content
            ),
            context_instance=RequestContext(request))

def terms_conditions(request, template='terms_conditions.html'):
    try:
        content = PageContent.objects.filter(page__page_name='terms_cond', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome to Terms and Conditions Page", 
                content = content
            ),
            context_instance=RequestContext(request))


def disclaimer(request, template='disclaimer.html'):
    try:
        content = PageContent.objects.filter(page__page_name='disclaimer', is_active=True).latest('page__pub_date')
    except:
        content = None

    return shortcuts.render_to_response(template,
            dict(
                title = content.page.title if content else "Welcome to Disclaimer page", 
                content = content
            ),
            context_instance=RequestContext(request))

def site_map(request, template='site_map.html'):
    return shortcuts.render_to_response(template,
        dict(),
            context_instance=RequestContext(request))