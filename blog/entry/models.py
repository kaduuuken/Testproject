from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField("Titel",max_length=200, blank=False,)
	content = models.TextField("Inhalt", blank=False)
	pub_date = models.DateTimeField('Datum','date published',auto_now_add=True)
	'''user = models.ForeignKey(User, null=True)'''
	
	def __unicode__(self):
		return "Eintrag: %s" % (self.title)

	class Meta:
		ordering = ['-pub_date']
		verbose_name = "Blog-Eintrag"
		verbose_name_plural = "Blog-Eintraege"

class Comment(models.Model):
	name = models.CharField("Name",max_length=200)
	email = models.EmailField("Email-Adresse")
	text = models.TextField("Kommentar")
	pub_date = models.DateTimeField("Datum",'date published', auto_now_add=True)
	post = models.ForeignKey(Post,related_name='comments')

	def __unicode__(self):
		return "Kommentar von: %s" % (self.name)

	class Meta:
		ordering = ['-pub_date']
		verbose_name = "Kommentar"
		verbose_name_plural = "Kommentare"
