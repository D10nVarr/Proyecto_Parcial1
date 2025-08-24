class CreateSurvey:
    def __init__(self):
        self.questionList =[]

    def agregar_question(self, question):
        self.questionList.append(question)

class register_request(CreateSurvey): #(CreateSurvey)
    def __init__(self):
        super().__init__()
        self.respuestas={}

    def registrar_repuestas(self):
        for i, pregunta in enumerate(self.questionList, start=1):
            respuesta=input(f"{i}. {pregunta}: ")
            self.respuestas[pregunta] = respuesta

    def mostrar_respuestas(self):
        for i, valor in enumerate(self.respuestas.values(), start=1):
            print(f"Pregunta {i}: {valor}")




##Pruebas de compatibilidad/posible forma de manejar el ingreso de datos
respuesta = register_request()#Instanciamiento de objeto, donde se toma tanto la lista de preguntas como de respuestas
for i in range(3):
    si=input(f"Ingrese el pregunta {i+1}: ")
    respuesta.agregar_question(si)

respuesta.registrar_repuestas()
respuesta.mostrar_respuestas()