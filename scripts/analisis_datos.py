# =============================================================
# Análisis de Datos Climáticos Globales
# Proyecto: TP Organización Empresarial - UTN TUP
# Rol: P2 - Paco (Desarrollador Técnico)
# Trazabilidad: CLIM-2
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------------
# 1. CARGA DE DATOS
# Leemos el CSV desde la carpeta /datos usando ruta relativa
# para garantizar la reproducibilidad en cualquier entorno
# -------------------------------------------------------------
df = pd.read_csv("datos/dataset_climatico.csv")
print("Dataset cargado correctamente")
print(df.head())
print(f"\nColumnas disponibles: {df.columns.tolist()}")
print(f"Total de registros: {len(df)}")

# -------------------------------------------------------------
# 2. LIMPIEZA DE DATOS
# Eliminamos filas con valores nulos para evitar errores
# en los cálculos estadísticos posteriores
# -------------------------------------------------------------
df = df.dropna()
print(f"\nRegistros tras limpieza: {len(df)}")

# -------------------------------------------------------------
# 3. INDICADORES ESTADÍSTICOS
# Calculamos los indicadores básicos requeridos por el TP
# sobre la columna de temperatura promedio global
# -------------------------------------------------------------
col_temp = "Mean"  # Columna de temperatura del dataset GISTEMP

temp_promedio = df[col_temp].mean()
temp_maxima = df[col_temp].max()
temp_minima = df[col_temp].min()

print("\n=== INDICADORES CLIMÁTICOS ===")
print(f"Temperatura promedio global: {temp_promedio:.4f} °C")
print(f"Temperatura máxima registrada: {temp_maxima:.4f} °C")
print(f"Temperatura mínima registrada: {temp_minima:.4f} °C")

# -------------------------------------------------------------
# 4. GUARDAR RESULTADOS EN TEXTO
# Exportamos los indicadores a un archivo de texto en /resultados
# para documentar el análisis de forma reproducible
# -------------------------------------------------------------
os.makedirs("resultados", exist_ok=True)

with open("resultados/indicadores.txt", "w") as f:
    f.write("=== INDICADORES CLIMÁTICOS GLOBALES ===\n")
    f.write(f"Temperatura promedio global: {temp_promedio:.4f} °C\n")
    f.write(f"Temperatura máxima registrada: {temp_maxima:.4f} °C\n")
    f.write(f"Temperatura mínima registrada: {temp_minima:.4f} °C\n")

print("\n✓ Indicadores guardados en resultados/indicadores.txt")

# -------------------------------------------------------------
# 5. GRÁFICO DE EVOLUCIÓN DE TEMPERATURA
# Filtramos por fuente GISTEMP y extraemos el año de la columna
# "Year" que tiene formato "YYYY-MM" en este dataset
# -------------------------------------------------------------
df_gistemp = df[df["Source"] == "GISTEMP"].copy()
df_gistemp["Anio"] = df_gistemp["Year"].astype(str).str[:4].astype(int)

df_anual = df_gistemp.groupby("Anio")[col_temp].mean().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(df_anual["Anio"], df_anual["Mean"], color="tomato", linewidth=2)
plt.axhline(y=0, color="gray", linestyle="--", linewidth=0.8)
plt.title("Evolución de la Temperatura Promedio Global (GISTEMP)", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Anomalía de Temperatura (°C)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("resultados/grafico_temperatura.png", dpi=150)
plt.show()
print("✓ Gráfico guardado en resultados/grafico_temperatura.png")
