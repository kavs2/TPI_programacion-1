# 🌍 Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1**
**Tecnicatura Universitaria en Programación — UTN (Distancia)**

---

## 📋 Descripción

Aplicación de consola desarrollada en Python que permite gestionar información sobre países del mundo. El sistema lee datos desde un archivo CSV y ofrece funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

---

## 👥 Integrantes

| Nombre | 
|--------|
| Franco Moiana |
| Leonardo Macre |

---

## 🚀 Instrucciones de uso

### Requisitos
- Python 3.x instalado
- Archivo `paises.csv` en la misma carpeta que el script

### Ejecución
```bash
python main.py
```

### Menú principal
Al ejecutar el programa se mostrará el siguiente menú:

```
========================================
     GESTIÓN DE DATOS DE PAÍSES
========================================
1. Agregar país
2. Actualizar país (población / superficie)
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
0. Salir
========================================
```

---

## 📁 Estructura del proyecto

```
/
├── main.py           # Punto de entrada y menú principal
├── funciones.py      # Todas las funciones del sistema
├── validaciones.py   # Funciones de validación de entrada
├── paises.csv        # Dataset base de países
└── README.md         # Este archivo
```

---

## 📄 Formato del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

---

## 💡 Ejemplos de uso

### Agregar un país
```
Ingrese nombre: Chile
Ingrese población: 19458310
Ingrese superficie (km²): 756102
Ingrese continente: América
✅ País agregado correctamente.
```

### Buscar por nombre
```
Ingrese nombre a buscar: arg
🔍 Resultados encontrados:
- Argentina | Población: 45.376.763 | Superficie: 2.780.400 km² | Continente: América
```

### Estadísticas
```
📊 ESTADÍSTICAS GENERALES
País con mayor población: China — 1.412.600.000
País con menor población: Vaticano — 800
Promedio de población: 48.350.000
Promedio de superficie: 612.000 km²

Países por continente:
  América:  15
  Europa:   20
  Asia:     18
  África:   12
  Oceanía:   5
```

---

## 🎥 Video demostrativo

🔗 [Pendiente — se actualizará antes de la entrega]

---

## 📑 Documentación PDF

🔗 [Ver documentación académica](https://github.com/kavs2/TPI_programacion-1/blob/main/documentacion.pdf)

---

## 🔗 Repositorio

🔗 [https://github.com/kavs2/TPI_programacion-1](https://github.com/kavs2/TPI_programacion-1)
