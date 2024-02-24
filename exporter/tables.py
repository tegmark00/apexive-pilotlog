import dataclasses
from typing import Iterable, Any

from exporter.types import Type


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

        for i, table_item in enumerate(self.meta_items):
            if table_item.show_comment:
                row1[i] = table_item.type.comment

            row2[i] = table_item.type.name
            row3[i] = table_item.name

            map_pos[table_item.name] = i

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
