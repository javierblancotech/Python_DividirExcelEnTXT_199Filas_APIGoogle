import pandas as pd
import os

print("Iniciando el script...")

# Ruta al archivo Excel
ruta_excel = r"E:\PROYECTOS SEO\quevisitarenestadosunidos.com\IndexacionAPI\tu_archivo.xlsx"

# Ruta al directorio de salida
ruta_output = r"E:\PROYECTOS SEO\quevisitarenestadosunidos.com\IndexacionAPI\output_txt_files"

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

# Iniciar una lista temporal y un contador para los archivos de salida
temp_list = []
file_counter = 1

print("Filtrando y agrupando los registros...")
for item in primera_columna:
    # Solo añadir el ítem a la lista temporal si su URL no termina en '/feed/'
    if not str(item).endswith('/feed/'):
        temp_list.append(item)

    # Si la lista temporal tiene 199 elementos, guardarlos en un archivo y limpiar la lista
    if len(temp_list) == 199:
        filename = os.path.join(ruta_output, f"batch{file_counter}.txt")
        print(f"Guardando {filename}...")
        with open(filename, 'w') as f:
            for line in temp_list:
                f.write(f"{line}\n")
        temp_list.clear()
        file_counter += 1

# Guardar cualquier elemento restante en un nuevo archivo
if temp_list:
    filename = os.path.join(ruta_output, f"batch{file_counter}.txt")
    print(f"Guardando {filename}...")
    with open(filename, 'w') as f:
        for line in temp_list:
            f.write(f"{line}\n")

print("El script ha finalizado exitosamente.")
