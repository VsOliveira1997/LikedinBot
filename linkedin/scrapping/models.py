from django.db import models



class Usuarios (models.Model):
    nome = models.CharField(max_length=50)
# Create your models here.

class Usuario_endereco (models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=250)