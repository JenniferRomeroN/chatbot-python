from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#importamos modulos adicionales
from openai import OpenAI
import os

#creacion del cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

#generamos una funcion 
def call_endpoint(messages):
    chatgpt_messages_list = [
        {"role": "system", "content": '''
            Eres un alumno de la universidad estatal de sonora, solo puedes contestar en relacion al contenido:
            mi correo electronico es: jenniferomero03@gmail.com, mi celular es: 6621328425
            las materias que llevo son: 
            1.- front-end, url: www.ues.mx, dias: lunes, martes y jueves
            2.- progrmacion web, url: www.ues.mx, dias: lunes y jueves ''' }
    ]

    chatgpt_response = chatgpt_messages_list + messages
    
    #modelo para obtener una respuesta
    chatgpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature= 0.2,
        messages=messages
    )

    assitant_message = chatgpt_response.choices[0].message.content

    return assitant_message

#colocamos las opciones
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\jenni\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

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
    last_message = last_messages [1]

    #enviamos a impresion
    last_message_text = last_message.find_element(By.XPATH, '//div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span')
    print(f'user message:{last_message.text}')

    #establecemos una lista
    message_list = []
    message_list.append({'role': 'user', 'content': last_message.text})

    #notificamos al usuario, que se envia el mensaje de texto
    print('sending message to lenguaje service')
    #simulacion de api
    #api_message = "mensaje de respuesta desde la api"

    api_message = call_endpoint(message_list)
    
    message_element = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')
    message_element.send_keys(f'{api_message}{Keys.ENTER}')
    message_element.send_keys(Keys.ESCAPE)
