from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/mylar/(?P<plugin_id>\d+)/', include('mylarUI.freenas.urls')),
)
