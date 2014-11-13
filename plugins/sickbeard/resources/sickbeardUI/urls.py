from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/sickbeard/(?P<plugin_id>\d+)/', include('sickbeardUI.freenas.urls')),
)
