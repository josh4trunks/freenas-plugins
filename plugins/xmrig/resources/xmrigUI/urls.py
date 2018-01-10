from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/xmrig/(?P<plugin_id>\d+)/', include('xmrigUI.freenas.urls')),
)
