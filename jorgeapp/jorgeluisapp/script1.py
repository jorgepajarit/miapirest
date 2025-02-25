import os
import django
import requests
from .models import DatosExternosjuan, DatosExternoscris, DatosExternoscamilo

def obtenerdatosjuan():
    urls = "http://54.157.69.113:8000/api/usuarios/"  # API de Juan
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = DatosExternosjuan.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                DatosExternosjuan.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    nombre=item["nombre"],
                    email=item["email"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
def obtenerdatoscris():
    urls = "http://3.19.235.79:8000/api/productos/"  # API de cris
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = DatosExternoscris.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                DatosExternoscris.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    descripcion =item["descripcion"],
                    stock =item["stock"],
                    ubicacion =item["ubicacion"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
def obtenerdatoscamilo():
    urls = "https://taller.imesh.app/materias"  # API de camilo
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()
        
        for item in data:
            # Verificar si ya existe un registro con el mismo 'id'
            existing_record = DatosExternoscamilo.objects.filter(id=item["id"]).first()

            if existing_record:
                # Si el registro ya existe, no hace nada
                print(f"El registro con ID {item['id']} ya existe y no se agrega.")
            else:
                # Si el registro no existe, lo agrega
                DatosExternoscamilo.objects.create(
                    id=item["id"],  # Asegurándote de que la primary key (id) se use al crear el nuevo registro
                    materia =item["materia"],
                    profesor =item["profesor"],
                    horario =item["horario"]
                )
                print(f"Nuevo registro creado para ID {item['id']}")

        print("Proceso completado")
    else:
        print(f"No se pudieron obtener los datos, código de estado: {response.status_code}")
        
def camilo2():
    urls = "https://taller.imesh.app/materias"  # API de Camilo
    response = requests.get(urls)   

    if response.status_code == 200:
        data = response.json()

        for item in data:
            try:
                # Acceder a los valores usando índices, ya que 'item' es una lista
                item_id = item[0]  # ID está en el primer índice (0)
                materia = item[1]  # Materia está en el segundo índice (1)
                profesor = item[2]  # Profesor está en el tercer índice (2)
                horario = item[3]  # Horario está en el cuarto índice (3)

                # Verificar si ya existe un registro con el mismo 'id'
                existing_record = DatosExternoscamilo.objects.filter(id=item_id).first()

                if existing_record:
                    print(f"El registro con ID {item_id} ya existe y no se agrega.")
                else:
                    # Crear nuevo registro
                    DatosExternoscamilo.objects.create(
                        id=item_id,  
                        materia=materia,
                        profesor=profesor,
                        horario=horario
                    )
                    print(f"Nuevo registro creado para ID {item_id}")

            except IndexError as e:
                print(f"Error: falta un campo en la lista de Camilo: {e}")
            except Exception as e:
                print(f"Ocurrió un error al procesar los datos de Camilo: {e}")

        print("Proceso completado para Camilo")
    else:
        print(f"No se pudieron obtener los datos de Camilo, código de estado: {response.status_code}")

        
        
def obtener_datos():
    obtenerdatosjuan()  #  es el metodo de juan
    obtenerdatoscris()  #  el metodo de cris
    camilo2() #  el metodo de camilo con arrays
   

    


        
        




