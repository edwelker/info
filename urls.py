from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web_resources.views.home', name='home'),
    url(r'^resources/all/$', 'web_resources.views.all', name='all'),
    url(r'^resources/(?P<id>.*)/$', 'web_resources.views.id', name='id'),
    # url(r'^info/', include('info.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
