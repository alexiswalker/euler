
def obtener_datos_desde_archivo(path):
    with open(path, 'r') as f:
        file = f.readlines()

    return [map(int, i.split(' ')) for i in file]

def coordenada_izquierdo(fila, columna):
    return (fila+1, columna)

def coordenada_derecho(fila, columna):
    return (fila+1, columna+1)
    
        
if __name__ == '__main__':
    datos = obtener_datos_desde_archivo('p067_triangle.txt')     
    for i in range(datos.__len__()-1)[::-1]:
        for j in range(datos[i].__len__()):
            coord = coordenada_izquierdo(i, j)
            valor_izquierdo = datos[coord[0]][coord[1]]

            coord = coordenada_derecho(i,j)
            valor_derecho = datos[coord[0]][coord[1]]

            padre = datos[i][j]

            datos[i][j]=max(padre + valor_derecho, padre + valor_izquierdo)
    
    print datos[0][0]