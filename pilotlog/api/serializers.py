import logging

from rest_framework import serializers
from pilotlog.api.validators import FileExtensionValidator
from pilotlog.extns.importer.mixs import WithImportUploadedFile


class ImportSerializer(WithImportUploadedFile, serializers.Serializer):
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
            self.import_file(self.validated_data["file"])
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError({"file": "Could not import provided file"})
