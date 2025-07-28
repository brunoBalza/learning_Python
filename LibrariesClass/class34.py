import os

# Obtener el directorio actual
cwd = os.getcwd()
print("Directorio de trabajo actual:", cwd)

# Cambiar a la subcarpeta (ajustá el nombre según corresponda)
os.chdir(os.path.join(cwd, 'FilesManipulation'))

# Verificar que cambió correctamente
print("Nuevo directorio de trabajo:", os.getcwd())

# Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)

# Renombrar archivo
os.rename('story.txt', 'cuento.txt')
print('Archivo renombrado')

# Listar los archivos .txt nuevamente
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt después del cambio:", txt_files)