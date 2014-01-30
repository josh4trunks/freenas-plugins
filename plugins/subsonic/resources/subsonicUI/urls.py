from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/subsonic/(?P<plugin_id>\d+)/', include('subsonicUI.freenas.urls')),
)
