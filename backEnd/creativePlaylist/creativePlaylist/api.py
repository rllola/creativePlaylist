from tastypie.resources import ModelResource, Resource
from django.conf.urls import url
from tastypie.authorization import Authorization
#Changing for bitAuth
#from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields
from tastypie.constants import ALL
from restApi.models import Artist, Art, Song, Address
from django.contrib.auth.models import User
from tastybitauth.authentication import BitAuthAuthentication
from tastypie.exceptions import Unauthorized

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
        authentication = BitAuthAuthentication()
        print authentication
        resource_name = 'user'
        fields = ['username']

class LoginUserResource(MultipartResource, ModelResource):
    class Meta:
        authentication = BitAuthAuthentication()
        authorization = Authorization()
        queryset = User.objects.all()
        resource_uri = False
        resource_name = 'login'
        detail_uri_name = 'username'
        fields = ['id','username']

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

    # TODO : change that for Authorization customize
    def authorized_read_detail(self, object_list, bundle):
        """
        Handles checking of permissions to see if the user that authenticated has the good username
        """
        try:
            auth_result = object_list[0] == bundle.request.user
            if not auth_result is True:
                raise Unauthorized()
        except Unauthorized as e:
                self.unauthorized_result(e)
        return auth_result


class ArtistResource(MultipartResource, ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artist'
        authentication = BitAuthAuthentication()
        fields = ['artistName']


class ArtResource(MultipartResource, ModelResource):
    #artImage = fields.FileField(attribute="artImage", null=True, blank=True)
    artThumb = fields.FileField(attribute="artThumb", null=True, blank=True)
    class Meta:
        queryset = Art.objects.all()
        resource_name = 'art'
        excludes = ['id', 'artImage']
        authentication = BitAuthAuthentication()


class SongResource(MultipartResource, ModelResource):
    songFile = fields.FileField(attribute="songFile", null=True, blank=True)
    artist = fields.ForeignKey(ArtistResource, 'artist', full=True)
    art = fields.ForeignKey(ArtResource, 'art', full=True)
    user = fields.ForeignKey(UserResource, 'submitedByUser', full=True)
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'song'
        excludes = ['id']
        authentication = BitAuthAuthentication()
        