from django.db import models


# Create your models here.
#class Genero(models.Model):
#    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
#    genero     = models.CharField(max_length=20, blank=False, null=False)

#    def __str__(self):
#        return str(self.genero)

class Usuario(models.Model):

    idUser          = models.AutoField(db_column='idUser', primary_key=True)
    nombre          = models.CharField(max_length=20)
    email           = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono        = models.CharField(max_length=45)


    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombreP         = models.CharField(max_length=64)
    categoria       = models.CharField(max_length=32)
    precio          = models.IntegerField()

    def __str__(self):
        return f'{self.nombreP} -> {self.precio}'