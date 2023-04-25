"""
Test Codigo Apuesta Dado
Omar Gaspar
Cedula 28593179
"""

from Ejercicio_Dado.ejercicio_dados import apuesta
from Ejercicio_Promedio_y_Moda.descriptiva import modaEdades, promedioEdades
import unittest

class test(unittest.TestCase):
    
    def testDado(self):
        resultado = apuesta()
        self.assertEqual((resultado % 2), 1)

    def testPromedioModa(self):
        promedio = promedioEdades()
        moda = modaEdades()
        self.assertEqual(promedio, 22)
        self.assertEqual(moda, 21)



if __name__ == '__main__':
    unittest.main()