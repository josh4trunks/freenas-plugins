from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/madsonic/(?P<plugin_id>\d+)/', include('madsonicUI.freenas.urls')),
)
