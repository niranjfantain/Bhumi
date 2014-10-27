from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^apps/', include(admin.site.urls)),
                       url(r'^chaining/', include('smart_selects.urls')),
                       )
admin.site.site_header = 'Bhumi'
admin.site.site_title = 'Apps'
admin.site.index_title = 'Bhumi'
