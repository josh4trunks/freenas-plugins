from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/mediabrowser/(?P<plugin_id>\d+)/', include('mediabrowserUI.freenas.urls')),
)
