from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/nextcloud/(?P<plugin_id>\d+)/', include('nextcloudUI.freenas.urls')),
)
