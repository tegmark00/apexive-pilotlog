import dataclasses
from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model as BaseDjangoModel
from django.db.transaction import atomic

from importer import models as dto
from importer.converters import LogEntryConverter
from importer.readers import StringReader, JsonFileReadStrategy
from importer.saver import Saver
from importer.utils import do_import
from pilotlog import models
from pilotlog.models import Flight


@dataclasses.dataclass(frozen=True)
class Map:
    model: type[BaseDjangoModel]
    content_type: ContentType = None
    items: list = dataclasses.field(default_factory=list)
    map_fields: dict[str, Any] = dataclasses.field(default_factory=dict)
    unique_fields: list[str] = dataclasses.field(default_factory=list)


class DjangoSaver(Saver):
    def __init__(self):
        self.model_mapping = {
            dto.AirCraftDTO.__name__: Map(
                models.Aircraft,
                content_type=ContentType.objects.get_for_model(models.Aircraft),
                map_fields={"aircraft_code": "code"},
                unique_fields=["code"],
            ),
            dto.AirFieldDTO.__name__: Map(
                models.AirField,
                content_type=ContentType.objects.get_for_model(models.AirField),
                map_fields={"af_code": "code"},
                unique_fields=["code"],
            ),
            dto.PilotDTO.__name__: Map(
                models.Pilot,
                content_type=ContentType.objects.get_for_model(models.Pilot),
                map_fields={"pilot_code": "code"},
                unique_fields=["code"],
            ),
            dto.FlightDTO.__name__: Map(
                models.Flight,
                content_type=ContentType.objects.get_for_model(models.Flight),
                map_fields={
                    "flight_code": "code",
                    "aircraft_code": "aircraft_id",
                    "p1_code": "p1_id",
                    "p2_code": "p2_id",
                    "p3_code": "p3_id",
                    "p4_code": "p4_id",
                },
                unique_fields=["code"],
            ),
            dto.ImagePicDTO.__name__: Map(
                models.ImagePic,
                content_type=ContentType.objects.get_for_model(models.ImagePic),
                map_fields={"img_code": "code"},
                unique_fields=["code"],
            ),
            dto.LimitRulesDTO.__name__: Map(
                models.LimitRules,
                content_type=ContentType.objects.get_for_model(models.LimitRules),
                map_fields={"limit_code": "code"},
                unique_fields=["code"],
            ),
            dto.MyQueryDTO.__name__: Map(
                models.MyQuery,
                content_type=ContentType.objects.get_for_model(models.MyQuery),
                map_fields={"mq_code": "code"},
                unique_fields=["code"],
            ),
            dto.MyQueryBuildDTO.__name__: Map(
                models.MyQueryBuild,
                content_type=ContentType.objects.get_for_model(models.MyQueryBuild),
                map_fields={"mqb_code": "code", "mq_code": "mq_id"},
                unique_fields=["code"],
            ),
            dto.QualificationDTO.__name__: Map(
                models.Qualification,
                content_type=ContentType.objects.get_for_model(models.Qualification),
                map_fields={"q_code": "code"},
                unique_fields=["code"],
            ),
            dto.SettingConfigDTO.__name__: Map(
                models.SettingConfig,
                content_type=ContentType.objects.get_for_model(models.SettingConfig),
                map_fields={"config_code": "code"},
                unique_fields=["code"],
            ),
        }

    @atomic
    def save(self, items):
        logentries = []

        for log in items:
            if mapped := self.model_mapping.get(log.meta.__class__.__name__):
                imported_model = mapped.model
                imported_model_data = log.meta.dict()

                # map fields from dto to model
                for key, value in mapped.map_fields.items():
                    if key in imported_model_data:
                        imported_model_data[value] = imported_model_data.pop(key)

                mapped.items.append(imported_model(**imported_model_data))

            else:
                raise ValueError(f"Unknown model {log.meta.__class__.__name__}")

            logentry = models.LogEntry(**log.dict(exclude={"meta", "table_name"}))
            logentry.content_type = mapped.content_type
            logentries.append(logentry)

        # Save all the models except LogEntry
        for value in self.model_mapping.values():
            if len(value.items) > 0:
                value.model.objects.bulk_create(
                    value.items,
                    batch_size=1000,
                    unique_fields=value.unique_fields,
                    ignore_conflicts=True,
                )

        # Save LogEntry models
        # Should be imported after all the other models has been created
        models.LogEntry.objects.bulk_create(
            logentries,
            batch_size=1000,
            unique_fields=["guid", "content_type"],
            ignore_conflicts=True,
        )

        # Update the flight model with the airfield and aircraft
        Flight.objects.sync_with_airfields()


class WithImportPilotlogJsonString:
    @staticmethod
    def import_json_string_data(data: str):
        do_import(
            reader=StringReader(data=data, read_strategy=JsonFileReadStrategy()),
            converter=LogEntryConverter(),
            saver=DjangoSaver(),
        )
