from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/gamez/(?P<plugin_id>\d+)/', include('gamezUI.freenas.urls')),
)
