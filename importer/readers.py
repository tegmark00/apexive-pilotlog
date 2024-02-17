import json
from abc import ABC, abstractmethod


class Reader(ABC):

    @abstractmethod
    def read(self):
        pass


class FileReadStrategy(ABC):

    @abstractmethod
    def read(self, file):
        pass


class FileReader(Reader):

    def __init__(self, file_path: str, read_strategy: FileReadStrategy):
        self.file_path = file_path
        self.read_strategy = read_strategy

    def read(self):
        with open(self.file_path) as f:
            return self.read_strategy.read(f)


class JsonFileReadStrategy(FileReadStrategy):

    def read(self, f):
        file_data = f.read()
        file_data = file_data.replace("\\\"", "\"")
        data = json.loads(file_data)
        return data
