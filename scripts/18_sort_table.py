import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tabulate import tabulate


class Tables(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod 
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize

	def test_sort_tables(self):
		driver = self.driver
	
		fields = []

		for i in range(5):
			header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i+1}]')
			fields.append(header.text)

		table1 = []

		for i in range(4):
			values = []
			for j in range(5):
				info = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{i+1}]/td[{j+1}]').text
				values.append(info)
			
			row = {field:value for field, value in zip(fields,values)}
			table1.append(row)

		print(tabulate(table1, headers='keys', tablefmt='github'))


	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
