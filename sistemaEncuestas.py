questionList = []

class CreateSurvey:
    def __init__(self, question):
        self.question = question
        super().__init__()
        questionList.append(self)
    def __str__(self):
        return f"Pregunta: {self.question}"

class register_request: #(CreateSurvey)
    def __init__(self):
        self.respuestas={}

    def registrar_repuestas(self):
        if not questionList:
            raise ValueError("No hay preguntas registradas aún.")
        for i, pregunta in enumerate(questionList, start=1):
            respuesta= input(f"{i}. {pregunta}: ").strip()
            if not respuesta:
                print("Se registrara como 'Sin respuesta'.")
                respuesta = "Sin respuesta"
            self.respuestas[pregunta] = respuesta
        print("Respuestas registradas correctamente")

    def mostrar_respuestas(self):
        if not self.respuestas
            print("No hay respiestas registradas todavia.")
            return
        for i, (pregunta,valor) in enumerate(self.respuestas.values(), start=1):
            print(f"Pregunta {i}: {pregunta}")
            print(f"Respuesta: {valor}")

class SistemaEncuestas:
    def __init__(self):
        self.respuestas_guardadas = []

    def crear_encuesta(self):



