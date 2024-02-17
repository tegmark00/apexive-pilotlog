from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self, data):
        pass


class FileWriteStrategy(ABC):
    @abstractmethod
    def write(self, file, data):
        pass


class CSVWriteStrategy(FileWriteStrategy):

    def write(self, file, data):
        for row in data:
            file.write(",".join(str(x) for x in row) + "\n")


class FileWriter(Writer):
    def __init__(self, file_path: str, write_strategy: FileWriteStrategy):
        self.file_path = file_path
        self.write_strategy = write_strategy

    def write(self, data):
        with open(self.file_path, "w") as f:
            self.write_strategy.write(f, data)


class ConsoleWriter(Writer):

    def write(self, data):
        for row in data:
            print(row)
