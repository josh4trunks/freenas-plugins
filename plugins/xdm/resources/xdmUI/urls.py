from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/xdm/(?P<plugin_id>\d+)/', include('xdmUI.freenas.urls')),
)
