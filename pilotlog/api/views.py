from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from pilotlog.api.serializers import ImportSerializer


class ImportView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImportSerializer
