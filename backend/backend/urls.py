from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^backend/', include('backend.foo.urls')),
    url(r'^dj/', include('dj.urls')),
    url(r'^$', include('home.urls')),
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
)
