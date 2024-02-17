from django.urls import path

from pilotlog import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("export/", views.LogbookExportView.as_view(), name="export"),
]
