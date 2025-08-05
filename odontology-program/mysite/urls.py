from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("treatments/", include("treatments.urls")),
    path("clients/", include("clients.urls")),
    path("admin/", admin.site.urls),
]