from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Calculadora:
    def __init__(self, driver):
        self.driver = driver
        self.num0 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_0')))
        self.num1 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_1')))
        self.num2 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_2')))
        self.num3 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_3')))
        self.num4 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_4')))
        self.num5 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_5')))
        self.num6 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_6')))
        self.num7 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_7')))
        self.num8 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_8')))
        self.num9 = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/digit_9')))
        self.ponto = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/dec_point')))
        self.add = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/op_add')))
        self.sub = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/op_sub')))
        self.mul = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/op_mul')))
        self.div = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/op_div')))
        self.eq = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/eq')))
        self.delete = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/del')))
        self.formula = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/formula')))
        self.result = WebDriverWait(self.driver.instance, 1) \
            .until(EC.presence_of_element_located((By.ID, 'com.android.calculator2:id/result')))

    def clicarnumero(self, num):
        select = str(num)
        self.driver.instance.find_element(By.ID, 'com.android.calculator2:id/digit_' + select).click()

    def somar(self, num1, num2):
        self.clicarnumero(num1)
        self.add.click()
        self.clicarnumero(num2)
        self.eq.click()
        return int(self.result.text)

    def subtrair(self, num1, num2):
        self.clicarnumero(num1)
        self.sub.click()
        self.clicarnumero(num2)
        self.eq.click()
        return int(self.result.text)

    def dividir(self, num1, num2):
        self.clicarnumero(num1)
        self.div.click()
        self.clicarnumero(num2)
        self.eq.click()
        return int(self.result.text)

    def multiplicar(self, num1, num2):
        self.clicarnumero(num1)
        self.mul.click()
        self.clicarnumero(num2)
        self.eq.click()
        return int(self.result.text)


