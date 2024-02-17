import datetime

from django.http import StreamingHttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from exporter.writer import CSVWriteStrategy
from importer.utils import do_import
from importer.converters.from_dict import LogEntryConverter
from importer.readers import JsonFileReadStrategy, StringReader
from pilotlog.forms import UploadJsonFileForm
from pilotlog.exporter.logbook import DjangoLogbook
from pilotlog.exporter.writers import LogbookStreamCSVWriter
from pilotlog.importer.saver import DjangoSaver


class IndexView(FormView):
    form_class = UploadJsonFileForm
    template_name = 'pilotlog/index.html'

    def form_valid(self, form):

        for f in form.cleaned_data["file"]:
            do_import(
                reader=StringReader(data=f.decode("utf-8"), read_strategy=JsonFileReadStrategy()),
                converter=LogEntryConverter(),
                saver=DjangoSaver(),
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
            DjangoLogbook().get().render()
        )

        return response
