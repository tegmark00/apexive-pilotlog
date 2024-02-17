from typing import Any

from django.db.models import F, Value, CharField
from django.db.models.functions import Coalesce, Concat, ExtractHour, ExtractMinute, Cast, LPad

from pilotlog.models import Aircraft, Flight


empty_string = Value("", output_field=CharField())

aircraft_mapping = {
    "AircraftID": F("code"),
    "EquipmentType": F("model"),
    "TypeCode": F("device_code"),
    "Year": empty_string,
    "Make": F("make"),
    "Model": empty_string,
    "Category": empty_string,
    "Class": F("aircraft_class"),
    "GearType": empty_string,
    "EngineType": Coalesce(F("eng_type"), empty_string, output_field=CharField()),
    "Complex": F("complex"),
    "HighPerformance": F("high_perf"),
    "Pressurized": empty_string,
    "TAA": empty_string,
}


def get_person(person: str):
    return Concat(
        F(f"{person}__pilot_name"),
        Value(";"),
        # role
        Value(";"),
        F(f"{person}__pilot_email"),
    )


def get_time(time: str):
    return Concat(
        LPad(Cast(ExtractHour(F(time)), output_field=CharField()), 2, Value("0")),
        LPad(Cast(ExtractMinute(F(time)), output_field=CharField()), 2, Value("0")),
    )


flight_mapping = {
    "AircraftID": F("aircraft"),
    "Date": F("date_utc"),

    # "TimeOut": F("dep_time_utc"),
    "TimeOut": get_time("dep_time_utc"),
    # "TimeIn": F("arr_time_utc"),
    "TimeIn": get_time("arr_time_utc"),

    "Route": F("route"),
    "TotalTime": F("min_total"),
    "Holds": F("holding"),

    # not sure if it is correct

    "Person1": get_person("p1"),
    "Person2": get_person("p2"),
    "Person3": get_person("p3"),
    "Person4": get_person("p4"),

    # not sure if it is correct
    "Approach1": Concat(
        # type
        Value(";"),
        F("dep_rwy"),  # runway
        Value(";"),
        F("dep__af_name"),  # airport
        Value(";"),
        F("remarks"),  # comments
    ),

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
        qs=Flight.objects.all().select_related(
            "p1_flights", "p2_flights", "p3_flights", "p4_flights",
            "arr_flights", "dep_flights"
        ),
        annotations=flight_mapping
    ).get()
