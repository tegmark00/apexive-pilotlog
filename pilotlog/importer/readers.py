import json

from importer.readers import Reader


class BytesReader(Reader):

    def __init__(self, bytes: bytes):
        self.bytes = bytes

    def read(self):
        return json.loads(self.bytes.decode("utf-8").replace("\\\"", "\""))
