from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/sonarr/(?P<plugin_id>\d+)/', include('sonarrUI.freenas.urls')),
)
