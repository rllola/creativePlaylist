from tastypie.resources import ModelResource, Resource
#from tastypie.authorization import Authorization
#Changing for bitAuth
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from tastypie.constants import ALL
from restApi.models import Artist, Art, Song
from django.contrib.auth.models import User
from tastybitauth.authentication import BitAuthAuthentication

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
        excludes = ['id', 'email']
        authentication = BitAuthAuthentication()

class ArtistResource(MultipartResource, ModelResource):
	class Meta:
		queryset = Artist.objects.all()
		resource_name = 'artist'
        #TODO : Change for bitAuth
        #authentication = ApiKeyAuthentication()
        #authorization = Authorization()
        excludes = ['id']
        filtering = { "artistName" : ALL }

class ArtResource(MultipartResource, ModelResource):
    artImage = fields.FileField(attribute="artImage", null=True, blank=True)
    artThumb = fields.FileField(attribute="artThumb", null=True, blank=True)
    class Meta:
        queryset = Art.objects.all()
        resource_name = 'art'
        excludes = ['id']
        #TODO : Change for bitAuth
        #authentication = ApiKeyAuthentication()
        #authorization = Authorization()

class SongResource(MultipartResource, ModelResource):
    songFile = fields.FileField(attribute="songFile", null=True, blank=True)
    artist = fields.ForeignKey(ArtistResource, 'artist', full=True)
    art = fields.ForeignKey(ArtResource, 'art', full=True)
    user = fields.ForeignKey(UserResource, 'submitedByUser', full=True)
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'
        excludes = ['id']
        #TODO : Change for bitAuth
        authentication = BitAuthAuthentication()
        #authorization = Authorization()
        