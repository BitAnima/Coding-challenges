import os
import shutil

# Archivos que NO deben moverse de la raíz
EXCEPTIONS = {
    'README.md',
    '.gitignore',
    'requirements.txt',
    'new_folder_structure.py'
    # Añade aquí otros nombres de archivos que quieras mantener en la raíz
}

# Carpetas principales
SRC_FOLDER = 'src'
TESTS_FOLDER = 'tests'

# Crear las carpetas si no existen
os.makedirs(SRC_FOLDER, exist_ok=True)
os.makedirs(TESTS_FOLDER, exist_ok=True)

# Recorre todos los archivos .py en el directorio actual
for filename in os.listdir('.'):
    # Ignora carpetas y archivos de excepción
    if (not os.path.isfile(filename)) or (filename in EXCEPTIONS):
        continue
    # Mueve archivos Python según su nombre
    if filename.endswith('.py'):
        if filename.startswith('test_'):
            shutil.move(filename, os.path.join(TESTS_FOLDER, filename))
            print(f"Movido a tests: {filename}")
        else:
            shutil.move(filename, os.path.join(SRC_FOLDER, filename))
            print(f"Movido a src: {filename}")

print("¡Reorganización completa!")
