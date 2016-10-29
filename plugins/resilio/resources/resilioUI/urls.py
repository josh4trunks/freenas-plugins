from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/resilio/(?P<plugin_id>\d+)/', include('resilioUI.freenas.urls')),
)
