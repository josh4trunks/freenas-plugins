from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/btsync/(?P<plugin_id>\d+)/', include('btsyncUI.freenas.urls')),
)
