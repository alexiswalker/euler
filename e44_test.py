import unittest
from euler_util import *
from e44 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_es_pentagono_5(self):
        self.assertTrue(es_pentagono(5))
    
    def test_es_pentagono_3(self):
        self.assertFalse(es_pentagono(3))

    def test_pentagono(self):
        self.assertEqual(pentagono(2),5)

if __name__ == '__main__':
    unittest.main()   