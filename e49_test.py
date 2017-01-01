import unittest
from euler_util import *
from e49 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_completar_ceros_un_digito(self):
        self.assertEqual(completar_ceros(1), '0001')

    def test_completar_ceros_tres_digitos(self):
        self.assertEqual(completar_ceros(111), '0111')

    def test_completar_ceros_cuatro_digitos(self):
        self.assertEqual(completar_ceros(1111), '1111')

    def test_ordenar_caracteres_de_string(self):
        self.assertEqual(ordernar_caracteres('4921'), '1249')

if __name__ == '__main__':
    unittest.main()   