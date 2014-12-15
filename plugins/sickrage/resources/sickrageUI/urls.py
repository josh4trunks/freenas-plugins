from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/sickrage/(?P<plugin_id>\d+)/', include('sickrageUI.freenas.urls')),
)
