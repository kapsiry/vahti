from django.contrib import admin
from hostmonitor.models import Host, Network

admin.site.register(Host)
admin.site.register(Network)
