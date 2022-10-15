import requests as fetch


def getPersonas():
    res = fetch.get("http://localhost:5000/personas")
    if res.status_code == 200:
        return res.json()
    else:
        return []


def deletePersona(cedula):
    res = fetch.delete("http://localhost:5000/personas/" + cedula)
    if res.status_code == 200:
        print("Persona eliminada")
    else:
        print("Persona no encontrada")


def cliente():
    print("Bienvenido al sistema de personas")
    while True:
        print("1. Ver personas")
        print("2. Eliminar persona")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            try:
                personas = getPersonas()
                for persona in personas:
                    print(persona)
            except:
                print("Error al obtener personas")

        elif opcion == "2":
            try:
                cedula = input("Ingrese la cedula: ")
                deletePersona(cedula)
            except:
                print("Error al eliminar persona")

        elif opcion == "3":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    cliente()
