from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'solr_haystack_tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
