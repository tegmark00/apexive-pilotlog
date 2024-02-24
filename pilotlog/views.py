import datetime
import logging

from django.http import StreamingHttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from exporter.writer import CSVWriteStrategy, Writer, WriteStrategy

from pilotlog.forms import UploadJsonFileForm
from pilotlog.importer import WithImportPilotlogJsonString
from pilotlog.exporter import Logbook
from pilotlog.models import Aircraft, Flight


class IndexView(WithImportPilotlogJsonString, FormView):
    form_class = UploadJsonFileForm
    template_name = "pilotlog/index.html"

    def form_valid(self, form):
        for f in form.cleaned_data["file"]:
            try:
                self.import_json_string_data(f.decode())
            except Exception as e:
                logging.error(e)
                form.add_error("file", "Could not import provided file")
                return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("import_logbook_csv")


class LogbookStreamCSVWriter(Writer):
    def __init__(self, response: StreamingHttpResponse, write_strategy: WriteStrategy):
        self.response = response
        self.write_strategy = write_strategy

    def write(self, data):
        self.response.streaming_content = self.write_strategy.written_lines(data)


class CSVLogbookExportView(View):
    def get(self, request, *args, **kwargs):
        time = datetime.datetime.now().isoformat()

        response = StreamingHttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": f'attachment; filename="{time} output.csv"'
            },
        )

        LogbookStreamCSVWriter(
            response=response, write_strategy=CSVWriteStrategy()
        ).write(
            Logbook(aircraft_qs=Aircraft.objects.all(), flight_qs=Flight.objects.all())
            .get()
            .render()
        )

        return response
