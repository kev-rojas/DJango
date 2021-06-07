from django.contrib import admin
from .models import Categoria, vehiculo
from .models import Obra, Usuario, Contacto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(vehiculo)
admin.site.register(Obra)
admin.site.register(Usuario)
admin.site.register(Contacto)