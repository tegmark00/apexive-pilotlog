import json

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
        if item["table"] in ["airfield", "Airfield"]:
            print(item["meta"])

    # with open("test.json", "w") as file:
    #     json.dump([{"a": 1, "b": 2}, {"a": 3, "b": 4}], file)
