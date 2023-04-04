import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = self.driver	#para no esta escribieno self.driver en cada linea
		driver.implicitly_wait(10) #esperar 10 segundo 'implicitamente' antes de realizar la siguiente accion
#		return super().setUp()

	#Caso de prueba, para que el navegador las automatize
	def test_hello_world(self):
		driver = self.driver
		driver.get('https://www.platzi.com')
		

	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	def tearDown(self):
		self.driver.quit()
#		return super().tearDown()

	
if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
		
