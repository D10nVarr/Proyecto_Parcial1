questionList = []

class CreateSurvey:
    def __init__(self, question):
        self.question = question
        super().__init__()
        questionList.append(self)

class register_request: #(CreateSurvey)
    def __init__(self):
        super().__init__()
        self.respuestas={}

    def registrar_repuestas(self):
        for i, pregunta in enumerate(questionList, start=1):
            respuesta=input(f"{i}. {pregunta}: ")
            self.respuestas[pregunta] = respuesta

    def mostrar_respuestas(self):
        for i, valor in enumerate(self.respuestas.values(), start=1):
            print(f"Pregunta {i}: {valor}")
