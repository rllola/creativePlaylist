from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings
from api import ArtistResource, UserResource, ArtResource, SongResource, LoginUserResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ArtistResource())
v1_api.register(ArtResource())
v1_api.register(SongResource())
v1_api.register(LoginUserResource())




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'creativePlaylist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^api/', include(v1_api.urls)),
	#url(r'^media/<imageFile>, )
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
