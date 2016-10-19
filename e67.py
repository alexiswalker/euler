
def obtener_datos_desde_archivo(path):
    with open(path, 'r') as f:
        file = f.readlines()

    return [map(int, i.split(' ')) for i in file]
        
if __name__ == '__main__':
    print obtener_datos_desde_archivo('p067_triangle.txt')     
  