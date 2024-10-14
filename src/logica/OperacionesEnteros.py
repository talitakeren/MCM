from src.logica.FaltanParametros import FaltanParametros
import math

class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularLCM(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        elif len(self.__numeros) > 1:
            return self.LCMMasDosNumeros()
        else:
            return 0

    def LCM(self, numero1, numero2):
        return abs(numero1 * numero2) // math.gcd(numero1, numero2)

    def LCMMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError

        cantidadNumeros = len(self.__numeros)
        lcm = self.LCM(self.__numeros[0], self.__numeros[1])
        for i in range(2, cantidadNumeros):
            lcm = self.LCM(lcm, self.__numeros[i])
        return lcm
