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
        

class DatosExternosjuan(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    

    class Meta:
        db_table = 'datos_externosjuan'

    def __str__(self):
        return self.nombre
        
        
class DatosExternoscris(models.Model):
   
    descripcion = models.CharField(max_length=80)
    stock = models.IntegerField()
    ubicacion = models.CharField(max_length=20)

    class Meta:
        db_table = 'PRODUCTOS_CRISTIAN'
        

class DatosExternoscamilo(models.Model):
    
    materia = models.CharField(max_length=255)
    profesor = models.CharField(max_length=255)
    horario = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.materia} - {self.profesor} ({self.horario})"

    class Meta:
        db_table = 'Materias_camilo' 
        
# Create your models here.

