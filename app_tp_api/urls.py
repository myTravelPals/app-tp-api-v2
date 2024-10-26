from django.contrib import admin
from django.urls import path

from app_tp_api.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls)
]
