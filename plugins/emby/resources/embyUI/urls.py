from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/emby/(?P<plugin_id>\d+)/', include('embyUI.freenas.urls')),
)
