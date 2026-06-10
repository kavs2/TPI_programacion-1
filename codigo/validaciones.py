def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error: el campo no puede estar vacío.")


def pedir_entero_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)

            if numero > 0:
                return numero

            print("Error: el número debe ser mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_entero_no_negativo(mensaje):
    while True:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)

            if numero >= 0:
                return numero

            print("Error: el número no puede ser negativo.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones_validas:
            return opcion

        print("Opción inválida.")


def validar_fila_csv(fila, numero_fila):
    campos_requeridos = ["nombre", "poblacion", "superficie", "continente"]

    if None in fila:
        print(f"Error en la fila {numero_fila}: la cantidad de columnas no es correcta.")
        return None

    for campo in campos_requeridos:
        if campo not in fila or fila[campo] is None:
            print(f"Error en la fila {numero_fila}: falta el campo {campo}.")
            return None

    nombre = fila["nombre"].strip()
    continente = fila["continente"].strip()

    if nombre == "" or continente == "":
        print(f"Error en la fila {numero_fila}: el nombre y el continente no pueden estar vacíos.")
        return None

    try:
        poblacion = int(fila["poblacion"])
        superficie = int(fila["superficie"])

    except (TypeError, ValueError):
        print(f"Error en la fila {numero_fila}: la población y la superficie deben ser números enteros.")
        return None

    if poblacion <= 0 or superficie <= 0:
        print(f"Error en la fila {numero_fila}: la población y la superficie deben ser mayores que cero.")
        return None

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    return pais
