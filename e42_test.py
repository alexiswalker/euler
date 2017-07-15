import unittest
from euler_util import *
from e42 import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_es_triangulo_6(self):
        self.assertTrue(es_triangulo(6))

    def test_es_triangulo_5(self):
        self.assertFalse(es_triangulo(5))

    def test_letters(self):
        self.assertEqual(letras(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    def test_indice_letra(self):
        self.assertEqual(indice_letra('A'), 1)

    def test_indice_letra(self):
        self.assertEqual(indice_letra('Z'), 26)

if __name__ == '__main__':
    unittest.main()