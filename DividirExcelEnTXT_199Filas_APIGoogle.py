import pandas as pd
import os

print("Iniciando el script...")

# Ruta al archivo Excel
ruta_excel = r"E:\PROYECTOS SEO\quevisitarenfrancia.com\IndexingAPI_Google\ParaIndexar\Libro1.xlsx"

# Ruta al directorio de salida
ruta_output = r"E:\PROYECTOS SEO\quevisitarenfrancia.com\IndexingAPI_Google\ParaIndexar\output_txt_files"

print(f"Leyendo el archivo Excel desde {ruta_excel}...")
# Leer el archivo Excel
df = pd.read_excel(ruta_excel)

# Crear el directorio para guardar los archivos .txt si no existe
print(f"Verificando la existencia del directorio de salida {ruta_output}...")
if not os.path.exists(ruta_output):
    print(f"Creando el directorio {ruta_output}...")
    os.makedirs(ruta_output)

# Obtener la primera columna
print("Obteniendo la primera columna del archivo Excel...")
primera_columna = df.iloc[:, 0]

# Dividir la columna en fragmentos de 199 filas
print("Dividiendo la primera columna en fragmentos de 199 filas...")
batches = [primera_columna[i:i+199] for i in range(0, len(primera_columna), 199)]

# Crear archivos .txt para cada lote
print("Creando archivos .txt para cada fragmento...")
for i, batch in enumerate(batches):
    filename = os.path.join(ruta_output, f"batch{i+1}.txt")
    print(f"Guardando {filename}...")
    with open(filename, 'w') as f:
        for item in batch:
            # Solo escribir el ítem si su URL no termina en '/feed'
            if not str(item).endswith('/feed/'):
                f.write(f"{item}\n")

print("El script ha finalizado exitosamente.")
