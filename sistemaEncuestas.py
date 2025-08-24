class CreateSurvey:
    def __init__(self):
        self.questionList =[]

    def agregar_question(self, question):
        self.questionList.append(question)

class register_request(CreateSurvey):
    def __init__(self):
        super().__init__()
        self.respuestas={}

    def registrar_respuestas(self):
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
            print("No hay respuestas registradas todavia.")
            return
        for i, (pregunta,valor) in enumerate(self.respuestas.items(), start=1):
            print(f"Pregunta {i}: {pregunta}")
            print(f"Respuesta: {valor}\n")
encuestas={}

num_encuesta=int(input("Ingrese el numero de encuestas: "))


for i in range(num_encuesta):
    nombre=input("Ingrese el nombre de la encuesta: ")
    ##Pruebas de compatibilidad/posible forma de manejar el ingreso de datos
    while True:
        try:
            cantidad =int(input("Ingrese la cantidad de preguntas a ingresar: "))
            if cantidad <=0:
                print("Debe ingresar un numero mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un numero valido.")
    respuesta = register_request()

    for i in range(cantidad):
        variable=input(f"Ingrese la pregunta {i+1}: ")
        respuesta.agregar_question(variable)

    encuestas[nombre]=respuesta
escojer = input("Escoja una encuesta: ")
if escojer in encuestas:
    encuestas[escojer].registrar_respuestas()
else:
    print("La encuesta no existe.")

for nombre,valor in encuestas.items():
    print(f"\nEncuestas: {nombre}")
    valor.mostrar_respuestas()

respuesta.registrar_respuestas()
respuesta.mostrar_respuestas()