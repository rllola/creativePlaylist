from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL
from restApi.models import Artist, Art, Song
from django.contrib.auth.models import User

class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)

            return data

        return super(MultipartResource, self).deserialize(request, data, format)

class UserResource(MultipartResource, ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		#TODO : Unsecure get ride of this after testing
		authorization= Authorization()
		filtering = { "username" : ALL }

class ArtistResource(MultipartResource, ModelResource):
	class Meta:
		queryset = Artist.objects.all()
		resource_name = 'artist'
		#TODO : Unsecure get ride of this after testing
		authorization= Authorization()
		filtering = { "artistName" : ALL }

class ArtResource(MultipartResource, ModelResource):
    artImage = fields.FileField(attribute="artImage", null=True, blank=True)
    artThumb = fields.FileField(attribute="artThumb", null=True, blank=True)
    class Meta:
        queryset = Art.objects.all()
        resource_name = 'art'
        authorization = Authorization()

class SongResource(MultipartResource, ModelResource):
    songFile = fields.FileField(attribute="songFile", null=True, blank=True)
    artist = fields.ForeignKey(ArtistResource, 'artist')
    art = fields.ForeignKey(ArtResource, 'art')
    user = fields.ForeignKey(UserResource, 'submitedByUser')
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'
        authorization = Authorization()