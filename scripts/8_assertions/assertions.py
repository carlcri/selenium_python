import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  


'''
Se realizan tres pruebas

'''

class AssertionsTest(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()
#		driver.implicitly_wait(5)


	#Casos de prueba, para que el navegador los automatize
	def test_search_field_by_id(self):
		self.assertTrue(self.is_element_present(By.ID, "search"))


	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))


	def test_search_field_by_xpath(self):
		self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img'))


	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as variable:
			return False
		return True
	 

#if __name__ == '__main__':
#	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = '7search-text-r1'))
		
