import unittest
from page_objects.calculadora import Calculadora
from webdriver.webdriver import Driver


class testCalculadora(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def testSoma(self):
        calculadora = Calculadora(self.driver)
        resultado_esperado = 11
        resultado = calculadora.somar(5, 6)
        assert resultado_esperado == resultado

    def testSubtracao(self):
        calculadora = Calculadora(self.driver)
        resultado_esperado = 6
        resultado = calculadora.subtrair(9, 3)
        assert resultado_esperado == resultado

    def testDivisao(self):
        calculadora = Calculadora(self.driver)
        resultado_esperado = 4
        resultado = calculadora.dividir(8, 2)
        assert resultado_esperado == resultado

    def testMultiplicacao(self):
        calculadora = Calculadora(self.driver)
        resultado_esperado = 12
        resultado = calculadora.multiplicar(4, 3)
        assert resultado_esperado == resultado
