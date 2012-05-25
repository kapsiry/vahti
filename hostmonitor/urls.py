from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.db.models import Q

from hostmonitor.models import Host

unnamed_down = Q(up=False, name=None)

urlpatterns = patterns('',
    (r'^$', ListView.as_view(
        model=Host,
        queryset=Host.objects.order_by('-up').filter(~unnamed_down),
    )),
)
