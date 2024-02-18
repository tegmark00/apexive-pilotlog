from django.contrib.staticfiles.storage import staticfiles_storage
from django.test import TestCase

from importer.converters import LogEntryConverter
from importer.readers import StringReader, JsonFileReadStrategy
from importer.utils import do_import
from pilotlog.extns.importer.saver import DjangoSaver
from pilotlog import models


class TestImportWithSaver(TestCase):
    def test_import_with_saver(self):

        with staticfiles_storage.open('samples.json') as file:

            reader = StringReader(
                file.read().decode('utf-8'),
                read_strategy=JsonFileReadStrategy(),
            )

            do_import(reader, LogEntryConverter(), DjangoSaver())

        self.assertEqual(models.LogEntry.objects.count(), 27)
        self.assertEqual(models.Aircraft.objects.count(), 4)
        self.assertEqual(models.AirField.objects.count(), 3)
        self.assertEqual(models.Flight.objects.count(), 4)
        self.assertEqual(models.ImagePic.objects.count(), 2)
        self.assertEqual(models.LimitRules.objects.count(), 2)
        self.assertEqual(models.MyQuery.objects.count(), 2)
        self.assertEqual(models.MyQueryBuild.objects.count(), 2)
        self.assertEqual(models.Qualification.objects.count(), 2)
        self.assertEqual(models.Pilot.objects.count(), 4)
        self.assertEqual(models.SettingConfig.objects.count(), 2)
