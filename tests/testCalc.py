import unittest
from page_objects.calculadora import Calculadora
from webdriver.webdriver import Driver


class testCalculadora(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def testSoma(self):
        calculadora = Calculadora(self.driver)
        formula_esperada = '5+6'
        resultado_esperado = 11
        formula, resultado = calculadora.somar(5, 6)
        assert resultado_esperado == resultado
        assert formula_esperada == formula

    def testSubtracao(self):
        calculadora = Calculadora(self.driver)
        formula_esperada = '9−3'
        resultado_esperado = 6
        formula, resultado = calculadora.subtrair(9, 3)
        assert resultado_esperado == resultado
        assert formula_esperada == formula

    def testDivisao(self):
        calculadora = Calculadora(self.driver)
        formula_esperada = '8÷2'
        resultado_esperado = 4
        formula, resultado = calculadora.dividir(8, 2)
        assert resultado_esperado == resultado
        assert formula_esperada == formula

    def testMultiplicacao(self):
        calculadora = Calculadora(self.driver)
        formula_esperada = '4×3'
        resultado_esperado = 12
        formula, resultado = calculadora.multiplicar(4, 3)
        assert resultado_esperado == resultado
        assert formula_esperada == formula

    def tearDown(self):
        self.driver.instance.quit()
