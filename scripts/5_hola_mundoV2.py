import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

'''
navega en dos sitios web diferentes pero en la misma ventana

'''

class HelloWorld(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver	#para no esta escribieno self.driber en cada linea
		driver.implicitly_wait(10) #esperar 10 segundo 'implicitamente' antes de realizar la siguiente accion
#		return super().setUp()

	#Casos de prueba, para que el navegador las automatize
	def test_hello_world(self):
		driver = self.driver
		driver.get('https://www.platzi.com')


	def test_visit_wikipedia(self):
		self.driver.get('https://www.wikipedia.org')	
		

	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
#		return super().tearDown()

	
if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report1'))
		
