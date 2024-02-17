from django.http import StreamingHttpResponse

from exporter.writer import Writer, WriteStrategy


class LogbookStreamCSVWriter(Writer):
    def __init__(self, response: StreamingHttpResponse, write_strategy: WriteStrategy):
        self.response = response
        self.write_strategy = write_strategy

    def write(self, data):
        self.response.streaming_content = self.write_strategy.written_lines(data)
