from tastypie.resources import ModelResource
from tastypie.constants import ALL
from restApi.models import Artist
from django.contrib.auth.models import User

class ArtistResource(ModelResource):
	class Meta:
		queryset = Artist.objects.all()
		resource_name = 'artists'
		filtering = { "artistName" : ALL }

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'users'
		filtering = { "username" : ALL }