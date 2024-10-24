#importacion de bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#intacionamos y vamos a dimensionar
driver = webdriver.Chrome()
driver.set_window_position(0,0)
driver.set_window_size(1024, 720)

#enviarlo (solicitarlo) con una URL especifica
driver.get('https://courses.academti.com/chatbot/weather-stations/add')
time.sleep(3)

#crearemos un diccionario: key, value
station_row = {
    #nombre_diccionario={'key' : 'value'}
    'ID' : 'AGM00060580',
    'Station Name' : 'OUARGLA',
    'Elev-m' : '150',
    'Lat' : '31.917',
    'Lon' : '5.413',
    'Type' : 'Automatic',
    'Teperature' : '1',
    'Atmospheric_Pressure' : '0',
    'Humidity' : '0',
    'Precipitation' : '1',
    'Radiation' : '1'
}

#declarar variables, a las cuales le asignaremos el diccionario, asociando el valor por medio de la llave
station_id = station_row['ID']
station_name = station_row['Station Name']
station_elevation = station_row['Elev-m']
station_lat = station_row['Lat']
station_lon = station_row['Lon']
station_type = station_row['Type']
station_temperature = station_row['Teperature']
station_atmospheric_Pressure = station_row['Atmospheric_Pressure']
station_humidity = station_row['Humidity']
station_precipitation = station_row['Precipitation']
station_radiation = station_row['Radiation']

#nombre de los controles en el formulario
#ID = station_id
#nombre de la estacion = station_name
#elevacion = number 
#latitud y longitud = coordinate [0], [1]

#declarar las variales
#recuperamos y enviamos el valor del id (identificador)
station_id_element = driver.find_element(By.ID, 'stationId')
station_id_element.send_keys(station_id)
time.sleep(5)

#recuperamos y enviamos el valor del nombre
station_name_element = driver.find_element(By.NAME, 'stationName')
station_name_element.send_keys(station_name)
time.sleep(5)

#recuperamos y enviamos el valor de la elevacion
station_elevation_element = driver.find_element(By.CLASS_NAME, 'number')
station_elevation_element.send_keys(station_elevation)
time.sleep(3)

#recuperamos y enviamos el valor de lat y lon
station_element = driver.find_elements(By.CLASS_NAME, 'coordinate')
station_element[0].send_keys(str(station_lat))
time.sleep(5)

station_element[1].send_keys(str(station_lon))
time.sleep(15)


