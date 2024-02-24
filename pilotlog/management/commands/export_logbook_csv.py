import datetime

from django.core.management import BaseCommand
from exporter.writer import FileWriter, CSVWriteStrategy, ConsoleWriter
from pilotlog.exporter import Logbook
from pilotlog.models import Aircraft, Flight


class Command(BaseCommand):
    help = "Export aircraft data to csv file."

    def handle(self, *args, **options):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        FileWriter(
            file_path=f"{time} output.csv", write_strategy=CSVWriteStrategy()
        ).write(
            Logbook(aircraft_qs=Aircraft.objects.all(), flight_qs=Flight.objects.all())
            .get()
            .render()
        )

        ConsoleWriter().write(
            Logbook(aircraft_qs=Aircraft.objects.all(), flight_qs=Flight.objects.all())
            .get()
            .render()
        )
