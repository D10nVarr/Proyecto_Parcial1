Este programa es un sistema de gestión de encuestas basado en Python y diseñado con fines educativos. 
Este sistema permite crear al usuario preguntas dinamicas, recopilar respuestas y visualizar los resultados a través de una interfaz de consola. 

Arquitectura del programa:
El programa cuenta con listas, clases, funciones y variables.
Se denomina un diccionario principal, en donde se guardarán las diferentes encuestas que se deseen realizar, en donde se encontrarán sus preguntas y sus respectivas respuestas.

A traves de una clase denominada "Create Survey", se crean las preguntas y se guardan dentro de una lista.

A través de la clase register Request se recorre dicha lista en donde se almacenan las preguntas para convertir estas mismas en inputs que puedan ser contestados por un usuario.
Misma clase hace que cada pregunta sea guardada dentro del diccionario en dodne el valor es la respuesta, y su clave es la rpegunta ("pregunta": "respuesta")

A traves de una funcion while, se hace un menú que permitirá al usuario escoger la acción a realizar, donde a traves del método "mostrar_respuestas", que está dentro de la clase registerRequests,
el usuario podrá mostrar las preguntas y sus respuestas.
