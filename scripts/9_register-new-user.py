import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
La prueba consiste en encontrar la barra de busqueda usando distintos selectores.
Realiza todas las pruebas en una sola ventana a diferencia del codigo anterior

'''

class RegisterNewUser(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = cls.driver
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()

	def test_new_user(self):
		self.driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
		self.driver.find_element(By.LINK_TEXT, 'Log In').click()

		create_account_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled()) 
		create_account_button.click()

		self.assertEqual(self.driver.title, 'Create New Customer Account')

		driver = self.driver
		first_name = driver.find_element(By.NAME, 'firstname')
		middle_name = driver.find_element(By.ID, 'middlename')
		last_name = driver.find_element(By.ID, 'lastname')
		email_address = driver.find_element(By.ID, 'email_address')
		news_letter_suscription = driver.find_element(By.ID, 'is_subscribed')  
		password = driver.find_element(By.ID, 'password')
		confirm_password = driver.find_element(By.ID, 'confirmation')
		register_button = driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')
		
		# Se verifica los campos esten habilitados
		self.assertTrue(first_name.is_enabled() 
		and middle_name.is_enabled()
		and last_name.is_enabled()
		and email_address.is_enabled()
		and news_letter_suscription.is_enabled()
		and password.is_enabled()
		and confirm_password.is_enabled
		and register_button.is_enabled()) 

		#Se envian los datos a los campos
		first_name.send_keys('Gonzalo')
		driver.implicitly_wait(1)
		middle_name.send_keys('El Duro')
		driver.implicitly_wait(1)
		last_name.send_keys('Guillen')
		driver.implicitly_wait(1)
		email_address.send_keys('gonza@lanuevaprensa.com')
		driver.implicitly_wait(1)
		news_letter_suscription.click()
		driver.implicitly_wait(1)
		password.send_keys('Matarife')
		driver.implicitly_wait(1)
		confirm_password.send_keys('Matarife')
		driver.implicitly_wait(1)
		register_button.click()
		driver.implicitly_wait(5)


	
	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	
if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = '7search-text-r1'))
		
