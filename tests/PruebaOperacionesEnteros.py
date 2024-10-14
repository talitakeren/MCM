import unittest
from src.logica.OperacionesEnteros import OperacionesEnteros
from src.logica.FaltanParametros import FaltanParametros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_LCM_dosNumerosPositivos_retornaLCM(self):
        numero1 = 18
        numero2 = 24
        resultadoEsperado = 72
        operacion = OperacionesEnteros([numero1, numero2])
        resultadoActual = operacion.calcularLCM()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_LCM_tresNumerosPositivos_retornaLCM(self):
        numero1 = 18
        numero2 = 24
        numero3 = 30
        resultadoEsperado = 360
        operacion = OperacionesEnteros([numero1, numero2, numero3])
        resultadoActual = operacion.calcularLCM()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_LCM_cuatroNumerosPositivos_retornaLCM(self):
        numero1 = 18
        numero2 = 24
        numero3 = 30
        numero4 = 4
        resultadoEsperado = 360
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])
        resultadoActual = operacion.calcularLCM()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_LCM_unNumeroPositivo_lanzaExcepcion(self):
        numero1 = 18
        operacion = OperacionesEnteros([numero1])
        with self.assertRaises(FaltanParametros):
            operacion.calcularLCM()

    def test_LCM_unaCadena_lanzaExcepcion(self):
        numero1 = "18a"
        numero2 = 13
        operacion = OperacionesEnteros([numero1, numero2])
        with self.assertRaises(ValueError):
            operacion.calcularLCM()
