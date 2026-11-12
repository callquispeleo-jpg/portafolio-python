# reporte_excel.py
# Lee un Excel de ventas, calcula un resumen por producto
# y genera un nuevo Excel con el reporte.
# Proyecto de portafolio usando pandas.

import pandas as pd


def leer_ventas(archivo):
    """Lee el Excel y devuelve un DataFrame."""
    return pd.read_excel(archivo)


def calcular_resumen(df):
    """Agrupa por producto y calcula unidades e ingresos."""
    df["ingreso"] = df["cantidad"] * df["precio"]

    resumen = (
        df.groupby("producto")
        .agg(unidades=("cantidad", "sum"), ingreso=("ingreso", "sum"))
        .reset_index()
        .sort_values("ingreso", ascending=False)
    )
    return resumen


def main():
    df = leer_ventas("ventas.xlsx")
    resumen = calcular_resumen(df)

    total_ingresos = resumen["ingreso"].sum()
    total_unidades = resumen["unidades"].sum()

    # Guarda el reporte en un Excel con dos hojas
    with pd.ExcelWriter("reporte.xlsx") as writer:
        resumen.to_excel(writer, sheet_name="Resumen", index=False)
        df.to_excel(writer, sheet_name="Datos", index=False)

    print("=== REPORTE DE VENTAS ===")
    print(resumen.to_string(index=False))
    print(f"\nTotal de ingresos: S/ {total_ingresos:,.2f}")
    print(f"Unidades vendidas: {total_unidades}")
    print("\nReporte guardado en 'reporte.xlsx'")


if __name__ == "__main__":
    main()
    try:
        input("\nPresiona Enter para cerrar...")
    except EOFError:
        pass
