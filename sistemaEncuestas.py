encuestas={}

class CreateSurvey:
    def __init__(self, nombre):
        self.nombre = nombre
        self.questionList =[]

    def agregar_question(self, question):
        if question != "":
            self.questionList.append(question)
        else:
            print("¡Pregunta vacía! No se puede agregar.")

class registerRequest(CreateSurvey): #(CreateSurvey)
    def __init__(self, nombre):
        super().__init__(nombre)
        self.respuestas={}

    def registrar_respuestas(self):
        if len(self.questionList) == 0:
            print("Esta encuesta no tiene preguntas para responder.")
        else:
            print(f"\nEncuesta {self.nombre}")
            for i, pregunta in enumerate(self.questionList, start=1):
                respuesta=input(f"{i}. {pregunta}: ")
                self.respuestas[pregunta] = respuesta

    def mostrar_respuestas(self):
        if len(self.respuestas) == 0:
            print("No hay respuestas registradas para esta encuesta.")
        else:
            for i, (pregunta, valor) in enumerate(self.respuestas.items(), start=1):
                print(f"Pregunta {i}: {pregunta}")
                print(f"Respuesta: {valor}\n")

while True:
    print("\nBienvenido al sistema de Encuestas Dinámicas")
    print("1. Crear una encuesta")
    print("2. Responder una encuesta")
    print("3. Mostrar respuestas de la encuesta a escoger")
    print("4. Salir")

    option=input("Selecciona una opción (1-4): ")

    match option:
        case "1":
            try:
                num_encuesta = int(input("\nIngrese el numero de encuestas: "))
                if num_encuesta <= 0:
                    print("Número inválido. Debe ser mayor a cero.")
                else:
                    for i in range(num_encuesta):
                        nombre = input("Ingrese el nombre de la encuesta: ").lower()
                        if nombre.isdigit() or nombre == "":
                            print("Nombre inválido. Debe contener letras.")
                        elif nombre in encuestas:
                            print("El nombre de la encuesta ya existe. No se puede agregar.")
                        else:
                            try:
                                cantidad = input("Ingrese la cantidad de preguntas a ingresar: ")
                                cantidad = int(cantidad)
                                if cantidad <= 0:
                                    print("Número de preguntas inválido. Debe ser mayor que 0.")
                                else:
                                    encuesta = registerRequest(nombre)
                                    for j in range(cantidad):
                                        pregunta = input(f"Ingrese la pregunta {j + 1}: ")
                                        encuesta.agregar_question(pregunta)
                                    encuestas[nombre] = encuesta
                                    print("Encuestas registradas.")
                            except ValueError:
                                print("Error: La cantidad de preguntas debe ser un número entero válido.")
                            except Exception as e:
                                print(f"Error inesperado al ingresar la cantidad de preguntas: {e}")
            except ValueError:
                print("Error: Debe ingresar un número entero válido para la cantidad de encuestas.")
            except Exception as e:
                print(f"Error inesperado al ingresar el número de encuestas: {e}")

        case "2":
            if len(encuestas) == 0:
                print("No hay encuestas registradas para responder.")
            else:
                escoger=input("Ingrese el nombre de la encuesta que desee responder: ").lower()
                if escoger in encuestas:
                    encuestas[escoger].registrar_respuestas()
                else:
                    print("Encuesta no encontrada")

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
            break

        case _:
            print("Opción no válida")