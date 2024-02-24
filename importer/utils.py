from typing import Iterable, Any, Generator

from importer.converters import Converter
from importer.saver import Saver
from importer.models import LogEntryDTO
from importer.readers import Reader


def converted_items(
    items: Iterable[Any], converter: Converter
) -> Generator[LogEntryDTO, None, None]:
    for item_ in items:
        yield converter.convert(item_)


def do_import(reader: Reader, converter: Converter, saver: Saver):
    saver.save(items=converted_items(items=reader.read(), converter=converter))
