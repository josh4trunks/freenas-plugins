from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/syncthing/(?P<plugin_id>\d+)/', include('syncthingUI.freenas.urls')),
)
