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
        
        
class MeteoriteLanding(models.Model):
     
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.name} ({self.year})"
        

class Trip(models.Model):
    id_envio = models.AutoField(primary_key=True)  # Clave primaria autoincremental
    gps_provider = models.CharField(max_length=50, blank=True, null=True)
    booking_id = models.CharField(max_length=50, blank=True, null=True)
    market_regular = models.CharField(max_length=20, blank=True, null=True)
    booking_id_date = models.DateTimeField(blank=True, null=True)
    vehicle_no = models.CharField(max_length=20, blank=True, null=True)
    origin_location = models.CharField(max_length=255, blank=True, null=True)
    destination_location = models.CharField(max_length=255, blank=True, null=True)
    org_lat_lon = models.CharField(max_length=50, blank=True, null=True)
    des_lat_lon = models.CharField(max_length=50, blank=True, null=True)
    data_ping_time = models.DateTimeField(blank=True, null=True)
    planned_eta = models.DateTimeField(blank=True, null=True)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    destination_location_actual = models.CharField(max_length=255, blank=True, null=True)
    actual_eta = models.DateTimeField(blank=True, null=True)
    curr_lat = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    curr_lon = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ontime = models.BooleanField(default=False)
    delay = models.CharField(max_length=20, null=True, blank=True)
    origin_location_code = models.CharField(max_length=50, blank=True, null=True)
    destination_location_code = models.CharField(max_length=50, blank=True, null=True)
    trip_start_date = models.DateTimeField(blank=True, null=True)
    trip_end_date = models.DateTimeField(blank=True, null=True)
    transportation_distance_in_km = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    minimum_kms_to_be_covered_in_a_day = models.CharField(max_length=50, blank=True, null=True)
    driver_name = models.CharField(max_length=100, blank=True, null=True)
    driver_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)
    customer_name_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_id = models.CharField(max_length=50, blank=True, null=True)
    supplier_name_code = models.CharField(max_length=255, blank=True, null=True)
    material_shipped = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'trip_data'  # Especificamos que se use la tabla existente

    def __str__(self):
        return f"Trip {self.id_envio} from {self.origin_location} to {self.destination_location}"
        
    
class Envio(models.Model):
    id = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    rango_peso_envio = models.CharField(max_length=50)
    ambito = models.CharField(max_length=50)
    tipo_envio = models.CharField(max_length=50)
    tipo_servicio = models.CharField(max_length=50)
    ingresos = models.CharField(max_length=150)
    numero_total_envios = models.IntegerField()
    
    class Meta:
        db_table = 'envios' 

    def __str__(self):
        return f"Envio {self.id} - {self.proveedor}"



        
# Create your models here.

