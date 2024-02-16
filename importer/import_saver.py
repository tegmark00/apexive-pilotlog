from abc import ABC, abstractmethod
from typing import Iterator

from importer.models import LogEntryDTO


class ImportSaver(ABC):
    @abstractmethod
    def save(self, items: Iterator[LogEntryDTO]):
        pass
