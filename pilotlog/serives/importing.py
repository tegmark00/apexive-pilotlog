import dataclasses
import time
from typing import Any

from django.contrib.contenttypes.models import ContentType
from django.db.models import Model as BaseDjangoModel
from django.db.transaction import atomic

from importer import models as dto
from importer.import_saver import ImportSaver

from pilotlog import models


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
                unique_fields=['aircraft_code'],
            ),
            dto.AirFieldDTO.__name__: Map(
                models.AirField,
                content_type=ContentType.objects.get_for_model(models.AirField),
                unique_fields=['af_code'],
            ),
            dto.FlightDTO.__name__: Map(
                models.Flight,
                content_type=ContentType.objects.get_for_model(models.Flight),
                map_fields={"aircraft_code": "aircraft_id"},
                unique_fields=['flight_code'],
            ),
            dto.ImagePicDTO.__name__: Map(
                models.ImagePic,
                content_type=ContentType.objects.get_for_model(models.ImagePic),
                unique_fields=['img_code']
            ),
            dto.LimitRulesDTO.__name__: Map(
                models.LimitRules,
                content_type=ContentType.objects.get_for_model(models.LimitRules),
                unique_fields=['limit_code']
            ),
            dto.MyQueryDTO.__name__: Map(
                models.MyQuery,
                content_type=ContentType.objects.get_for_model(models.MyQuery),
                unique_fields=['mq_code'],
            ),
            dto.MyQueryBuildDTO.__name__: Map(
                models.MyQueryBuild,
                content_type=ContentType.objects.get_for_model(models.MyQueryBuild),
                map_fields={"mq_code": "mq_id"},
                unique_fields=['mqb_code'],
            ),
            dto.PilotDTO.__name__: Map(
                models.Pilot,
                content_type=ContentType.objects.get_for_model(models.Pilot),
                unique_fields=['pilot_code'],
            ),
            dto.QualificationDTO.__name__: Map(
                models.Qualification,
                content_type=ContentType.objects.get_for_model(models.Qualification),
                unique_fields=['q_code'],
            ),
            dto.SettingConfigDTO.__name__: Map(
                models.SettingConfig,
                content_type=ContentType.objects.get_for_model(models.SettingConfig),
                unique_fields=['config_code'],
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

        end = time.time()

        print(f"Imported {len(log_entries)} log entries in {end - start} seconds")
