from django.contrib import admin
from hostmonitor.models import Host, Network

class NetworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Host)
admin.site.register(Network, NetworkAdmin)
