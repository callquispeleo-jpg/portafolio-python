# generar_datos_ejemplo.py
# Crea un archivo ventas.xlsx de ejemplo para probar el reporte.

import pandas as pd

datos = {
    "fecha": [
        "2026-11-01", "2026-11-02", "2026-11-03", "2026-11-04",
        "2026-11-05", "2026-11-06", "2026-11-07", "2026-11-08",
    ],
    "producto": [
        "Laptop", "Mouse", "Teclado", "Laptop",
        "Monitor", "Mouse", "Teclado", "Monitor",
    ],
    "cantidad": [2, 10, 5, 1, 3, 7, 2, 1],
    "precio": [2500, 25, 80, 2500, 700, 25, 80, 700],
}

df = pd.DataFrame(datos)
df.to_excel("ventas.xlsx", index=False)
print("Listo: se creó 'ventas.xlsx'")
