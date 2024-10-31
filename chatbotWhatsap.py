from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#colocamos las opciones
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\jenni\AppData\\Local\Google\\Chrome\\User Data\\Default")

#asignamos las opciones como argumento
driver = webdriver.Chrome(options=options)

#dimensionamos la ventana que se abre
driver.set_window_size(1024, 720)
driver.set_window_position(0, 0)

#implementamos el tiempo implicito
driver.implicitly_wait(3600)

#llamado a la url
driver.get("https://web.whatsapp.com/")

while(True):
    #Expresiones XPath
    #//*[@id="pane-side"]/descendant::span[contains(@aria-label, 'unread messages')]
    #//*[@id="main"]/descendant::div[@role='row']
    #//*[@id="main"]//div/div/div[1]/div[2]/div[1]/div/div[2]/div/span[1]/span
    #//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]

    #recuperamos nuevos mensajes
    new_message = driver.find_element(By.XPATH, '//*[@id="pane-side"]/descendant::span[contains(@aria-label, \'unread message\')]')
    new_message.click()

    #obtener los mensajes del usuario
    last_messages = driver.find_elements(By.XPATH, '//*[@id="main"]/descendant::div[@role=\'row\']')
    last_message = last_messages [-1]

    #enviamos a impresion
    last_message_text = last_message.find_element(By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
    print(f'user message:{last_message.text}')

    #notificamos al usuario, que se envia el mensaje de texto
    print('sending message to lenguaje service')
    api_message = "mensaje de respuesta desde la api"
    message_element = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    message_element.send_keys(f'{api_message}{Keys.ENTER}')
    message_element.send_keys(Keys.ESCAPE)
