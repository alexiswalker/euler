import unittest
from e80 import *

class Test(unittest.TestCase):
    def setUp(self):
        self.decimales_raiz_dos = '1414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572'
        self.number = 2

    def test_cien_primeros_digitos(self):
        self.assertEqual(cien_primeros_digitos(self.number), self.decimales_raiz_dos)

    def test_suma_cien_primeros_digitos(self):
        self.assertEqual(475, suma_cien_primeros_digitos(cien_primeros_digitos(self.number)))

    def test_longitud_decimales(self):
        self.assertEqual(len(cien_primeros_digitos(self.number)), 100)

    def test_resultado(self):
        self.assertEqual(40886, resultado())

if __name__ == '__main__':
    unittest.main()        