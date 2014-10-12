from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings
from api import ArtistResource, UserResource, ArtResource, SongResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ArtistResource())
v1_api.register(ArtResource())
v1_api.register(SongResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'creativePlaylist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^api/', include(v1_api.urls)),
	#url(r'^media/<imageFile>, )
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
