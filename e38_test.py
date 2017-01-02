import unittest

from e38 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_es_pandigital(self):
        self.assertTrue(es_pandigital(123456789))

    def test_no_es_pandigital(self):
        self.assertFalse(es_pandigital(223456789))

if __name__ == '__main__':
    unittest.main()    