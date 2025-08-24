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
        for i, (pregunta, valor) in enumerate(self.respuestas.items(), start=1):
            print(f"Pregunta {i}: {pregunta}")
            print(f"Respuesta: {valor}\n")

encuestas={}

num_encuesta=int(input("Ingrese el numero de encuestas: "))
respuesta = register_request()#Instanciamiento de objeto, donde se toma tanto la lista de preguntas como de respuestas

for i in range(num_encuesta):
    nombre=input("Ingrese el nombre de la encuesta: ")
    ##Pruebas de compatibilidad/posible forma de manejar el ingreso de datos
    cantidad=int(input("Ingrese la cantidad de preguntas a ingresar: "))
    for i in range(cantidad):
        variable=input(f"Ingrese la pregunta {i+1}: ")
        respuesta.agregar_question(variable)
    encuestas[nombre]=respuesta


for (nombre,valor) in encuestas.items():
    print(f"Encuesta {nombre}: {valor.mostrar_respuestas()}")
