from django.db import models

class Host(models.Model):
    ip = models.GenericIPAddressField(unpack_ipv4=True, primary_key=True)
    name = models.CharField(max_length=30, editable=False, null=True)
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

    def save(self, *args, **kwargs):
        try:
            old = Host.objects.get(pk=self.pk)
        except Host.DoesNotExist:
            old = None
        super(Host, self).save(*args, **kwargs)
        if not old or old.up != self.up:
            Event.objects.create(host=self, up=self.up)

class Network(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=30, editable=True, unique=True)

    def __unicode__(self):
        return "%s" % (self.name)

class Event(models.Model):
    host = models.ForeignKey('Host', editable=False)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    up = models.NullBooleanField(default=None)

    def __unicode__(self):
        return u"%s %s -> %s" % (self.time, self.host.ip, self.up)
