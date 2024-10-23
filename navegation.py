#hacemos las importaciones
#webdriver es de selenium
from selenium import webdriver
#time es para pausar la ejecucion
import time

driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024, 720)

#navegacion hacia la pagina de whatsapp
driver.get(("https://web.whatsapp.com/"))
time.sleep(15)

#navegacion hacia el url
#abre el navegador en la pagina principal
driver.get("https://google.com")
#imprime el titulo de la pagina actual, en este ejemplo "google"
print(driver.title)
#el timepo que se pausa cuando se abre el navegador
time.sleep(15)

#metodo BACK
driver.back()
print(driver.current_url)
time.sleep(5)