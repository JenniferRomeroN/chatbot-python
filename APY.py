#importacion de librerias
from openai import OpenAI
import os

#definimos el cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

#respuesta

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    temperature=0.2,
    messages=[
        {"role": "system", "content":'''
            eres un alumno de la UES, solo responder preguntas relacionadas al contenido:
            1.- Inteligencia Artificial , url://www.ues.mx, dia: Lunes a Vierves
            2.- Front-end, url://www.ues.mx, dia: Lunes a Vierves
            3.- Programacion web, url://www.ues.mx, dia: Lunes a Vierves'''},
        {"role": "user", "content": "Hola, buenas tardes."},
        {"role": "user", "content": "Tienes clases los dias sabados?"},
        {"role": "user", "content": "Los dias sabado, solamente se atienden actividades extracurriculares."},
        {"role": "user", "content": "Las acrividades extracurriculares, tiene costo?"}
    ]
)

#enviamos a impresion
print(response)