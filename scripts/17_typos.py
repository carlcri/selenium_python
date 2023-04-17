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
		driver.find_element(By.LINK_TEXT, 'Typos').click()
		driver.maximize_window()	

	#Casos de prueba, para que el navegador los automatize

	def test_find_typo(self):
		driver = self.driver
		correct_text = "Sometimes you'll see a typo, other times you won't."

		tries = 0
		found = False
		

		while(found is not True):
			typo = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
			print(typo.text)

			if typo.text != correct_text:
				tries+=1
				driver.refresh()
			
			else:
				found = True
				break

			if tries >= 10:
				break

		print(f'intentos: {tries+1}')
		print(found)

	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()	

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
