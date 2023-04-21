"""
Test Codigo Apuesta Dado
Omar Gaspar
Cedula 28593179
"""

from ejercicio_dados import apuesta
import unittest

class testEjercicioDado(unittest.TestCase):
    
    def test(self):
        resultado = apuesta()
        self.assertEqual((resultado % 2), 1)

if __name__ == '__main__':
    unittest.main()
        
