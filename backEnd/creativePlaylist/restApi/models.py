from django.db import models


# Create your models here.
class Artist(models.Model):
	"""docstring for Artist"""
	artistName = models.CharField(max_length=255)

	def __init__(self, *args, **kwargs):
		super(Artist, self).__init__(*args,**kwargs)

class Art(models.Model):
	"""docstring for Art"""
	artImage = models.ImageField(upload_to='media/art_image')
	artThumb = models.ImageField(upload_to='media/art_thumb')

	def __init__(self, *args, **kwargs):
		super(Art, self).__init__(*args, **kwargs)
		
class Song(models.Model):
	"""docstring for Song"""
	title = models.CharField(max_length=255)
	songFile = models.FileField(upload_to='media/music')
	artist = models.ForeignKey(Artist)
	art = models.ForeignKey(Art)

	def __init__(self, *args, **kwargs):
		super(Song, self).__init__(*args, **kwargs)
