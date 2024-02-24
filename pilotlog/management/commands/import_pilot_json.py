from importer.utils import do_import
from importer.converters import LogEntryConverter
from importer.readers import LocalFileReader, JsonFileReadStrategy

from django.core.management import BaseCommand, CommandParser
from pilotlog.importer import DjangoSaver


class Command(BaseCommand):
    help = "Imports pilot log data"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        if "file" in options:
            do_import(
                reader=LocalFileReader(
                    file_path=options["file"], read_strategy=JsonFileReadStrategy()
                ),
                converter=LogEntryConverter(),
                saver=DjangoSaver(),
            )
