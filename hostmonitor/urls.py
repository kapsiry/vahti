from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from hostmonitor.models import Host, Network
from hostmonitor.views import HostDetailView, HostListView


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Network), name='network-list'),
    url(r'^network/(?P<slug>[^/]*)$', HostListView.as_view(),
        name='host-list'),
    url(r'^host/(?P<pk>[^/]*)$', HostDetailView.as_view(), name='host-detail'),
)
