from unittest import mock

import freezegun
from django.test import TestCase
from django.urls import reverse

from exporter.template import Template
from pilotlog.exporter import Logbook


class ExportViewTestCase(TestCase):
    @freezegun.freeze_time("2022-02-24 00:00:00")
    def test_exported_file(self):
        url = reverse("export_logbook_csv")

        with mock.patch.object(Logbook, "get", return_value=Template("Mock")):
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertEqual(
            response["Content-Disposition"],
            'attachment; filename="2022-02-24 00:00:00 output.csv"',
        )
        self.assertEqual(response.getvalue(), b'Mock\r\n""\r\n')
