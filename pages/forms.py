from django import forms

from pages.models import PageContent

class PageContentForm(forms.ModelForm):
	top_content = forms.CharField( widget= forms.Textarea(attrs={'class':'sameh'}))
	left_content = forms.CharField( widget = forms.Textarea())
	right_content = forms.CharField( widget = forms.Textarea())

	class Meta:
		model = PageContent


