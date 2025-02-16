from django.db import models

class Perfil(models.Model):
    nombre_perfil = models.CharField(max_length=100)

    class Meta:  # Corregido: la indentación debe ser consistente
        db_table = 'perfiles'
        
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    email_usuario = models.EmailField(unique=True)
    contrasena_usuario = models.CharField(max_length=255)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    class Meta:  # Corregido: la indentación debe ser consistente
        db_table = 'usuarios' 
        
# Create your models here.

