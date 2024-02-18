import datetime
import logging

from django.http import StreamingHttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from exporter.writer import CSVWriteStrategy
from importer.utils import do_import
from importer.converters import LogEntryConverter
from importer.readers import JsonFileReadStrategy, StringReader
from pilotlog.forms import UploadJsonFileForm
from pilotlog.extns.exporter.logbook import DjangoLogbook
from pilotlog.extns.exporter.writers import LogbookStreamCSVWriter
from pilotlog.extns.importer.saver import DjangoSaver


class IndexView(FormView):
    form_class = UploadJsonFileForm
    template_name = 'pilotlog/index.html'

    def form_valid(self, form):

        for f in form.cleaned_data["file"]:
            try:
                self.import_file(f)
            except Exception as e:
                logging.error(e)
                form.add_error("file", "Could not import provided file")
                return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('import_logbook_csv')

    def import_file(self, file):
        do_import(
            reader=StringReader(data=file.decode("utf-8"), read_strategy=JsonFileReadStrategy()),
            converter=LogEntryConverter(),
            saver=DjangoSaver(),
        )


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
            DjangoLogbook().get().render()
        )

        return response
