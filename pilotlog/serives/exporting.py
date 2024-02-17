from exporter.template import Template, build_logbook_template
from pilotlog.querysets.exporting import get_aircraft_export_qd, get_flight_export_qd


def get_logbook_template() -> Template:
    aircraft = "aircraft"
    flight = "flight"

    aircraft_items = get_aircraft_export_qd()
    flight_items = get_flight_export_qd()

    logbook = build_logbook_template(aircraft, flight)
    aircraft_table = logbook.get_table(aircraft)
    flight_table = logbook.get_table(flight)

    aircraft_table.set_data_items(aircraft_items)
    flight_table.set_data_items(flight_items)

    aircraft_table.set_empty_rows(1)

    return logbook
