import csv
from validaciones import pedir_entero_no_negativo, pedir_entero_positivo, pedir_opcion, pedir_texto, validar_fila_csv

# ------------------- CARGA Y GUARDADO CSV ---------------------------
def cargar_csv(ruta):
    paises = []
    error_encontrado = False

    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, strict=True)

            campos_requeridos = ["nombre", "poblacion", "superficie", "continente"]

            if lector.fieldnames is None:
                print("Error: el archivo CSV está vacío.")
                return None

            campos_faltantes = []

            for campo in campos_requeridos:
                if campo not in lector.fieldnames:
                    campos_faltantes.append(campo)

            if len(campos_faltantes) > 0:
                print("Error: faltan columnas en el CSV:", ", ".join(campos_faltantes))
                return None

            numero_fila = 2

            for fila in lector:
                pais = validar_fila_csv(fila, numero_fila)

                if pais is not None:
                    paises.append(pais)

                else:
                    error_encontrado = True

                numero_fila += 1

            if error_encontrado:
                print()
                print("==============================================")
                print("ERROR: el archivo CSV contiene datos inválidos.")
                print("Corrija las filas indicadas antes de continuar.")
                print("==============================================")
                return None

    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
        return None

    except PermissionError:
        print("No se tienen permisos para leer el archivo CSV.")
        return None

    except UnicodeDecodeError:
        print("No se pudo leer el archivo CSV porque su codificación no es válida.")
        return None

    except csv.Error as error:
        print(f"Error de formato en el archivo CSV: {error}.")
        return None

    except OSError as error:
        print(f"No se pudo leer el archivo CSV: {error}.")
        return None

    return paises


def guardar_csv(paises, ruta):
    try:
        paises_validados = []

        numero_fila = 2

        for pais in paises:
            pais_validado = validar_fila_csv(pais, numero_fila)

            if pais_validado is None:
                print("No se guardaron los datos porque hay información inválida.")
                return False

            paises_validados.append(pais_validado)
            numero_fila += 1

        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for pais in paises_validados:
                escritor.writerow(pais)

        print("Los datos se guardaron correctamente.")
        return True

    except PermissionError:
        print("No se tienen permisos para guardar el archivo CSV.")

    except csv.Error as error:
        print(f"Error de formato al guardar el archivo CSV: {error}.")

    except OSError as error:
        print(f"No se pudo guardar el archivo CSV: {error}.")

    return False

# 1. //////////  AGREGAR PAIS \\\\\\\\\\\\

