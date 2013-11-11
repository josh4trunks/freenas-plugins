from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/couchpotato/(?P<plugin_id>\d+)/', include('couchpotatoUI.freenas.urls')),
)
