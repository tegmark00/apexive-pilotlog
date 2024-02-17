from rest_framework import serializers
from importer.converters.from_dict import LogEntryConverter
from importer.readers import JsonFileReadStrategy, StringReader
from importer.utils import do_import
from pilotlog.importer.saver import DjangoSaver


class ImportSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)
    status = serializers.CharField(read_only=True, default="ok")

    def save(self, **kwargs):
        do_import(
            reader=StringReader(
                data=self.validated_data.get("file").read().decode("utf-8"),
                read_strategy=JsonFileReadStrategy()
            ),
            converter=LogEntryConverter(),
            saver=DjangoSaver(),
        )
