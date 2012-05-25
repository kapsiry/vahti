# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.db.models import Q

from hostmonitor.models import Host, Network


class HostListView(ListView):
    model = Host

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.network = get_object_or_404(Network, slug=slug)
        no_unnamed_down = ~Q(up=False, name=None)
        qs = Host.objects.order_by('-up')
        qs = qs.filter(no_unnamed_down, network=self.network)
        return qs
