from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.db.models import Q

from hostmonitor.models import Host, Network

unnamed_down = Q(up=False, name=None)

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        model=Network,
    ), name='network-list'),
    url(r'^network/(?P<slug>[^/]*)$', ListView.as_view(
        model=Host,
        queryset=Host.objects.order_by('-up').filter(~unnamed_down),
    ), name='host-list'),
)
