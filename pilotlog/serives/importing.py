import dataclasses
import time
from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model as BaseDjangoModel
from django.db.transaction import atomic

from importer import models as dto
from importer.import_saver import ImportSaver

from pilotlog import models
from pilotlog.serives.assosiations import associate_flights_and_airfields


@dataclasses.dataclass(frozen=True)
class Map:
    model: type(BaseDjangoModel)
    content_type: ContentType = None
    items: list = dataclasses.field(default_factory=list)
    map_fields: dict[str, Any] = dataclasses.field(default_factory=dict)
    unique_fields: list[str] = dataclasses.field(default_factory=list)


class DjangoImportSaver(ImportSaver):

    @atomic
    def save(self, items):

        start = time.time()

        model_mapping = {
            dto.AirCraftDTO.__name__: Map(
                models.Aircraft,
                content_type=ContentType.objects.get_for_model(models.Aircraft),
                map_fields={"aircraft_code": "code"},
                unique_fields=['code'],
            ),
            dto.AirFieldDTO.__name__: Map(
                models.AirField,
                content_type=ContentType.objects.get_for_model(models.AirField),
                map_fields={"af_code": "code"},
                unique_fields=['code'],
            ),
            dto.PilotDTO.__name__: Map(
                models.Pilot,
                content_type=ContentType.objects.get_for_model(models.Pilot),
                map_fields={"pilot_code": "code"},
                unique_fields=['code'],
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
                unique_fields=['code'],
            ),
            dto.ImagePicDTO.__name__: Map(
                models.ImagePic,
                content_type=ContentType.objects.get_for_model(models.ImagePic),
                map_fields={"img_code": "code"},
                unique_fields=['code']
            ),
            dto.LimitRulesDTO.__name__: Map(
                models.LimitRules,
                content_type=ContentType.objects.get_for_model(models.LimitRules),
                map_fields={"limit_code": "code"},
                unique_fields=['code']
            ),
            dto.MyQueryDTO.__name__: Map(
                models.MyQuery,
                content_type=ContentType.objects.get_for_model(models.MyQuery),
                map_fields={"mq_code": "code"},
                unique_fields=['code'],
            ),
            dto.MyQueryBuildDTO.__name__: Map(
                models.MyQueryBuild,
                content_type=ContentType.objects.get_for_model(models.MyQueryBuild),
                map_fields={
                    "mqb_code": "code",
                    "mq_code": "mq_id"
                },
                unique_fields=['code'],
            ),
            dto.QualificationDTO.__name__: Map(
                models.Qualification,
                content_type=ContentType.objects.get_for_model(models.Qualification),
                map_fields={"q_code": "code"},
                unique_fields=['code'],
            ),
            dto.SettingConfigDTO.__name__: Map(
                models.SettingConfig,
                content_type=ContentType.objects.get_for_model(models.SettingConfig),
                map_fields={"config_code": "code"},
                unique_fields=['code'],
            ),
        }

        log_entries = []

        for item in items:

            if mapped := model_mapping.get(item.meta.__class__.__name__):
                model = mapped.model
                meta_data = item.meta.dict()
                for key, value in mapped.map_fields.items():
                    if key in meta_data:
                        meta_data[value] = meta_data.pop(key)
                mapped.items.append(model(**meta_data))
            else:
                raise ValueError(f"Unknown model {item.meta.__class__.__name__}")

            log_entry = models.LogEntry(**item.dict(exclude={'meta', 'table_name'}))
            log_entry.content_type = mapped.content_type

            log_entries.append(log_entry)

        for value in model_mapping.values():
            if len(value.items) > 0:
                value.model.objects.bulk_create(
                    value.items,
                    batch_size=1000,
                    unique_fields=value.unique_fields,
                    ignore_conflicts=True
                )

        # Should be imported after the models are created
        models.LogEntry.objects.bulk_create(
            log_entries,
            batch_size=1000,
            unique_fields=['guid', 'content_type'],
            ignore_conflicts=True
        )

        # Add existing airfields to flights
        associate_flights_and_airfields()

        end = time.time()

        print(f"Imported {len(log_entries)} log entries in {end - start} seconds")
