import json

class Archivo:
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño  # en KB

    def __repr__(self):
        return f"Archivo(nombre='{self.nombre}', tipo='{self.tipo}', tamaño={self.tamaño}KB)"


class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = []

    def agregar_archivo(self, archivo):
        
        # isinstance: es una función incorporada que se usa para verificar si un objeto es una instancia de una clase específica
        if not isinstance(archivo, Archivo):
            raise TypeError("Solo se pueden agregar objetos de tipo Archivo.")
        self.archivos.append(archivo)

    def buscar_archivo(self, nombre):
        return [a for a in self.archivos if a.nombre == nombre]

    def organizar_por(self, atributo="tipo"):
        self.archivos.sort(key=lambda a: getattr(a, atributo, None))

    def __repr__(self):
        return f"Carpeta(nombre='{self.nombre}', archivos={self.archivos})"


class Archivador:
    def __init__(self):
        self.carpetas = {}

    def crear_carpeta(self, nombre):
        if nombre in self.carpetas:
            raise ValueError(f"La carpeta '{nombre}' ya existe.")
        self.carpetas[nombre] = Carpeta(nombre)

    def agregar_archivo(self, nombre_carpeta, archivo):
        if nombre_carpeta not in self.carpetas:
            raise ValueError(f"La carpeta '{nombre_carpeta}' no existe.")
        self.carpetas[nombre_carpeta].agregar_archivo(archivo)

    def buscar_archivo_global(self, nombre):
        resultados = []
        for carpeta in self.carpetas.values():
            resultados.extend(carpeta.buscar_archivo(nombre))
        return resultados

    def organizar_carpeta(self, nombre_carpeta, atributo="tipo"):
        if nombre_carpeta not in self.carpetas:
            raise ValueError(f"La carpeta '{nombre_carpeta}' no existe.")
        self.carpetas[nombre_carpeta].organizar_por(atributo)

    def guardar_estado(self, ruta):
        estado = {}
        for nombre, carpeta in self.carpetas.items():
            estado[nombre] = [archivo.__dict__ for archivo in carpeta.archivos]
        with open(ruta, "w") as f:
            json.dump(estado, f, indent=4)

    def cargar_estado(self, ruta):
        with open(ruta, "r") as f:
            estado = json.load(f)
        self.carpetas = {}
        for nombre, archivos in estado.items():
            carpeta = Carpeta(nombre)
            for datos in archivos:
                archivo = Archivo(**datos)
                carpeta.agregar_archivo(archivo)
            self.carpetas[nombre] = carpeta

    def __repr__(self):
        return f"Archivador(carpetas={self.carpetas})"
