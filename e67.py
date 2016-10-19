class Datos:
    datos=None
    def obtener_datos_desde_archivo(self, path):
        f = open(path, 'r')
        file = f.readlines()
        f.close()
        self.datos = [i.split(' ') for i in file]
        