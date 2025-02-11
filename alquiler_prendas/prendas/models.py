from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen_url = models.URLField(max_length=255, null=True, blank=True)  # Permitir nulos

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre

class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

    

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'usuario'  # Especifica el nombre de la tabla

    def __str__(self):
        return self.username
    

class Testimonio(models.Model):
    usuario = models.ForeignKey('usuario', on_delete=models.CASCADE, null=True, blank=True)  # Referencia al usuario
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    class Meta:
        db_table = 'testimonios'  # Nombre de la tabla en la base de datos

    def __str__(self):
        return f'Testimonio de {self.usuario} - {self.fecha}'