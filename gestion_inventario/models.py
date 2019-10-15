from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre=models.CharField(max_length=15)
    cargo=models.CharField(max_length=30)
    email=models.EmailField()
    contrasena=models.CharField(max_length=30)
    class meta:
        db_table = "Usuario"

class formulario(models.Model):
    nombre_responsable=models.CharField(max_length=15)
    bibloteca=models.CharField(max_length=30)
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    fecha_informe=models.DateField()
    id_usuario=models.CharField(max_length=8)
    class meta:
        db_table = "Formulario"

class concepto(models.Model):
    resp=models.IntegerField()
    cd=models.IntegerField()
    libros=models.IntegerField()
    ssue=models.IntegerField()
    nombre_concepto=models.CharField(max_length=30)
    id_formulario=models.CharField(max_length=8)
    class meta:
        db_table = "Concepto"