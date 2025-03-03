import os
import django
import csv
from datetime import datetime
from django.utils import timezone
from django.db import transaction

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jorgeapp.settings')
django.setup()

from jorgeluisapp.models import Trip

# Ruta del archivo CSV
FILE_PATH = os.path.expanduser("~/Desktop/datos/Delivery_truck_trip_data1.csv")

def convertir_fecha(fecha_str):
    """Convierte una cadena de fecha en objeto datetime, asegurando compatibilidad con zona horaria."""
    if not fecha_str or fecha_str.upper() == "NULL":
        return None  # Ahora sí deja los valores nulos

    if "." in fecha_str:
        fecha_str = fecha_str.split(".")[0]

    formatos = ["%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d", "%Y-%m-%d"]

    for formato in formatos:
        try:
            fecha = datetime.strptime(fecha_str, formato)
            return timezone.make_aware(fecha)
        except ValueError:
            continue

    print(f"⚠️ Error de formato en fecha: {fecha_str}")
    return None

def convertir_float(valor):
    """Convierte un valor a float, asegurando que solo se convierten números válidos."""
    if not valor or valor.strip().upper() in ["NULL", "R", ""]:
        return None  
    
    try:
        return float(valor)
    except ValueError:
        print(f"⚠️ Error de conversión en valor flotante: {valor}")
        return None

def importar_viajes():
    """Importa registros desde un CSV y los guarda en la base de datos."""
    if not os.path.exists(FILE_PATH):
        print(f"❌ Error: No se encontró el archivo {FILE_PATH}")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        batch = []
        total_importados = 0
        errores = 0

        for i, row in enumerate(reader, start=1):
            try:
                trip = Trip(
                    gps_provider=row.get("GpsProvider", ""),
                    booking_id=row.get("BookingID", ""),
                    market_regular=row.get("Market_Regular", ""),
                    booking_id_date=convertir_fecha(row.get("BookingID_Date")),
                    vehicle_no=row.get("vehicle_no", ""),
                    origin_location=row.get("Origin_Location", ""),
                    destination_location=row.get("Destination_Location", ""),
                    org_lat_lon=row.get("Org_lat_lon", ""),
                    des_lat_lon=row.get("Des_lat_lon", ""),
                    data_ping_time=convertir_fecha(row.get("Data_Ping_time")),
                    planned_eta=convertir_fecha(row.get("Planned_ETA")),
                    current_location=row.get("Current_Location", ""),
                    destination_location_actual=row.get("DestinationLocation", ""),
                    actual_eta=convertir_fecha(row.get("actual_eta")),
                    curr_lat=convertir_float(row.get("Curr_lat")),
                    curr_lon=convertir_float(row.get("Curr_lon")),
                    ontime=row.get("ontime", "").strip().lower() == "true",
                    delay=row.get("delay", "").strip(),
                    origin_location_code=row.get("OriginLocation_Code", ""),
                    destination_location_code=row.get("DestinationLocation_Code", ""),
                    trip_start_date=convertir_fecha(row.get("trip_start_date")),
                    trip_end_date=convertir_fecha(row.get("trip_end_date")),
                    transportation_distance_in_km=int(row.get("TRANSPORTATION_DISTANCE_IN_KM", "0")) if row.get("TRANSPORTATION_DISTANCE_IN_KM") else None,
                    vehicle_type=row.get("vehicleType", ""),
                    minimum_kms_to_be_covered_in_a_day=row.get("Minimum_kms_to_be_covered_in_a_day", ""),
                    driver_name=row.get("Driver_Name", ""),
                    driver_mobile_no=row.get("Driver_MobileNo", ""),
                    customer_id=row.get("customerID", ""),
                    customer_name_code=row.get("customerNameCode", ""),
                    supplier_id=row.get("supplierID", ""),
                    supplier_name_code=row.get("supplierNameCode", ""),
                    material_shipped=row.get("Material_Shipped", ""),
                )

                batch.append(trip)
                total_importados += 1

                if len(batch) >= 500:  # Guardar en la BD cada 500 registros
                    with transaction.atomic():
                        Trip.objects.bulk_create(batch, ignore_conflicts=True)
                    batch.clear()

            except Exception as e:
                errores += 1
                print(f"⚠️ Error en la fila {i}: {e}")

        if batch:
            with transaction.atomic():
                Trip.objects.bulk_create(batch, ignore_conflicts=True)

    print(f"\n🚀 Proceso completado: Se importaron {total_importados} registros. ❌ Fallaron {errores}.")

if __name__ == "__main__":
    importar_viajes()





