from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/htpc-manager/(?P<plugin_id>\d+)/', include('htpcmanagerUI.freenas.urls')),
)
