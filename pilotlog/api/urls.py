from django.urls import path

from pilotlog.api.views import ImportView


urlpatterns = [
    path("import/", ImportView.as_view(), name="import"),
]
