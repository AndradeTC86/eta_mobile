from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Calculadora:
    def __init__(self, driver):
        self.driver = driver
        self.elements = {}
        self._initialize_elements()

    def _initialize_elements(self):
        element_ids = {
            'num0': 'com.android.calculator2:id/digit_0',
            'num1': 'com.android.calculator2:id/digit_1',
            'num2': 'com.android.calculator2:id/digit_2',
            'num3': 'com.android.calculator2:id/digit_3',
            'num4': 'com.android.calculator2:id/digit_4',
            'num5': 'com.android.calculator2:id/digit_5',
            'num6': 'com.android.calculator2:id/digit_6',
            'num7': 'com.android.calculator2:id/digit_7',
            'num8': 'com.android.calculator2:id/digit_8',
            'num9': 'com.android.calculator2:id/digit_9',
            'ponto': 'com.android.calculator2:id/dec_point',
            'add': 'com.android.calculator2:id/op_add',
            'sub': 'com.android.calculator2:id/op_sub',
            'mul': 'com.android.calculator2:id/op_mul',
            'div': 'com.android.calculator2:id/op_div',
            'eq': 'com.android.calculator2:id/eq',
            'delete': 'com.android.calculator2:id/del',
            'formula': 'com.android.calculator2:id/formula',
            'result': 'com.android.calculator2:id/result'
        }
        for key, value in element_ids.items():
            try:
                self.elements[key] = WebDriverWait(self.driver.instance, 1).until(
                    EC.presence_of_element_located((By.ID, value))
                )
            except Exception as e:
                print(f"Error initializing element {key}: {e}")

    def clicarnumero(self, num):
        select = str(num)
        self.elements[f'num{select}'].click()

    def somar(self, num1, num2):
        self.clicarnumero(num1)
        self.elements['add'].click()
        self.clicarnumero(num2)
        formula = self.elements['formula'].text
        result = int(self.elements['result'].text)
        return formula, result

    def subtrair(self, num1, num2):
        self.clicarnumero(num1)
        self.elements['sub'].click()
        self.clicarnumero(num2)
        formula = self.elements['formula'].text
        result = int(self.elements['result'].text)
        return formula, result

    def dividir(self, num1, num2):
        self.clicarnumero(num1)
        self.elements['div'].click()
        self.clicarnumero(num2)
        formula = self.elements['formula'].text
        result = int(self.elements['result'].text)
        return formula, result

    def multiplicar(self, num1, num2):
        self.clicarnumero(num1)
        self.elements['mul'].click()
        self.clicarnumero(num2)
        formula = self.elements['formula'].text
        result = int(self.elements['result'].text)
        return formula, result