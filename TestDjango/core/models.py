from django.db import models

# Create your models here.

#modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de categoria')

    def __str__(self):
        return self.nombreCategoria

#modelo para vehiculo

class vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente


#modelos proyecto

class Obra(models.Model):
    nombreOb = models.CharField(max_length=50, primary_key=True, verbose_name= 'Nombre de la Obra')
    autor = models.CharField(max_length=30, verbose_name= 'Autor')
    año = models.CharField(max_length=20, verbose_name='Año')
    tecnica = models.CharField(max_length=50, verbose_name= 'Técnica')
    tamaño = models.CharField(max_length=20, verbose_name='Tamaño')

    def str(self):
        return self.nombreOb
#
class Usuario(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    email = models.EmailField(max_length=100, primary_key=True, verbose_name= 'Email')
    contraseña = models.CharField(max_length=30, verbose_name='Contraseña')

    def str(self):
        return self.email

class Contacto(models.Model):
    nombre = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200, verbose_name= 'mensaje')

    def str(self):
        return self.nombre