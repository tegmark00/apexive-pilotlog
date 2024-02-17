import csv

from abc import ABC, abstractmethod
from typing import Iterator, Any


class Writer(ABC):
    @abstractmethod
    def write(self, data):
        pass


class WriteStrategy(ABC):
    @abstractmethod
    def written_lines(self, data) -> Iterator[Any]:
        pass


class Echo:
    def write(self, value):
        return value


class CSVWriteStrategy(WriteStrategy):

    def written_lines(self, data) -> Iterator[Any]:
        writer = csv.writer(Echo())
        for row in data:
            formatted_row = writer.writerow(row)
            yield formatted_row


class FileWriter(Writer):
    def __init__(self, file_path: str, write_strategy: WriteStrategy):
        self.file_path = file_path
        self.write_strategy = write_strategy

    def write(self, data):
        with open(self.file_path, "w") as f:
            for item in self.write_strategy.written_lines(data):
                f.write(item)


class ConsoleWriter(Writer):

    def write(self, data):
        for row in data:
            print(row)
