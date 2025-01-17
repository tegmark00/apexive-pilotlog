from abc import ABC, abstractmethod
from typing import Iterator

from importer.models import LogEntryDTO


class Saver(ABC):
    @abstractmethod
    def save(self, items: Iterator[LogEntryDTO]):
        pass
