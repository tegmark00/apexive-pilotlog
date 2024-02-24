from exporter.tables import Table, TableItem
from exporter.template import Template
from exporter.types import (
    text,
    yyyy,
    boolean,
    date,
    hhmm,
    decimal,
    number,
    packed_detail_approach,
    packed_detail_person,
    datetime_,
)


class LogbookBuilder:
    """
    LogbookBuilder class to build a logbook template for provided CSV template.
    Adding aircraft and flight tables information to the template.

    Usage:
    ```
    builder = LogbookBuilder()
    builder.add_aircraft_items(aircraft_items)
    builder.add_flight_items(flight_items)
    template = builder.get_logbook_template()
    rows = template.render()
    ```
    """

    aircraft_alias = "aircraft"
    flight_alias = "flights"

    def __init__(self):
        # Name is a part of the CSV template, so we hold it hardcoded
        self.template = Template(name="ForeFlight Logbook Import")

        self.aircraft_table = self.create_aircraft_table()
        self.flights_table = self.create_flights_table()

        self.template.add_table(self.aircraft_alias, self.aircraft_table)
        self.template.add_table(self.flight_alias, self.flights_table)

    def get_logbook_template(self) -> Template:
        return self.template

    def get_aircraft_table(self):
        return self.aircraft_table

    def get_flights_table(self):
        return self.flights_table

    def add_flight_items(self, items):
        self.flights_table.set_data_items(items)

    def add_aircraft_items(self, items):
        self.aircraft_table.set_data_items(items)

    @staticmethod
    def create_aircraft_table():
        return Table(
            name="Aircraft Table",
            meta_items=[
                TableItem("AircraftID", text),
                TableItem("EquipmentType", text),
                TableItem("TypeCode", text),
                TableItem("Year", yyyy),
                TableItem("Make", text),
                TableItem("Model", text),
                TableItem("Category", text),
                TableItem("Class", text),
                TableItem("GearType", text),
                TableItem("EngineType", text),
                TableItem("Complex", boolean),
                TableItem("HighPerformance", boolean),
                TableItem("Pressurized", boolean),
                TableItem("TAA", boolean),
            ],
        )

    @staticmethod
    def create_flights_table():
        return Table(
            name="Flights Table",
            meta_items=[
                TableItem("Date", date),
                TableItem("AircraftID", text),
                TableItem("From", text),
                TableItem("To", text),
                TableItem("Route", text),
                TableItem("TimeOut", hhmm),
                TableItem("TimeOff", hhmm),
                TableItem("TimeOn", hhmm),
                TableItem("TimeIn", hhmm),
                TableItem("OnDuty", hhmm),
                TableItem("OffDuty", hhmm),
                TableItem("TotalTime", decimal),
                TableItem("PIC", decimal),
                TableItem("SIC", decimal),
                TableItem("Night", decimal),
                TableItem("Solo", decimal),
                TableItem("CrossCountry", decimal),
                TableItem("NVG", decimal),
                TableItem("NVGOps", number),
                TableItem("Distance", decimal),
                TableItem("DayTakeoffs", number),
                TableItem("DayLandingsFullStop", number),
                TableItem("NightTakeoffs", number),
                TableItem("NightLandingsFullStop", number),
                TableItem("AllLandings", number),
                TableItem("ActualInstrument", decimal),
                TableItem("SimulatedInstrument", decimal),
                TableItem("HobbsStart", decimal),
                TableItem("HobbsEnd", decimal),
                TableItem("TachStart", decimal),
                TableItem("TachEnd", decimal),
                TableItem("Holds", number),
                TableItem("Approach1", packed_detail_approach, show_comment=True),
                TableItem("Approach2", packed_detail_approach),
                TableItem("Approach3", packed_detail_approach),
                TableItem("Approach4", packed_detail_approach),
                TableItem("Approach5", packed_detail_approach),
                TableItem("Approach6", packed_detail_approach),
                TableItem("DualGiven", decimal),
                TableItem("DualReceived", decimal),
                TableItem("SimulatedFlight", decimal),
                TableItem("GroundTraining", decimal),
                TableItem("InstructorName", text),
                TableItem("InstructorComments", text),
                TableItem("Person1", packed_detail_person, show_comment=True),
                TableItem("Person2", packed_detail_person),
                TableItem("Person3", packed_detail_person),
                TableItem("Person4", packed_detail_person),
                TableItem("Person5", packed_detail_person),
                TableItem("Person6", packed_detail_person),
                TableItem("FlightReview", boolean),
                TableItem("Checkride", boolean),
                TableItem("IPC", boolean),
                TableItem("NVGProficiency", boolean),
                TableItem("FAA6158", boolean),
                TableItem("[Text]CustomFieldName", text),
                TableItem("[Numeric]CustomFieldName", decimal),
                TableItem("[Hours]CustomFieldName", decimal),
                TableItem("[Counter]CustomFieldName", number),
                TableItem("[Date]CustomFieldName", date),
                TableItem("[DateTime]CustomFieldName", datetime_),
                TableItem("[Toggle]CustomFieldName", boolean),
                TableItem("PilotComments", text),
            ],
        )
