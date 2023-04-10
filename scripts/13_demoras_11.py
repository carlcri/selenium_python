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
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize
	def test_account_link(self):
		WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, 'select-language').get_attribute('length')=='3')

		account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
		account.click()

		self.driver.find_element(By.LINK_TEXT, 'Register').click()

#		driver = self.driver
#		length = driver.find_element(By.ID, 'select-language').get_attribute('length')
#		self.assertTrue(length == '3')
	

	def test_create_new_customer(self):
		self.driver.find_element(By.LINK_TEXT, 'ACCOUNT').click()
		my_account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
		my_account.click()

		create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
		create_account_button.click()

		WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

	#	self.driver.find_element(By.LINK_TEXT, 'My Account').click()

	def hola(self):
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
