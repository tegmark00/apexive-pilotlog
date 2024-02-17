from django.db.models import Value, CharField, F
from django.db.models.functions import Coalesce, Concat, LPad, ExtractHour, Cast, ExtractMinute

from exporter.builder import LogbookBuilder
from pilotlog.models import Aircraft, Flight


class DjangoLogbook:
    empty_string = Value("", output_field=CharField())

    def __init__(self):
        self.builder = LogbookBuilder()
        self.builder.add_aircraft_items(self.get_aircraft_items())
        self.builder.add_flight_items(self.get_flight_items())
        self.builder.get_aircraft_table().set_empty_rows(1)

    def get(self):
        return self.builder.get_logbook_template()

    def get_aircraft_items(self):
        qs = Aircraft.objects.all()

        fields_map = {
            "AircraftID": F("code"),
            "EquipmentType": F("model"),
            "TypeCode": F("device_code"),
            "Year": self.empty_string,
            "Make": F("make"),
            "Model": self.empty_string,
            "Category": self.empty_string,
            "Class": F("aircraft_class"),
            "GearType": self.empty_string,
            "EngineType": Coalesce(F("eng_type"), self.empty_string, output_field=CharField()),
            "Complex": F("complex"),
            "HighPerformance": F("high_perf"),
            "Pressurized": self.empty_string,
            "TAA": self.empty_string,
        }

        return self.prepared_qs(qs, fields_map)

    def get_flight_items(self):
        qs = Flight.objects.all().select_related(
            "p1_flights", "p2_flights", "p3_flights", "p4_flights",
            "arr_flights", "dep_flights"
        )

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

        fields_map = {
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

        return self.prepared_qs(qs, fields_map)

    @staticmethod
    def prepared_qs(qs, annotations):
        return qs.annotate(
            **annotations
        ).values(
            *annotations.keys()
        ).iterator(
            chunk_size=1000
        )
