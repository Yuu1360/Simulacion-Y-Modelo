"""
Test Codigo Apuesta Dado
Omar Gaspar
Cedula 28593179
"""

from Ejercicio_Dado.ejercicio_dados import apuesta
from Ejercicio_Promedio_y_Moda.descriptiva import modaEdades, promedioEdades
from Variables_Aleatorias_Discretas.descriptiva import bernoulliExtito, bernoulliFracaso, binomial, geometrica, poisson
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

    def testVariablesAleatorias(self):
        self.assertEqual(round(bernoulliExtito(0.8), 2), 0.8)
        self.assertEqual(round(bernoulliFracaso(0.8), 2), 0.2)
        self.assertEqual(round(binomial(4, 3, 0.8), 2), 0.41)
        self.assertEqual(round(geometrica(0.8, 2), 2), 0.16)
        self.assertEqual(round(poisson(5, 3), 2), 0.14)



if __name__ == '__main__':
    unittest.main()