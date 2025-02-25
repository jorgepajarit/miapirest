import os
import django
import csv

# 🔹 Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jorgeapp.settings')
django.setup()

# 🔹 Importar el modelo
from jorgeluisapp.models import MeteoriteLanding

# Ruta del archivo CSV (ajústala si es necesario)
FILE_PATH = os.path.expanduser("~/Desktop/datoskaggle/meteorite_data/Meteorite_Landings.csv")

def obtener_meteoros():
    """ Importa hasta 500 registros SOLO con ID y Name desde el CSV y los guarda en la base de datos """
    if not os.path.exists(FILE_PATH):
        print(f"❌ Error: No se encontró el archivo {FILE_PATH}")
        return

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        batch = []
        max_registros = 500
        nuevos = 0

        for row in reader:
            if nuevos >= max_registros:
                break  # 🔹 Detener cuando alcanzamos el límite de 500

            # Validar que el CSV tenga las columnas correctas
            if "id" not in row or "name" not in row:
                print("❌ Error: El CSV no contiene las columnas 'id' y 'name'.")
                return

            # Obtener ID y Nombre, ignorando todo lo demás
            meteorite_id = int(row["id"]) if row["id"].isdigit() else None
            name = row["name"].strip()  # Evitar espacios en blanco innecesarios

            if meteorite_id and name:  # 🔹 Solo agregar si ambos valores existen
                batch.append(MeteoriteLanding(id=meteorite_id, name=name))  # 👈 Cambié `meteorite_id` por `id`
                nuevos += 1

        # Insertar en la base de datos
        if batch:
            MeteoriteLanding.objects.bulk_create(batch, ignore_conflicts=True)

        print(f"\n🚀 Proceso completado: Se importaron {nuevos} registros.")

# Ejecutar la importación cuando se corre el script
if __name__ == "__main__":
    obtener_meteoros()