# ---- Agregar pais junto con sus datos ----
def agregar_pais(paises):
    nombre = pedir_texto("Ingrese el nombre del país: ")

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"El país '{nombre}' ya existe.")
            return False

    poblacion = pedir_entero_positivo("Ingrese la población del país: ")
    superficie = pedir_entero_positivo("Ingrese la superficie del país en km²: ")
    continente = pedir_texto("Ingrese el continente del país: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print(f"País '{nombre}' agregado correctamente.")
    return True

# 2. ///////////////// ACTUALIZAR POBLACION O SUPERFICIE \\\\\\\\\\\\\


def actualizar_pais(paises):
    nombre = pedir_texto("Ingrese el nombre del país a actualizar: ")

    pais_encontrado = None

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print(f"No se encontró el país '{nombre}'.")
        return False

    print("\n¿Qué dato desea actualizar?")
    print("1. Población")
    print("2. Superficie")
    print("3. Población y superficie")

    opcion = pedir_opcion("Seleccione una opción: ", ["1", "2", "3"])

    if opcion == "1":
        nueva_poblacion = pedir_entero_positivo(
            f"Nueva población (actual: {pais_encontrado['poblacion']}): "
        )
        pais_encontrado["poblacion"] = nueva_poblacion
        print(f"Población de '{pais_encontrado['nombre']}' actualizada correctamente.")

    elif opcion == "2":
        nueva_superficie = pedir_entero_positivo(
            f"Nueva superficie (actual: {pais_encontrado['superficie']} km²): "
        )
        pais_encontrado["superficie"] = nueva_superficie
        print(f"Superficie de '{pais_encontrado['nombre']}' actualizada correctamente.")

    elif opcion == "3":
        nueva_poblacion = pedir_entero_positivo(
            f"Nueva población (actual: {pais_encontrado['poblacion']}): "
        )
        nueva_superficie = pedir_entero_positivo(
            f"Nueva superficie (actual: {pais_encontrado['superficie']} km²): "
        )
        pais_encontrado["poblacion"] = nueva_poblacion
        pais_encontrado["superficie"] = nueva_superficie
        print(f"País '{pais_encontrado['nombre']}' actualizado correctamente.")

    return True

# 3. /////////////// BUSQUEDA DE PAIS \\\\\\\\\\\\\\\

def buscar_por_nombre(paises, texto_busqueda):
    resultados = []

    for pais in paises:
        if texto_busqueda.lower() in pais["nombre"].lower():
            resultados.append(pais)

    return resultados


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No se encontraron países.")
    else:
        for pais in paises:
            print("-------------------------")
            print("Nombre:", pais["nombre"])
            print("Población:", pais["poblacion"])
            print("Superficie:", pais["superficie"], "km²")
            print("Continente:", pais["continente"])
        print("-------------------------")

# 4. //////////// FILTRAR PAISES \\\\\\\\\\\\

# ------- FILTRAR POR CONTINENTE -------
def filtrar_por_continente(paises, busqueda_continente):
    resultados = []

    for pais in paises:
        if busqueda_continente.lower().strip() == pais["continente"].lower().strip():
            resultados.append(pais)

    return resultados

# ------- FILTRAR POR POBLACION ---------
def filtrar_por_rango_poblacion(paises, busqueda_poblacion_min, busqueda_poblacion_max):
    resultados = []

    for pais in paises:
        if busqueda_poblacion_min <= pais["poblacion"] <= busqueda_poblacion_max:
            resultados.append(pais)

    return resultados

# --------- FILTRAR POR SUPERFICIE ---------
def filtrar_por_rango_superficie(paises, busqueda_superficie_min, busqueda_superficie_max):
    resultados = []

    for pais in paises:
        if busqueda_superficie_min <= pais["superficie"] <= busqueda_superficie_max:
            resultados.append(pais)

    return resultados

# --------- FILTRAR POR PAISES UNIFICADO --------
def filtrar_paises(paises):
    print()
    print("¿Cómo desea filtrar los países?")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion = pedir_opcion("\nIngrese una opción: ", ["1", "2", "3"])

    if opcion == "1":
        continente = pedir_texto("Ingrese el continente: ")
        resultados = filtrar_por_continente(paises, continente)
        mostrar_paises(resultados)

    elif opcion == "2":
        minimo = pedir_entero_no_negativo("Ingrese población mínima: ")
        maximo = pedir_entero_no_negativo("Ingrese población máxima: ")

        while minimo > maximo:
            print("Error: el valor mínimo no puede ser mayor que el máximo.")
            minimo = pedir_entero_no_negativo("Ingrese población mínima: ")
            maximo = pedir_entero_no_negativo("Ingrese población máxima: ")

        resultados = filtrar_por_rango_poblacion(paises, minimo, maximo)
        mostrar_paises(resultados)

    elif opcion == "3":
        minimo = pedir_entero_no_negativo("Ingrese superficie mínima: ")
        maximo = pedir_entero_no_negativo("Ingrese superficie máxima: ")

        while minimo > maximo:
            print("Error: el valor mínimo no puede ser mayor que el máximo.")
            minimo = pedir_entero_no_negativo("Ingrese superficie mínima: ")
            maximo = pedir_entero_no_negativo("Ingrese superficie máxima: ")

        resultados = filtrar_por_rango_superficie(paises, minimo, maximo)
        mostrar_paises(resultados)

# 5. /////////////// ORDENAMIENTOS \\\\\\\\\\\\\\\

# ---- FUNCIONES PARA ORDENAR ----

def ordenar_segun_criterio(paises, criterio, descendente):

    if criterio == "nombre":
        orden_nombre = sorted(paises, key=lambda pais: pais["nombre"], reverse=descendente)
        return orden_nombre
    
    elif criterio == "poblacion":
        orden_poblacion = sorted(paises, key=lambda pais: pais["poblacion"], reverse=descendente)
        return orden_poblacion
    
    elif criterio == "superficie":
        orden_superficie = sorted(paises, key=lambda pais: pais["superficie"], reverse=descendente)
        return orden_superficie
    
    else:
        print("Criterio incorrecto")
        return []

# -------- IMPLEMENTACION FUNCIONES PARA ORDENAR --------

def ordenar_paises(paises):
    print()
    print("¿Por qué criterio desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    opcion_criterio = pedir_opcion("\nIngrese una opción: ", ["1", "2", "3"])

    if opcion_criterio == "1":
        criterio = "nombre"
    elif opcion_criterio == "2":
        criterio = "poblacion"
    else:
        criterio = "superficie"

    print()
    print("¿En qué orden desea mostrar los países?")
    print("1. Ascendente")
    print("2. Descendente")

    opcion_orden = pedir_opcion("\nIngrese una opción: ", ["1", "2"])

    descendente = opcion_orden == "2"

    paises_ordenados = ordenar_segun_criterio(paises, criterio, descendente)

    mostrar_paises(paises_ordenados)

# 6. ////////////// ESTADISTICAS \\\\\\\\\\\\\\

# ----- Min y Max poblacion -----

def estadistica_mayor_poblacion(paises):
    pais_mayor = max(paises, key=lambda pais: pais["poblacion"])
    return pais_mayor


def estadistica_menor_poblacion(paises):
    pais_menor = min(paises, key=lambda pais: pais["poblacion"])
    return pais_menor


# ----- Promedio poblacion y superficie -----

def promedio_poblacion(paises):
    return sum(pais["poblacion"] for pais in paises) / len(paises)


def promedio_superficie(paises):
    return sum(pais["superficie"] for pais in paises) / len(paises)


# ----- Cantidad de paises por continente -----

def paises_por_continente(paises):
    continentes = {}

    for pais in paises:
        continente = pais["continente"]

        if continente not in continentes:
            continentes[continente] = 1
        else:
            continentes[continente] += 1

    return continentes


# ----- Mostrar estadisticas generales -----

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    mayor_poblacion = estadistica_mayor_poblacion(paises)
    menor_poblacion = estadistica_menor_poblacion(paises)
    promedio_pob = promedio_poblacion(paises)
    promedio_sup = promedio_superficie(paises)
    continentes = paises_por_continente(paises)

    print()
    print("----- ESTADÍSTICAS -----")
    print(f"País con mayor población: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']} habitantes)")
    print(f"País con menor población: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']} habitantes)")
    print(f"Promedio de población: {promedio_pob:.2f} habitantes")
    print(f"Promedio de superficie: {promedio_sup:.2f} km²")

    print()
    print("Cantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")
