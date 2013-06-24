# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=200)
    #print title
    page_name = models.CharField(max_length=10)
    #print page_name
    pub_date = models.DateTimeField('date published')



    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class PageContent(models.Model):
    page = models.ForeignKey(Page)
    top_content = HTMLField(max_length=500, null=True, blank=True)
    left_content = HTMLField(max_length=500, null=True, blank=True)
    right_content = HTMLField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=False)



    def __unicode__(self):
        return "%s %s" %(self.page.page_name, self.top_content if self.top_content else '')

