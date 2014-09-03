from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/pydio/(?P<plugin_id>\d+)/', include('pydioUI.freenas.urls')),
)
