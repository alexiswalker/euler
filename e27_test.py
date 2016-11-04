import unittest

from e27 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_lista_de_primos_entre_dos_valores(self):
        self.assertEqual(primos_entre(1,7), [2,3,5,7])

if __name__ == '__main__':
    unittest.main()      