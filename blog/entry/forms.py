from django import forms
from django.forms import ModelForm
from entry.models import Post, Comment

class PostForm(ModelForm):
	title = forms.CharField(error_messages={'required': 'Bitte einen Titel eingeben'})
	content = forms.CharField(min_length=5, widget=forms.Textarea, 
		  error_messages={'required': 'Bitte einen Inhalt eingeben','min_length':'Bitte mindestens 5 Zeichen eingeben'})
	class Meta:
		model = Post
		exclude = ('user')

class CommentForm(ModelForm):
	name = forms.CharField(error_messages={'required': 'Bitte einen Namen eingeben'})
	text = forms.CharField(min_length=5, widget=forms.Textarea, 
		  error_messages={'required': 'Bitte einen Inhalt eingeben','min_length':'Bitte mindestens 5 Zeichen eingeben'})
	email = forms.EmailField(error_messages={'required': 'Bitte eine Email-Adresse eingeben', 'invalid': 'Bitte eine korrekte Email-Adresse eingeben'})
	post = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput)
	class Meta:
		model = Comment

