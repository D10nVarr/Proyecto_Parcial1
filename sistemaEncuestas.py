encuestas={}

class CreateSurvey:
    def __init__(self, nombre):
        self.nombre = nombre
        self.questionList =[]

    def agregar_question(self, question):
        self.questionList.append(question)

class registerRequest(CreateSurvey): #(CreateSurvey)
    def __init__(self, nombre):
        super().__init__(nombre)
        self.respuestas={}

    def registrar_respuestas(self):
        print(f"Encuesta {self.nombre}")

        for i, pregunta in enumerate(self.questionList, start=1):
            respuesta=input(f"{i}. {pregunta}: ")
            self.respuestas[pregunta] = respuesta

    def mostrar_respuestas(self):
        for i, (pregunta, valor) in enumerate(self.respuestas.items(), start=1):
            print(f"Pregunta {i}: {pregunta}")
            print(f"Respuesta: {valor}\n")

while True:
    print("\nBienvenido al sistema de Encuestas Dinámicas")
    print("1. Crear una encuesta")
    print("2. Responder una encuesta")
    print("3. Mostrar respuestas de la encuesta a escojer")
    print("4. Salir")

    option=input("Seleccione una opciones: ")

    match option:
        case "1":
            num_encuesta=int(input("Ingrese el numero de encuestas: "))

            for i in range(num_encuesta):
                nombre = input("Ingrese el nombre de la encuesta: ").lower()
                cantidad = int(input("Ingrese la cantidad de preguntas a ingresar: "))

                encuesta = registerRequest(nombre)

                for i in range(cantidad):
                    variable = input(f"Ingrese la pregunta {i + 1}: ")
                    encuesta.agregar_question(variable)

                encuestas[nombre] = encuesta
            print("Encuestas registradas")

        case "2":
            escojer=input("Ingrese el nombre de la encuesta que desee responder: ").lower()

            encuestas[escojer].registrar_respuestas()

        case "3":
            if not encuestas:
                print("No hay encuestas registradas.")
            else:
                print("Encuestas disponibles:")
                for nombre in encuestas:  # directamente recorre las claves
                    print(f"- {nombre}")
                nombre_elegido = input("Ingrese el nombre de la encuesta que desea ver: ").lower()
                if nombre_elegido in encuestas:
                    encuestas[nombre_elegido].mostrar_respuestas()
                else:
                    print("Encuesta no encontrada.")
        case "4":
            print("Saliendo...")

        case _:
            print("Opción no válida")