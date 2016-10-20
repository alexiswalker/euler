import unittest

from e67 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        self.datos = obtener_datos_desde_archivo('p067_triangle_test.txt')
    
    def test_obtener_datos_desde_archivo(self):
        self.assertEqual(self.datos, [[3],[7,4],[2,4,6],[8,5,9,3]])

    def test_obtener_coordenada_elemento_izquierdo(self):
        self.assertEqual(coordenada_izquierdo(2,0) ,(3,0))

    def test_obtener_coordenada_elemento_derecho(self):
        self.assertEqual(coordenada_derecho(2,0), (3,1))


if __name__ == '__main__':
    unittest.main()