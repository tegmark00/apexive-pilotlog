import json

from importer.readers import Reader, FileReadStrategy, JsonFileReadStrategy


class BytesReader(Reader):

    def __init__(self, bytes: bytes, read_strategy: FileReadStrategy):
        self.bytes = bytes
        self.read_strategy = read_strategy

    def read(self):
        return self.read_strategy.formatted_data(self.bytes.decode("utf-8"))
