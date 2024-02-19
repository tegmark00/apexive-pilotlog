from django.core.files.uploadedfile import UploadedFile

from importer.converters import LogEntryConverter
from importer.readers import StringReader, JsonFileReadStrategy
from importer.utils import do_import
from pilotlog.extns.importer.saver import DjangoSaver


class WithImportUploadedFile:

    @staticmethod
    def import_file(file: UploadedFile):
        do_import(
            reader=StringReader(data=file.read().decode("utf-8"), read_strategy=JsonFileReadStrategy()),
            converter=LogEntryConverter(),
            saver=DjangoSaver(),
        )
