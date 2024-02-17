import datetime

from django.http import StreamingHttpResponse
from django.views import View
from django.views.generic import TemplateView

from exporter.writer import Writer, WriteStrategy, CSVWriteStrategy
from pilotlog.serives.exporting import get_logbook


class IndexView(TemplateView):
    template_name = 'pilotlog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'John Doe'
        return context


class LogbookStreamCSVWriter(Writer):
    def __init__(self, response: StreamingHttpResponse, write_strategy: WriteStrategy):
        self.response = response
        self.write_strategy = write_strategy

    def write(self, data):
        self.response.streaming_content = self.write_strategy.written_lines(data)


class LogbookExportView(View):
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
