# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.db.models import Q

from hostmonitor.models import Host, Network


class HostListView(ListView):
    model = Host

    def get_context_data(self, **kwargs):
        context = super(HostListView, self).get_context_data(**kwargs)
        context.update({'network' : self.network})
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        self.network = get_object_or_404(Network, slug=slug)
        no_unnamed_down = ~Q(up=False, name=None)
        qs = Host.objects.order_by('-up')
        qs = qs.filter(no_unnamed_down, network=self.network)
        return qs

class HostDetailView(DetailView):
    model = Host

    def get_context_data(self, **kwargs):
        context = super(HostDetailView, self).get_context_data(**kwargs)
        host = context['object']
        context['event_list'] = host.event_set.all().order_by('-time')[:20]
        return context
