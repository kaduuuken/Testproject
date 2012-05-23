from django import forms
from django.forms import ModelForm
from entry.models import Post

class PostForm(ModelForm):
	title = forms.CharField(error_messages={'required': 'Bitte einen Titel eingeben'})
	content = forms.CharField(min_length=5, widget=forms.Textarea, 
		  error_messages={'required': 'Bitte einen Inhalt eingeben','min_length':'Bitte mindestens 5 Zeichen eingeben'})
	class Meta:
		model = Post

