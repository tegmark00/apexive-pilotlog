from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import ImportView
from .viewsets import LogEntryViewSet, AircraftViewSet, FlightViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("logs", LogEntryViewSet, basename="logs")
router.register("aircrafts", AircraftViewSet, basename="aircrafts")
router.register("flights", FlightViewSet, basename="flights")

urlpatterns = [path("import/", ImportView.as_view(), name="import"), *router.urls]
