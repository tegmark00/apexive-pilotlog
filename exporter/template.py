from typing import Any, Iterable
from exporter.tables import Table


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
        if self.tables:
            max_columns = max(len(table.meta_items) for table in self.tables.values())
        else:
            max_columns = 1  # for the name of the template

        yield [self.name] + [""] * (max_columns - 1)
        yield [""] * max_columns

        for table in self.tables.values():
            yield from table.render(max_columns)
