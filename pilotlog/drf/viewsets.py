from rest_framework import viewsets

from .serializers import LogEntrySerializer, AircraftSerializer, FlightSerializer
from ..models import LogEntry, Aircraft, Flight


class LogEntryViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.select_related("content_type")
    serializer_class = LogEntrySerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related("aircraft", "arr", "dep")
    serializer_class = FlightSerializer
