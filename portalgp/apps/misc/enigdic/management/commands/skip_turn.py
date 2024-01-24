from django.core.management.base import BaseCommand
from ...views import cmd_skip_turn

class Command(BaseCommand):

    def handle(self, *args, **options):
        cmd_skip_turn()
        self.stdout.write(self.style.SUCCESS('siguiente día OK'))
