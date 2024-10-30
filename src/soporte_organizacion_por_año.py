import os
import shutil

def organizar_archivos_por_año(ruta_archivos):
    """
    Organiza archivos CSV en carpetas por año según el nombre de cada archivo.

    Parameters:
    ruta_archivos (str): Ruta de la carpeta que contiene los archivos CSV.
    """
    # Listar todos los archivos en la carpeta
    archivos = [f for f in os.listdir(ruta_archivos) if f.endswith('.csv')]

    # Procesar cada archivo
    for archivo in archivos:
        # Extraer el año del nombre del archivo (los primeros 4 caracteres)
        año = archivo[:4]

        # Crear una carpeta para el año si no existe
        ruta_carpeta_año = os.path.join(ruta_archivos, año)
        os.makedirs(ruta_carpeta_año, exist_ok=True)

        # Mover el archivo a la carpeta del año correspondiente
        shutil.move(os.path.join(ruta_archivos, archivo), os.path.join(ruta_carpeta_año, archivo))

    print("Archivos organizados por año en carpetas correspondientes.")


