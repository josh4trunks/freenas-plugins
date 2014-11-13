from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/maraschino/(?P<plugin_id>\d+)/', include('maraschinoUI.freenas.urls')),
)
