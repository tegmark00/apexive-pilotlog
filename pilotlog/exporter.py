from typing import Iterator, Any

from exporter.builder import LogbookBuilder
from exporter.template import Template
from pilotlog.models import ExportedFlightLogBookQuerySet


class Logbook:
    """
    Logbook class to export aircraft and flight data
    with Django ORM to a logbook template.

    Usage:
    ```
    logbook = Logbook(
        aircraft_qs=Aircraft.objects.all(),
        flight_qs=Flight.objects.all()
    )
    rows = logbook.get().render()
    ```

    """

    chunk_size: int = 1024

    def __init__(
        self,
        aircraft_qs: ExportedFlightLogBookQuerySet,
        flight_qs: ExportedFlightLogBookQuerySet,
    ):
        self.builder = LogbookBuilder()

        self.builder.add_aircraft_items(self.get_exported_iterator(aircraft_qs))

        self.builder.add_flight_items(self.get_exported_iterator(flight_qs))

        self.builder.get_aircraft_table().set_empty_rows(1)

    def get(self) -> Template:
        return self.builder.get_logbook_template()

    def get_exported_iterator(
        self, qs: ExportedFlightLogBookQuerySet
    ) -> Iterator[dict[str, Any]]:
        return qs.annotate_exported_fields().iterator(self.chunk_size)
