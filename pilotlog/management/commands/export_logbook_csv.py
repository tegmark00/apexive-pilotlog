import datetime

from django.core.management import BaseCommand
from exporter.writer import FileWriter, CSVWriteStrategy, ConsoleWriter
from pilotlog.serives.exporting import get_logbook


class Command(BaseCommand):
    help = "Export aircraft data to csv file."

    def handle(self, *args, **options):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ConsoleWriter().write(
        #     get_logbook().render()
        # )

        FileWriter(
            file_path=f"{time} output.csv",
            write_strategy=CSVWriteStrategy()
        ).write(
            data=get_logbook().render()
        )
