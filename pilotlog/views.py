import datetime

from django.http import StreamingHttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from exporter.writer import CSVWriteStrategy
from importer.converters.iter import converted_items
from importer.converters.json import JsonLogEntryConverter
from importer.readers import JsonFileReadStrategy
from pilotlog.forms import UploadJsonFileForm
from pilotlog.importer.readers import BytesReader
from pilotlog.serives.exporting import get_logbook
from pilotlog.exporter.writers import LogbookStreamCSVWriter
from pilotlog.serives.importing import DjangoImportSaver


class IndexView(FormView):
    form_class = UploadJsonFileForm
    template_name = 'pilotlog/index.html'

    def form_valid(self, form):
        files = form.cleaned_data["file"]
        saver = DjangoImportSaver()

        for f in files:

            reader = BytesReader(
                bytes=f,
                read_strategy=JsonFileReadStrategy()
            )

            saver.save(
                items=converted_items(
                    items=reader.read(),
                    converter=JsonLogEntryConverter()
                )
            )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('import_logbook_csv')


class CSVLogbookExportView(View):
    def get(self, request, *args, **kwargs):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = StreamingHttpResponse(
            content_type="text/csv",
            headers={'Content-Disposition': f'attachment; filename="{time} output.csv"'}
        )

        LogbookStreamCSVWriter(
            response=response,
            write_strategy=CSVWriteStrategy()
        ).write(
            get_logbook().render()
        )

        return response
