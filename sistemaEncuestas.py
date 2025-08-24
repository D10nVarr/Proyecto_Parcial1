class probador:
    def __init__(self):
        self.preguntas=["¿Si o no?", "¿Te gusta la comida?", "¿Cuánto pesas?"]

class register_request(probador): #(CreateSurvey)
    def __init__(self):
        super().__init__()
        self.respuestas={}

    def registrar_repuestas(self):
        for i, pregunta in enumerate(self.preguntas, start=1):
            respuesta=input(f"{i}. {pregunta}: ")
            self.respuestas[pregunta] = respuesta

    def mostrar_respuestas(self):
        for i, valor in enumerate(self.respuestas.values(), start=1):
            print(f"Pregunta {i}: {valor}")


objeto=register_request()

objeto.registrar_repuestas()

objeto.mostrar_respuestas()
