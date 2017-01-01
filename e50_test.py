import unittest
from euler_util import *
from e50 import *

class Test(unittest.TestCase):
    
    def setUp(self):
        self.limite = 20
        self.primos = [i for i in primes_sieve(self.limite)]

    def test_posicion_anterior_a_superar_limite_2(self):
        self.assertEqual(cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, 0), 4)
    
    def test_posicion_anterior_a_superar_limite_3(self):
        self.assertEqual(cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, 1), 3)
    
    def test_posicion_anterior_a_superar_limite_19(self):
        self.assertEqual(cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, 7), 1)

    def test_cantidad_elementos_suma_es_primo_2(self):
        primera_posicion = 0
        c = cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, primera_posicion)
        self.assertEqual(cantidad_elementos_suma_es_primo(self.primos, primera_posicion, c), 4)

    def test_cantidad_elementos_suma_es_primo3(self):
        primera_posicion = 1
        c = cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, primera_posicion)
        self.assertEqual(cantidad_elementos_suma_es_primo(self.primos, primera_posicion, c), 1)

    def test_cantidad_elementos_suma_es_primo97(self):
        primera_posicion = 7
        c = cantidad_elementos_anterior_a_superar_limite(self.primos, self.limite, primera_posicion)
        self.assertEqual(cantidad_elementos_suma_es_primo(self.primos, primera_posicion, c), 1)

if __name__ == '__main__':
    unittest.main()   