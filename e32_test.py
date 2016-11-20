import unittest

from e32 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_es_pandigital(self):
        self.assertTrue(es_pandigital('456781239'))

if __name__ == '__main__':
    unittest.main()   