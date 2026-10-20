import requests

# URL limpia
BASE_URL = "https://t1-pyfastapi-tg1b.onrender.com/trainees"


def limpiar_pantalla():
  input("\nPresiona Enter para continuar...")
  print("\n" + "=" * 50 + "\n")


def mostrar_menu():
  print("--- GESTIÓN DE APRENDICES (CONSOLA) ---")
  print("1. Registrar nuevo aprendiz")
  print("2. Listar todos los aprendices")
  print("3. Buscar aprendiz por ID")
  print("4. Actualizar aprendiz")
  print("5. Eliminar aprendiz")
  print("6. Salir")


def registrar_aprendiz():
  print("\n--- Registrar Aprendiz ---")
  document = input("Documento (document): ")
  firstname = input("Nombres (firstname): ")
  lastname = input("Apellidos (lastname): ")
  email = input("Correo electrónico (email): ")
  age = int(input("Edad (age): "))
  program = input("Programa de formación (program): ")
  record_number = int(input("Número de ficha (record_number): "))

  data = {
      "document": document,
      "firstname": firstname,
      "lastname": lastname,
      "email": email,
      "age": age,
      "program": program,
      "record_number": record_number,
  }

  response = requests.post(f"{BASE_URL}/", json=data)
  if response.status_code == 201:
    print("\n¡Aprendiz registrado exitosamente!")
    print(response.json())
  else:
    print(f"\nError ({response.status_code}):", response.json())


def listar_aprendices():
  print("\n--- Lista de Aprendices ---")
  response = requests.get(f"{BASE_URL}/")
  if response.status_code == 200:
    aprendices = response.json()
    if not aprendices:
      print("No hay aprendices registrados.")
    for a in aprendices:
      print(
          f"ID: {a['id']} | Doc: {a['document']} | Nombre: {a['firstname']}"
          f" {a['lastname']} | Ficha: {a['record_number']}"
      )
  else:
    print("Error al obtener los aprendices:", response.text)


def buscar_aprendiz():
  print("\n--- Buscar Aprendiz por ID ---")
  id_aprendiz = input("Ingrese el ID del aprendiz: ")
  response = requests.get(f"{BASE_URL}/{id_aprendiz}")
  if response.status_code == 200:
    print("\nAprendiz encontrado:")
    print(response.json())
  else:
    print("\nAprendiz no encontrado o ID inválido.")


def actualizar_aprendiz():
  print("\n--- Actualizar Aprendiz ---")
  id_aprendiz = input("Ingrese el ID del aprendiz a actualizar: ")

  print("Deje el campo vacío si no desea actualizarlo.")
  firstname = input("Nuevo nombre: ")
  lastname = input("Nuevo apellido: ")
  email = input("Nuevo correo: ")
  age_str = input("Nueva edad: ")
  program = input("Nuevo programa de formación: ")
  record_str = input("Nueva ficha: ")

  data = {}
  if firstname:
    data["firstname"] = firstname
  if lastname:
    data["lastname"] = lastname
  if email:
    data["email"] = email
  if age_str:
    data["age"] = int(age_str)
  if program:
    data["program"] = program
  if record_str:
    data["record_number"] = int(record_str)

  response = requests.put(f"{BASE_URL}/{id_aprendiz}", json=data)
  if response.status_code == 200:
    print("\n¡Aprendiz actualizado con éxito!")
    print(response.json())
  else:
    print(f"\nError ({response.status_code}):", response.json())


def eliminar_aprendiz():
  print("\n--- Eliminar Aprendiz ---")
  id_aprendiz = input("Ingrese el ID del aprendiz a eliminar: ")
  response = requests.delete(f"{BASE_URL}/{id_aprendiz}")
  if response.status_code == 200:
    print("\n¡Aprendiz eliminado exitosamente!")
  else:
    print("\nAprendiz no encontrado.")


def main():
  while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
      registrar_aprendiz()
    elif opcion == "2":
      listar_aprendices()
    elif opcion == "3":
      buscar_aprendiz()
    elif opcion == "4":
      actualizar_aprendiz()
    elif opcion == "5":
      eliminar_aprendiz()
    elif opcion == "6":
      print("\nSaliendo del sistema...")
      break
    else:
      print("\nOpción inválida. Intente de nuevo.")
    limpiar_pantalla()


if __name__ == "__main__":
  main()