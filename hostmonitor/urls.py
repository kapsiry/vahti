from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from hostmonitor.models import Host

urlpatterns = patterns('',
    (r'^$', ListView.as_view(
        model=Host,
        queryset=Host.objects.order_by('-up'),
    )),
)
