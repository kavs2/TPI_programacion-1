from funciones import *
from validaciones import pedir_opcion, pedir_texto
import os

RUTA_CSV = os.path.join(os.path.dirname(__file__), "paises.csv")

# ------- Estructura general del menu -----

def menu():
    while True:
        print("\n=== Gestión de Países ===")
        print("1. Agregar país")
        print("2. Actualizar poblacion o superficie")
        print("3. Buscar país por nombre")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Estadísticas")
        print("0. Salir")

        opcion = pedir_opcion(
            "\nIngrese una opción: ",
            ["0", "1", "2", "3", "4", "5", "6"]
        )

        if opcion == "1":
            print()
            if agregar_pais(paises):
                guardar_csv(paises, RUTA_CSV)
        elif opcion == "2":
            if actualizar_pais(paises):
                guardar_csv(paises, RUTA_CSV)
        elif opcion == "3":
            texto_busqueda = pedir_texto("Ingrese el nombre del país a buscar: ")
            resultados = buscar_por_nombre(paises, texto_busqueda)
            mostrar_paises(resultados)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Saliendo...")
            break

paises = cargar_csv(RUTA_CSV)

if paises is not None:
    menu()
else:
    print()
    print("El programa no puede iniciarse porque el archivo CSV debe corregirse.")
