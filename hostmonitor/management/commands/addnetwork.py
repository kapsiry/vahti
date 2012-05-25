import socket

from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from iptools import validate_ip, validate_cidr, IpRange

from hostmonitor.models import Network


def resolve_dns(name):
    return set([x[4][0] for x in socket.getaddrinfo(name, 80)])


class Command(BaseCommand):
    args = '<target>'
    help = 'Add the specified hosts or CIDR networks (not network/broadcast)'

    def handle(self, *args, **options):
        if len(args) == 1:
            name = args[0]
            n = Network(name=name)
            n.save()

