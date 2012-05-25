from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=30, editable=False, null=True)
    ip = models.GenericIPAddressField(unpack_ipv4=True, unique=True)
    last_up = models.DateTimeField(null=True, editable=False)
    up_since = models.DateTimeField(null=True, editable=False)
    up = models.NullBooleanField(default=None)
    monitor = models.BooleanField(default=True)
    network = models.ForeignKey('Network')

    def __unicode__(self):
        if self.name:
            name = self.name
        else:
            name = "unknown"
        return "%s (%s)" % (self.ip, name)


class Network(models.Model):
    name = models.CharField(max_length=30, editable=True, unique=True)

    def __unicode__(self):
        return "%s" % (self.name)

