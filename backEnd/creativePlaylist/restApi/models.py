from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Artist(models.Model):
	"""docstring for Artist"""
	artistName = models.CharField(max_length=255)

	def __init__(self, *args, **kwargs):
		super(Artist, self).__init__(*args,**kwargs)

class Art(models.Model):
	"""docstring for Art"""
	artImage = models.ImageField(upload_to='art_image')
	artThumb = models.ImageField(upload_to='art_thumb')

	def __init__(self, *args, **kwargs):
		super(Art, self).__init__(*args, **kwargs)
		
class Song(models.Model):
	"""docstring for Song"""
	#TODO : Addin default value (user : request.User)
	title = models.CharField(max_length=255)
	songFile = models.FileField(upload_to='media/music')
	artist = models.ForeignKey(Artist)
	art = models.ForeignKey(Art)
	submitedByUser = models.ForeignKey(User, null=True)

	def __init__(self, *args, **kwargs):
		super(Song, self).__init__(*args, **kwargs)
