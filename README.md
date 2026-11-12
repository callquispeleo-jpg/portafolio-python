# Portafolio Python — Automatización y Reportes

Proyectos de automatización y procesamiento de datos con Python.
Ideales para tareas repetitivas de negocios: reportes, limpieza de datos y Excel.

## Proyectos

### 1. Reporte de ventas desde CSV (`reporte_ventas.py`)

Lee un archivo CSV de ventas, calcula los ingresos totales, las unidades
vendidas y el precio promedio, y guarda el resultado en `resumen.csv`.

**Ejecutar:**

```powershell
python reporte_ventas.py
```

### 2. Reporte de Excel con pandas (`reporte_excel.py`)

Lee `ventas.xlsx`, agrupa las ventas por producto y genera `reporte.xlsx`
con dos hojas: `Resumen` y `Datos`.

**Ejecutar:**

```powershell
python generar_datos_ejemplo.py   # crea ventas.xlsx
python reporte_excel.py           # genera reporte.xlsx
```

## Tecnologías

- Python 3.13
- pandas
- openpyxl

## Autor

Leo
