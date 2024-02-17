from django.core.management import BaseCommand
from pilotlog.serives.assosiations import associate_flights_and_airfields


class Command(BaseCommand):

    def handle(self, *args, **options):
        associate_flights_and_airfields()
