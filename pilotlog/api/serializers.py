import logging

from rest_framework import serializers
from importer.converters import LogEntryConverter
from importer.readers import JsonFileReadStrategy, StringReader
from importer.utils import do_import
from pilotlog.api.validators import FileExtensionValidator
from pilotlog.extns.importer.saver import DjangoSaver


class ImportSerializer(serializers.Serializer):
    file = serializers.FileField(
        write_only=True,
        validators=[FileExtensionValidator(allowed_extensions=["json"])],
    )
    status = serializers.CharField(
        read_only=True,
        default="ok"
    )

    def save(self, **kwargs):
        try:
            self.import_file(self.validated_data["file"].read().decode("utf-8"))
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError({"file": "Could not import provided file"})

    @staticmethod
    def import_file(file):
        do_import(
            reader=StringReader(data=file, read_strategy=JsonFileReadStrategy()),
            converter=LogEntryConverter(),
            saver=DjangoSaver(),
        )
