from django.urls import path
from django.urls.resolvers import URLPattern
from rest_usuario.views import lista_usua, detalle_usuario

urlpatterns = [
    path('lista_usua', lista_usua, name="lista_usua"),
    path('detalle_usuario/<id>', detalle_usuario, name="detalle_usuario"),
]