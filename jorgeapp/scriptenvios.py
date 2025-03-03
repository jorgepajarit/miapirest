import os
import csv
from django.core.wsgi import get_wsgi_application

# Configurar Django para usar los modelos
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jorgeapp.settings")  # Ajusta según tu proyecto
get_wsgi_application()

from jorgeluisapp.models import Envio  # Ajusta según tu estructura de modelos

# Ruta del archivo CSV
FILE_PATH1 = os.path.expanduser("~/Desktop/datos/SERVICIO_DE_CORREO_20250301.csv")

# Función auxiliar para limpiar montos (asegurar que funcione)
def limpiar_monto(valor):
    """Convierte montos a float, eliminando caracteres no numéricos"""
    try:
        return float(valor.replace(",", "").replace("$", ""))
    except ValueError:
        return 0.0  # Si no se puede convertir, devuelve 0

def importar_envios():
    """Importa datos desde un CSV a la base de datos"""
    if not os.path.exists(FILE_PATH1):
        print(f"❌ Error: No se encontró el archivo {FILE_PATH1}")
        return

    with open(FILE_PATH1, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        envios = []
        total_importados = 0

        for i, row in enumerate(reader, start=1):  # Enumerar para rastrear el número de fila
            try:
                envio = Envio(
                    periodo=row["PERIODO"],
                    proveedor=row["PROVEEDOR"],
                    direccion=row["DIRECCION"],
                    rango_peso_envio=row["RANGO_PESO_ENVIO"],
                    ambito=row["AMBITO"],
                    tipo_envio=row["TIPO_ENVIO"],
                    tipo_servicio=row["TIPO_SERVICIO"],
                    ingresos=limpiar_monto(row["INGRESOS"]),
                    numero_total_envios=int(row["NUMERO_TOTAL_ENVIOS"])
                )

                envios.append(envio)
                total_importados += 1

                # Guardar en la BD cada 500 registros para optimizar memoria
                if len(envios) >= 500:
                    Envio.objects.bulk_create(envios)
                    envios.clear()

            except Exception as e:
                print(f"⚠️ Error en la fila {i}: {e}")

        # Insertar los últimos registros
        if envios:
            Envio.objects.bulk_create(envios)

        print(f"\n✅ Proceso completado: Se importaron {total_importados} registros.")

if __name__ == "__main__":
    importar_envios()


