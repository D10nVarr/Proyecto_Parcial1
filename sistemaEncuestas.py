class CreateSurvey:
    def __init__(self):
        self.questionList =[]

    def agregar_question(self, question):
        self.questionList.append(question)

class register_request(CreateSurvey):
    def __init__(self):
        super().__init__()
        self.respuestas={}

    def registrar_repuestas(self):
        if not self.questionList:
            raise ValueError("No hay preguntas registradas aún.")
        for i, pregunta in enumerate (self.questionList, start=1):
            respuesta= input(f"{i}. {pregunta}: ").strip()
            if not respuesta:
                print("Se registrara como 'Sin respuesta'.")
                respuesta = "Sin respuesta"
            self.respuestas[pregunta] = respuesta
        print("Respuestas registradas correctamente")

    def mostrar_respuestas(self):
        if not self.respuestas:
            print("No hay respiestas registradas todavia.")
            return
        for i, (pregunta,valor) in enumerate(self.respuestas.items(), start=1):
            print(f"Pregunta {i}: {pregunta}")
            print(f"Respuesta: {valor}\n")
titul_encuesta = input("Ingrese el titulo de la encuesta: ")
respuesta = register_request(titul_encuesta)

while True:
    cantidad = input("Ingrese la cantidad de preguntas: ")
    if cantidad <= 0:
        print("las preguntas deben ser mayor a 0.")
        continue

    for i range(cantidad)
        pregunta = input(f"Ingrese la pregunta {i + 1}")



respuesta.registrar_repuestas()
respuesta.mostrar_respuestas()
