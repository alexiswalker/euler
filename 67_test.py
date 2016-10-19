import unittest

from e67 import Datos

class Test(unittest.TestCase):
    
    def test_obtener_datos_desde_archivo(self):
        datos = Datos()
        datos.obtener_datos_desde_archivo('p067_triangle_test.txt')
        self.assertEqual(datos.datos, [[3],[7,4],[2,4,6],[8,5,9,3]])
        
        
    


if __name__ == '__main__':
    unittest.main()