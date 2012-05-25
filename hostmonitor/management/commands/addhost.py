import socket
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from iptools import validate_ip, validate_cidr, IpRange

from hostmonitor.models import Host, Network


def resolve_dns(name):
    return set([x[4][0] for x in socket.getaddrinfo(name, 80)])


class Command(BaseCommand):
    args = '<target target ...>'
    help = 'Add the specified hosts or CIDR networks (not network/broadcast)'
    option_list = BaseCommand.option_list + (
        make_option('-n', '--network', dest="network"),
        )

    def add_host(self, ip, network):
        h = Host(ip=ip, network=network)
        self.stdout.write("%s adding\n" % ip)
        try:
            h.save()
        except IntegrityError, e:
            self.stderr.write("%s ERROR %s\n" % (ip, e))

    def handle(self, *args, **options):
        try:
            net = Network.objects.get(name=options['network'])
        except Network.DoesNotExist, e:
            self.stderr.write("ERROR %s\n" % e)
            return
        for target in args:
            if validate_ip(target):
                self.add_host(target, net)
            elif validate_cidr(target):
                hosts = list(IpRange(target))
                print hosts
                for host in hosts[1:-1]:
                    self.add_host(host, net)
            else:
                hosts = resolve_dns(target)
                for host in hosts:
                    self.add_host(host, net)

