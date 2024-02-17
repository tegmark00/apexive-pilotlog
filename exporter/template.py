from typing import Any, Iterable

from exporter.tables import Table, create_aircraft_table, create_flights_table
from exporter.writer import ConsoleWriter


class Template:
    def __init__(self, name: str):
        self.name = name
        self.tables: dict[str, Table] = {}

    def add_table(self, alias: str, table: Table):
        if alias in self.tables:
            raise ValueError(f"Table with alias '{alias}' already exists.")
        self.tables[alias] = table

    def get_table(self, alias: str) -> Table:
        return self.tables[alias]

    def render(self) -> Iterable[list[Any]]:
        max_columns = max(len(table.meta_items) for table in self.tables.values())
        yield [self.name] + [""] * (max_columns - 1)
        yield [""] * max_columns
        for table in self.tables.values():
            yield from table.render(max_columns)


def build_logbook_template(
        aircraft_alias: str = "aircraft",
        flights_alias: str = "flights",
):
    template = Template(
        name="ForeFlight Logbook Import",
    )

    template.add_table(
        alias=aircraft_alias,
        table=create_aircraft_table()
    )

    template.add_table(
        alias=flights_alias,
        table=create_flights_table()
    )

    return template


if __name__ == "__main__":
    ConsoleWriter().write(build_logbook_template().render())
