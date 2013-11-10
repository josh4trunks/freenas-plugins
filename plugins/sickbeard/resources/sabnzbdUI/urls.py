from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/sabnzbd/(?P<plugin_id>\d+)/', include('sabnzbdUI.freenas.urls')),
)
