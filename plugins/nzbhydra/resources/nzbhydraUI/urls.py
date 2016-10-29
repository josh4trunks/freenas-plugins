from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/nzbhydra/(?P<plugin_id>\d+)/', include('nzbhydraUI.freenas.urls')),
)
