import dataclasses
from typing import Iterable, Any

from exporter.types import (
    Type, text, yyyy, boolean, date, hhmm, decimal, number,
    packed_detail_approach, packed_detail_person, datetime_
)


@dataclasses.dataclass
class TableItem:
    name: str
    type: Type
    show_comment: bool = False


@dataclasses.dataclass
class Table:
    name: str
    meta_items: list[TableItem]
    data_items: Iterable[dict[str, Any]] = dataclasses.field(default_factory=list)
    empty_rows: int = 0

    def set_data_items(self, data_items: Iterable[dict[str, Any]]):
        self.data_items = data_items

    def set_empty_rows(self, count: int):
        self.empty_rows = count

    def render(self, max_columns: int) -> Iterable[list[Any]]:
        columns = len(self.meta_items)
        max_columns = max(columns, max_columns)

        row1 = [""] * max_columns
        row2 = [""] * max_columns
        row3 = [""] * max_columns

        row1[0] = self.name

        map_pos = {}

        for i, item in enumerate(self.meta_items):

            if item.show_comment:
                row1[i] = item.type.comment

            row2[i] = item.type.name
            row3[i] = item.name

            map_pos[item.name] = i

        yield row1
        yield row2
        yield row3

        for item in self.data_items:
            row = [""] * max_columns
            for key, value in item.items():
                i = map_pos[key]
                row[i] = value
            yield row

        if self.empty_rows:
            for _ in range(self.empty_rows):
                yield [""] * max_columns


def create_aircraft_table() -> Table:
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
        ]
    )


def create_flights_table() -> Table:
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
        ]
    )
