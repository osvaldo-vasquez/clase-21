from django.db import models

# Create your models here.

class libro(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=40)
    numpag = models.IntegerField()
    fecha_pub = models.DateField(default="2023-10-16")
    fecha_compra = models.DateField(default="2023-10-16")
    ISBN = models.CharField(max_length=40)

class ebook(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    editorial = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=40)
    numpag = models.IntegerField()
    aplicativo = models.CharField(max_length=40)
    fecha_pub = models.DateField

class autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    nacionalidad = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    premios = models.CharField(max_length=40)

class revista(models.Model):
    nombre = models.CharField(max_length=40)
    webpage = models.URLField(max_length=40)
    genero = models.CharField(max_length=40)
    temas = models.CharField(max_length=40)
    numpag = models.IntegerField()
    fecha_pub = models.DateField
