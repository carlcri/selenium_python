import unittest
from pyunitreport import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
La prueba consiste en encontrar la barra de busqueda usando distintos selectores.
Al no usar el decorador @classmethod cada una de las pruebas se ejecuta en una ventana diferente

'''

class HomePageTests(unittest.TestCase):

	#ejecuta lo necesario antes de hacer la prueba
	
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = '../chromedriver')
		driver = self.driver
		driver.get('http://demo-store.seleniumacademy.com/')
		driver.maximize_window()
#		driver.implicitly_wait(5)


	#Casos de prueba, para que el navegador los automatize
	def test_search_text_field(self):
		search_field = self.driver.find_element(By.ID, "search")
#		search_field = self.driver.find_element_by_id("search")


	def test_search_text_field_by_name(self):
		search_field = self.driver.find_element(By.NAME, "q")
#		search_field = self.driver.find_element_by_name("q")


	def test_search_text_field_by_class_name(self):
		search_field = self.driver.find_element(By.CLASS_NAME, "input-text" )
#		search_field = self.driver.find_element_by_class_name("input-text")


    #verificar que un el boton de la lupita de la barra de busqueda este habilitado
	def test_search_button_enabled(self):
		button = self.driver.find_element(By.CLASS_NAME, "button")
#		button = self.driver.find_element_by_class_name("button")


        #Contar los elementos que encontremos, en este caso las de la clase promos
	def test_count_of_promo_banner_images(self):
		banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
		banners = banner_list.find_elements(By.TAG_NAME, "img")

		#Assertions 
		self.assertEqual(3, len(banners))

#		banner_list = self.driver.find_element_by_class_name("promos")
#		banners = banner_list.find_elements_by_tag_name('img')

	def test_vip_promo(self):
		vip_promo =self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
#		vip_promo = self.driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

	def test_shopping_cart(self):
		shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, "div.header-minicart span.icon")

	#Acciones para finalizar. Importante cerrar la ventana del navegador despues de cada prueba	
	
	def tearDown(self):
		self.driver.quit()

	
if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = '7search-text-r'))
		

