from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/lazylibrarian/(?P<plugin_id>\d+)/', include('lazylibrarianUI.freenas.urls')),
)
