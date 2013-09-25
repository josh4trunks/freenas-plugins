from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/crashplan/(?P<plugin_id>\d+)/', include('crashplanUI.freenas.urls')),
)
