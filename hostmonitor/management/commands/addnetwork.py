import socket
from iptools import validate_ip, validate_cidr, IpRange

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify

from hostmonitor.models import Network


def resolve_dns(name):
    return set([x[4][0] for x in socket.getaddrinfo(name, 80)])


class Command(BaseCommand):
    args = '<network>'
    help = 'Add the specified hosts or CIDR networks (not network/broadcast)'

    def handle(self, *args, **options):
        if len(args) == 1:
            name = args[0]
            slug = slugify(name)
            n = Network(name=name, slug=slug)
            n.save()
        else:
            self.stderr.write("Invalid usage, try --help\n")

