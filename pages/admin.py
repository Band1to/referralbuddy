from django.contrib import admin
from pages.models import Page, PageContent

from pages.forms import PageContentForm


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
 
        ('Identificatikkan', {'fields': ['page_name']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']} ),

    ]

    def save(self):
    	"""
    	make sure the page name is unique
    	"""
    	super(PageAdmin, self).save()
    	
class PageContentAdmin(admin.ModelAdmin):
	form = PageContentForm

admin.site.register(Page, PageAdmin)
admin.site.register(PageContent, PageContentAdmin)

#admin.site.register(Page)