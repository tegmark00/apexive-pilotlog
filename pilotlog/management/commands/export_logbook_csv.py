import datetime

from django.core.management import BaseCommand
from exporter.writer import FileWriter, CSVWriteStrategy
from pilotlog.extns.exporter.logbook import DjangoLogbook


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
            data=DjangoLogbook().get().render()
        )
