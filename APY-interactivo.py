#importacion de librerias
from openai import OpenAI
import os

#definimos el cliente
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

#mensajes
messages=[
    {"role": "system", "content":'''
        eres un alumno de la UES, solo responder preguntas relacionadas al contenido:
        1.- Inteligencia Artificial , url://www.ues.mx, dia: Lunes a Viernes
        2.- Front-end, url://www.ues.mx, dia: Lunes a Viernes
        3.- Programacion web, url://www.ues.mx, dia: Lunes a Viernes'''},
]

#interactividad
user_message = ''

#declaramos un bucle 
while(user_message != 'exit'):
    #se carga el mensaje del usuario en la variable
    print("redactar el mensaje del usuario: ")
    user_message = input()

    #manejo del historial y los mensajes
    if len(messages) >=1 and len(messages) <=4:
        messages.append({'role': 'user', 'content': user_message})
    else:
        #colocamos un bucle for
        for i in range(3, len(messages), 2):
            messages[i-2] = messages[i]
            messages[i-1] = messages[i+1]
        
        messages[len(messages) - 2] = {'role': 'user', 'content': user_message}
        messages.pop

    #establecemos la respuesta
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        temperature=0.2,
        messages= messages
    )

    assistan_message = response.choices[0].message.content
    print(f"LA API responde de la siguiente manera --> {assistan_message}")

    #despues de la llamda a la api
    print(f"Despues de haber llamado a la API, tenemos la siguiente respuesta --->")
    print(messages)