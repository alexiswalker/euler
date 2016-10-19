import unittest

from e67 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        self.datos = obtener_datos_desde_archivo('p067_triangle_test.txt')
    
    def test_obtener_datos_desde_archivo(self):
        self.assertEqual(self.datos, [[3],[7,4],[2,4,6],[8,5,9,3]])


if __name__ == '__main__':
    unittest.main()