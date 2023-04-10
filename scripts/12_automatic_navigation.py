import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class NavigationTest(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod 
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://google.com')
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize
	def test_browser_navigation(self):
		driver = self.driver

		search_field = driver.find_element(By.NAME, 'q')
		search_field.clear()
		search_field.send_keys('Gonzallo Guillen')
		search_field.submit()
		driver.implicitly_wait(2)

		driver.back()
		sleep(1)
		driver.forward()
		sleep(1)
		driver.refresh()
		sleep(1)

	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
