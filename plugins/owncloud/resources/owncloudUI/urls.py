from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/owncloud/(?P<plugin_id>\d+)/', include('owncloudUI.freenas.urls')),
)
