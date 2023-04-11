import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ExplicitWaitTests(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod 
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize
	def test_add_remove(self):
		add_element_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/button')))

		elements_added = input('Elementos a añadir: ')

		for i in range(int(elements_added)):
			add_element_button.click()	
		sleep(3)


		for i in range(int(elements_added)):
			remove_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="elements"]/button')))
			remove_button.click()
		sleep(1)


	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
