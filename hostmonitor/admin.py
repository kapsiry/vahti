from django.contrib import admin
from hostmonitor.models import Host, Network

class NetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class HostAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ip']

admin.site.register(Host, HostAdmin)
admin.site.register(Network, NetworkAdmin)
