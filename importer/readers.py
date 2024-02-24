import json
from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class FileReadStrategy(ABC):
    @abstractmethod
    def formatted_data(self, data):
        pass


class JsonFileReadStrategy(FileReadStrategy):
    def formatted_data(self, data):
        return json.loads(data.replace('\\"', '"'))


class LocalFileReader(Reader):
    def __init__(self, file_path: str, read_strategy: FileReadStrategy):
        self.file_path = file_path
        self.read_strategy = read_strategy

    def read(self):
        with open(self.file_path) as f:
            return self.read_strategy.formatted_data(f.read())


class StringReader(Reader):
    def __init__(self, data: str, read_strategy: FileReadStrategy):
        self.data = data
        self.read_strategy = read_strategy

    def read(self):
        return self.read_strategy.formatted_data(self.data)
