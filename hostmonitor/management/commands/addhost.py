import socket

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from iptools import validate_ip, validate_cidr, IpRange

from hostmonitor.models import Host


def resolve_dns(name):
    return set([x[4][0] for x in socket.getaddrinfo(name, 80)])


class Command(BaseCommand):
    args = '<target target ...>'
    help = 'Add the specified hosts or CIDR networks (not network/broadcast)'

    def add_host(self, ip):
        h = Host(ip=ip)
        self.stdout.write("%s adding\n" % ip)
        try:
            h.save()
        except IntegrityError, e:
            self.stderr.write("%s ERROR, already exists, ignoring\n" % ip)

    def handle(self, *args, **options):
        for target in args:
            if validate_ip(target):
                self.add_host(target)
            elif validate_cidr(target):
                hosts = list(IpRange(target))
                print hosts
                for host in hosts[1:-1]:
                    self.add_host(host)
            else:
                hosts = resolve_dns(target)
                for host in hosts:
                    self.add_host(host)
                #self.stderr.write("Invalid host: %s\n" % target)
            # try:
            #     poll = Poll.objects.get(pk=int(poll_id))
            # except Poll.DoesNotExist:
            #     raise CommandError('Poll "%s" does not exist' % poll_id)
            # 
            # poll.opened = False
            # poll.save()
            # 
            # self.stdout.write('Successfully closed poll "%s"\n' % poll_id)

