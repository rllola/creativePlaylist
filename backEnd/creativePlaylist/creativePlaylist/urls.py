from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import ArtistResource, UserResource

artist_resource = ArtistResource()
user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'creativePlaylist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^api/', include(artist_resource.urls)),
	url(r'^api/', include(user_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)