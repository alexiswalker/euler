import unittest
from euler_util import *
from e47 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_divisores(self):
        self.assertEqual(divisores(10), [1, 10, 2, 5])

    def test_divisores_primos_10(self):
        self.assertEqual(divisores_primos(10), [2,5])

    def test_divisores_primos_644(self):
        self.assertEqual(divisores_primos(644), [2,7,23])

    def test_divisores_primos_645(self):
        self.assertEqual(divisores_primos(645), [3,5,43])

    def test_divisores_primos_646(self):
        self.assertEqual(divisores_primos(646), [2,17,19])


if __name__ == '__main__':
    unittest.main()   