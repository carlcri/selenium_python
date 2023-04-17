import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class DynamicControls(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod 
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize

	def test_dynamic_controls(self):
		driver = self.driver
		checkBox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')

		if checkBox.is_enabled == True:
			checkBox.click()	

		removeAddButton = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
		removeAddButton.click()

		WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
		removeAddButton.click()


	def test_dynamic_controls_1(self):
		driver = self.driver
		enableDisablebutton = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
		enableDisablebutton.click()

		WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))
		text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
		text_area.send_keys('Hola Mundo')

		enableDisablebutton.click()


	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
