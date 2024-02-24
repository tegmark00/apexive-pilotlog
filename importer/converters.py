from abc import ABC, abstractmethod

from importer import models


class Converter(ABC):
    @abstractmethod
    def convert(self, data):
        pass


class LogEntryConverter(Converter):
    models_map = {
        "aircraft": models.AirCraftDTO,
        "airfield": models.AirFieldDTO,
        "flight": models.FlightDTO,
        "imagepic": models.ImagePicDTO,
        "limitrules": models.LimitRulesDTO,
        "myquery": models.MyQueryDTO,
        "myquerybuild": models.MyQueryBuildDTO,
        "pilot": models.PilotDTO,
        "qualification": models.QualificationDTO,
        "settingconfig": models.SettingConfigDTO,
    }

    def convert(self, data: dict) -> models.LogEntryDTO:
        table_name = data["table"].lower()
        model_class = self.models_map[table_name]
        data["meta"] = model_class(**data["meta"])
        return models.LogEntryDTO(**data)
