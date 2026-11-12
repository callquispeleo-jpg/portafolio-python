# reporte_ventas.py
# Lee un archivo CSV de ventas y genera un reporte resumen.
# Este es tu primer proyecto de portafolio: útil y vendible.

import csv


def leer_ventas(archivo):
    """Lee el CSV y devuelve una lista de diccionarios."""
    ventas = []
    with open(archivo, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            ventas.append(fila)
    return ventas


def calcular_resumen(ventas):
    """Calcula ingresos totales, unidades y precio promedio."""
    total_ingresos = 0
    total_unidades = 0
    for venta in ventas:
        cantidad = int(venta["cantidad"])
        precio = float(venta["precio"])
        total_ingresos += cantidad * precio
        total_unidades += cantidad

    promedio = total_ingresos / total_unidades if total_unidades > 0 else 0
    return total_ingresos, total_unidades, promedio


def guardar_resumen(archivo, total_ingresos, total_unidades, promedio):
    """Guarda el resumen en un nuevo archivo CSV."""
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["metrica", "valor"])
        escritor.writerow(["total_ingresos", round(total_ingresos, 2)])
        escritor.writerow(["total_unidades", total_unidades])
        escritor.writerow(["precio_promedio", round(promedio, 2)])


def main():
    ventas = leer_ventas("ventas.csv")
    total_ingresos, total_unidades, promedio = calcular_resumen(ventas)
    guardar_resumen("resumen.csv", total_ingresos, total_unidades, promedio)

    print(f"Total de ingresos:    S/ {total_ingresos:,.2f}")
    print(f"Unidades vendidas:    {total_unidades}")
    print(f"Precio promedio:      S/ {promedio:,.2f}")
    print("\nResumen guardado en 'resumen.csv'")


if __name__ == "__main__":
    main()
    input("\nPresiona Enter para cerrar...")
