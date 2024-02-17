from django.urls import path

from pilotlog import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="import_logbook_csv"),
    path("export/", views.CSVLogbookExportView.as_view(), name="export_logbook_csv"),
]
