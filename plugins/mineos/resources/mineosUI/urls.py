from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/mineos/(?P<plugin_id>\d+)/', include('mineosUI.freenas.urls')),
)
