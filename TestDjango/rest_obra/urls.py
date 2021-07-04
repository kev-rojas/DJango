from django.urls import path
from django.urls.resolvers import URLPattern
from rest_obra.views import listado_obra, detalle_obra

urlpatterns = [
    path('listado_obra', listado_obra, name="listado_obra"),
    path('detalle_obra/<id>', detalle_obra, name="detalle_obra"),
]
