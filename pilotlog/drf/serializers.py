import logging
from typing import Any

from django.contrib.contenttypes.models import ContentType
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from pilotlog.drf.validators import FileExtensionValidator
from pilotlog.importer import WithImportPilotlogJsonString
from pilotlog.models import LogEntry, Aircraft, Flight, AirField


class ImportSerializer(WithImportPilotlogJsonString, serializers.Serializer):
    file = serializers.FileField(
        write_only=True,
        validators=[FileExtensionValidator(allowed_extensions=["json"])],
    )
    status = serializers.CharField(read_only=True, default="ok")

    def save(self, **kwargs):
        try:
            self.import_json_string_data(self.validated_data["file"].read().decode())
        except Exception as e:
            logging.error(e)
            raise serializers.ValidationError(
                {"file": "Could not import provided file"}
            )


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "model",
        )
        model = ContentType


class LogEntrySerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()

    class Meta:
        fields = "__all__"
        model = LogEntry


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Aircraft


class ShortAirfieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "code",
            "aficao",
            "af_name",
        )
        model = AirField


class DirectionSerializer(serializers.Serializer):
    from_airfield = ShortAirfieldSerializer(allow_null=True)
    to_airfield = ShortAirfieldSerializer(allow_null=True)


class FlightSerializer(serializers.ModelSerializer):
    direction = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Flight

    @extend_schema_field(DirectionSerializer)
    def get_direction(self, obj: Flight) -> dict[str, Any]:
        return DirectionSerializer(
            {
                "from_airfield": obj.arr,
                "to_airfield": obj.dep,
            }
        ).data
