from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'crimes/$', 'crimes.views.index'),
	url(r'^polls/(?P<crime_id>\d+)/$', 'polls.views.detail'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'map/$', 'crimes.views.map'),
    # Examples:
    # url(r'^$', 'crime.views.home', name='home'),
    # url(r'^crime/', include('crime.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
