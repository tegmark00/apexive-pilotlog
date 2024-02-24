from django.core.management import BaseCommand

from pilotlog.models import Flight


class Command(BaseCommand):
    def handle(self, *args, **options):
        Flight.objects.sync_with_airfields()
