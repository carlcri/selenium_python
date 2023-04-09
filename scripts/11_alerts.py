import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ComareProducts(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	@classmethod 
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()

	#Casos de prueba, para que el navegador los automatize
	def test_compare_products_removal_alert(self):
		driver = self.driver
		search_field = driver.find_element(By.ID, "search")
		search_field.clear()
		search_field.send_keys('tee')
		search_field.submit()
		driver.implicitly_wait(2)

		driver.find_element(By.CLASS_NAME, "link-compare").click()
		driver.find_element(By.LINK_TEXT, "Clear All").click()
		driver.implicitly_wait(2)

		alert = driver.switch_to.alert
		alert_text = alert.text
		self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
		alert.accept()


	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
	