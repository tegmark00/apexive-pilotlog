from importer.converters.iter import converted_items
from importer.converters.json import JsonLogEntryConverter
from importer.reader import FileReader, JsonFileReadStrategy

from django.core.management import BaseCommand, CommandParser
from pilotlog.serives.importing import DjangoImportSaver


class Command(BaseCommand):
    help = "Imports pilot log data"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):

        if "file" in options:

            reader = FileReader(
                file_path=options["file"],
                read_strategy=JsonFileReadStrategy()
            )

            DjangoImportSaver().save(
                items=converted_items(
                    items=reader.read(),
                    converter=JsonLogEntryConverter()
                )
            )
