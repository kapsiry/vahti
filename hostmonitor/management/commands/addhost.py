from iptools import validate_ip, validate_cidr, IpRange
from django.core.management.base import BaseCommand, CommandError

from hostmonitor.models import Host

class Command(BaseCommand):
    args = '<target target ...>'
    help = 'Add the specified hosts or CIDR networks (not network/broadcast)'

    def add_host(self, ip):
        h = Host(ip=ip)
        self.stdout.write("Adding host %s\n" % ip)
        h.save()

    def handle(self, *args, **options):
        for target in args:
            if validate_ip(target):
                self.add_host(target)
            elif validate_cidr(target):
                hosts = list(IpRange(target))
                print hosts
                for i in hosts[1:-1]:
                    self.add_host(i)
            else:
                self.stderr.write("Invalid host: %s\n" % target)
            # try:
            #     poll = Poll.objects.get(pk=int(poll_id))
            # except Poll.DoesNotExist:
            #     raise CommandError('Poll "%s" does not exist' % poll_id)
            # 
            # poll.opened = False
            # poll.save()
            # 
            # self.stdout.write('Successfully closed poll "%s"\n' % poll_id)

