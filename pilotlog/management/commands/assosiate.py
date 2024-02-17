from django.core.management import BaseCommand

from pilotlog.importer.saver import DjangoSaver


class Command(BaseCommand):

    def handle(self, *args, **options):
        DjangoSaver().associate_flights_and_airfields()
