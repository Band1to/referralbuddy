from django import forms

from tinymce.widgets import TinyMCE

from pages.models import PageContent

class PageContentForm(forms.ModelForm):
	top_content = forms.CharField( widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
	left_content = forms.CharField( widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
	right_content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

	class Meta:
		model = PageContent


