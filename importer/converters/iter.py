from typing import Iterable, Any, Iterator

from importer.converters.base import Converter
from importer.models import LogEntryDTO


def converted_items(items: Iterable[Any], converter: Converter) -> Iterator[LogEntryDTO]:
    for item_ in items:
        yield converter.convert(item_)
