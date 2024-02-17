from typing import Any

from django.db.models import F, Value, CharField

from pilotlog.models import Aircraft, Flight


empty_string = Value("", output_field=CharField())

aircraft_mapping = {
    "AircraftID": F("aircraft_code"),
    "EquipmentType": F("model"),
    "TypeCode": F("device_code"),
    "Year": empty_string,
    "Make": F("make"),
    "Model": empty_string,
    "Category": empty_string,
    "Class": F("aircraft_class"),
    "GearType": empty_string,
    "EngineType": empty_string,
    "Complex": F("complex"),
    "HighPerformance": F("high_perf"),
    "Pressurized": empty_string,
    "TAA": empty_string,
}

flight_mapping = {
    "Date": F("date_base"),
    "AircraftID": F("aircraft"),
}


class QsForExport:

    def __init__(self, qs, annotations):
        self.qs = qs
        self.annotations = annotations

    def get(self) -> list[dict[str, Any]]:
        return self.qs.annotate(
            **self.annotations
        ).values(
            *self.annotations.keys()
        ).iterator(
            chunk_size=1000
        )


def get_aircraft_export_qd() -> list[dict[str, Any]]:
    return QsForExport(
        qs=Aircraft.objects.all(),
        annotations=aircraft_mapping
    ).get()


def get_flight_export_qd() -> list[dict[str, Any]]:
    return QsForExport(
        qs=Flight.objects.all(),
        annotations=flight_mapping
    ).get()
