from unittest import mock

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from rest_framework.test import APITestCase

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from importer.converters import LogEntryConverter
from importer.readers import StringReader
from pilotlog.logbook_exporter import DjangoSaver


class ImportTestCase(APITestCase):
    do_import = "pilotlog.extns.importer.mixs.do_import"

    def setUp(self):
        super().setUp()
        self.url = reverse("import")
        self.file = staticfiles_storage.open("samples.json")

    def tearDown(self):
        super().tearDown()
        self.file.close()

    def test(self):
        user_model = get_user_model()
        user_model.objects.create_user("test", "test", "test")
        self.assertEqual(user_model.objects.count(), 1)

    def test_do_import_called(self):
        with mock.patch(self.do_import) as mocked_do_import:
            response = self.client.post(
                self.url,
                data={"file": self.file},
            )

            mocked_do_import.assert_called_once_with(
                reader=mock.ANY,
                converter=mock.ANY,
                saver=mock.ANY,
            )

            params = mocked_do_import.call_args[1]

            self.assertTrue(isinstance(params["reader"], StringReader))
            self.assertTrue(isinstance(params["converter"], LogEntryConverter))
            self.assertTrue(isinstance(params["saver"], DjangoSaver))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {"status": "ok"})

    def test_import_exception(self):
        with mock.patch(
            self.do_import, side_effect=Exception("test")
        ) as mocked_do_import:
            with mock.patch("logging.error") as mocked_logger:
                response = self.client.post(
                    self.url,
                    data={"file": self.file},
                )
                mocked_logger.assert_called_once()
            mocked_do_import.assert_called_once()

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data, {"file": "Could not import provided file"})

    def test_extension_validation(self):
        response = self.client.post(
            self.url, data={"file": ContentFile(b'{"test": "test"}', name="test.txt")}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            {"file": ["File extension not allowed. Allowed extensions are ['json']"]},
        )
