from importer.readers import JsonFileReadStrategy, FileReader


def get_reader(file_path):
    return FileReader(
        file_path=file_path,
        read_strategy=JsonFileReadStrategy()
    )


if __name__ == "__main__":
    PATH = "import - pilotlog_mcc.json"
    reader = get_reader(PATH)

    for item in reader.read():
        print(item)
