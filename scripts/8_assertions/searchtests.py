import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By


'''
Se realizan busquedas

'''

class SearchTests(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()
#		driver.implicitly_wait(5)


	#Busca una camisa
	def test_search_tee(self):
		search_field = self.driver.find_element(By.NAME, "q")
		search_field.clear()
		search_field.send_keys('tee')
		search_field.submit()

    #Busca un salero
	def test_search_salt_shaker(self):
		search_field = self.driver.find_element(By.NAME, "q")
		search_field.clear()
		search_field.send_keys('salt shaker')
		search_field.submit()
		products = self.driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
		self.assertEqual(0, len(products))



	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
	 

#if __name__ == '__main__':
#	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = '7search-text-r1'))
		
