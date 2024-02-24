import unittest

from exporter.template import Template
from exporter.tables import Table, TableItem
from exporter.types import text, number


class TestTemplate(unittest.TestCase):
    def test_template(self):
        template = Template(name="ForeFlight Logbook Import")

        aircraft = TableItem("AircraftID", text)
        eq_type = TableItem("EquipmentType", number)

        aircraft_table = Table(name="Aircraft Table", meta_items=[aircraft, eq_type])

        aircraft_table.set_data_items(
            [
                {"AircraftID": "1", "EquipmentType": "2"},
                {
                    "AircraftID": "3",
                },
            ]
        )

        aircraft_table.set_empty_rows(1)

        template.add_table("aircraft", aircraft_table)

        flight = TableItem("FlightID", text)
        date = TableItem("Date", text)
        time_out = TableItem("TimeOut", text)

        flights_table = Table(name="Flights Table", meta_items=[flight, date, time_out])

        flights_table.set_data_items(
            (
                [
                    {"FlightID": "1", "Date": "2"},
                    {"FlightID": "5", "Date": "6"},
                ]
            )
        )

        template.add_table("flights", flights_table)

        self.assertListEqual(
            list(row for row in template.render()),
            [
                ["ForeFlight Logbook Import", "", ""],
                ["", "", ""],
                ["Aircraft Table", "", ""],
                ["Text", "Number", ""],
                ["AircraftID", "EquipmentType", ""],
                ["1", "2", ""],
                ["3", "", ""],
                ["", "", ""],
                ["Flights Table", "", ""],
                ["Text", "Text", "Text"],
                ["FlightID", "Date", "TimeOut"],
                ["1", "2", ""],
                ["5", "6", ""],
            ],
        )
