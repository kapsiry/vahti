from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'vahti/', include('hostmonitor.urls')),
    (r'^vahti/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^vahti/admin/', include(admin.site.urls)),
)
