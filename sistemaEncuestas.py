surveys = {}

class CreateSurvey:
    def __init__(self, survey_name):
        self.survey_name = survey_name
        self.question_list = []

    def agregar_question(self, question):
        if question != "":
            self.question_list.append(question)
        else:
            print("¡Pregunta vacía! No se puede agregar.")

class RegisterRequest(CreateSurvey): #(CreateSurvey)
    def __init__(self, survey_name):
        super().__init__(survey_name)
        self.answers = {}

    def registrar_respuestas(self):
        if len(self.question_list) == 0:
            print("Esta encuesta no tiene preguntas para responder.")
        else:
            print(f"\nEncuesta {self.survey_name}")
            for index, question in enumerate(self.question_list, start=1):
                try:
                    answer = input(f"{index}. {question}: ")
                    if answer.strip() == "":
                        raise ValueError("La respuesta no puede estar vacía.")
                    self.answers[question] = answer
                except ValueError as error:
                    print(f"Error: {error}")
                except Exception as error:
                    print(f"Error inesperado: {error}")

    def mostrar_respuestas(self):
        if len(self.answers) == 0:
            print("No hay respuestas registradas para esta encuesta.")
        else:
            for index, (question, value) in enumerate(self.answers.items(), start=1):
                print(f"Pregunta {index}: {question}")
                print(f"Respuesta: {value}\n")

while True:
    print("\nBienvenido al sistema de Encuestas Dinámicas")
    print("1. Crear una encuesta")
    print("2. Responder una encuesta")
    print("3. Mostrar respuestas de la encuesta a escoger")
    print("4. Salir")

    option = input("Selecciona una opción (1-4): ")

    match option:
        case "1":
            try:
                num_survey = int(input("\nIngrese el numero de encuestas: "))
                if num_survey <= 0:
                    print("Número inválido. Debe ser mayor a cero.")
                else:
                    for index in range(num_survey):
                        survey_name = input("Ingrese el nombre de la encuesta: ").lower()
                        if survey_name.isdigit() or survey_name == "":
                            print("Nombre inválido. Debe contener letras.")
                        elif survey_name in surveys:
                            print("El nombre de la encuesta ya existe. No se puede agregar.")
                        else:
                            try:
                                quantity = input("Ingrese la cantidad de preguntas a ingresar: ")
                                quantity = int(quantity)
                                if quantity <= 0:
                                    print("Número de preguntas inválido. Debe ser mayor que 0.")
                                else:
                                    survey = RegisterRequest(survey_name)
                                    for q_index in range(quantity):
                                        question = input(f"Ingrese la pregunta {q_index + 1}: ")
                                        survey.agregar_question(question)
                                    surveys[survey_name] = survey
                                    print("Encuestas registradas.")
                            except ValueError:
                                print("Error: La cantidad de preguntas debe ser un número entero válido.")
                            except Exception as error:
                                print(f"Error inesperado al ingresar la cantidad de preguntas: {error}")
            except ValueError:
                print("Error: Debe ingresar un número entero válido para la cantidad de encuestas.")
            except Exception as error:
                print(f"Error inesperado al ingresar el número de encuestas: {error}")

        case "2":
            if len(surveys) == 0:
                print("No hay encuestas registradas para responder.")
            else:
                try:
                    choose = input("Ingrese el nombre de la encuesta que desee responder: ").lower()

                    if choose.strip() == "":
                        raise ValueError("El nombre de la encuesta no puede estar vacío.")

                    if choose in surveys:
                        surveys[choose].registrar_respuestas()
                    else:
                        print("Encuesta no encontrada.")
                except ValueError as error:
                    print(f"Error: {error}")
                except Exception as error:
                    print(f"Error inesperado: {error}")

        case "3":
            if not surveys:
                print("No hay encuestas registradas.")
            else:
                print("Encuestas disponibles:")
                for survey_name in surveys:  # directamente recorre las claves
                    print(f"- {survey_name}")
                try:
                    chosen_name = input("Ingrese el nombre de la encuesta que desea ver: ").lower()

                    if chosen_name.strip() == "":
                        raise ValueError("El nombre de la encuesta no puede estar vacío.")

                    if chosen_name in surveys:
                        surveys[chosen_name].mostrar_respuestas()
                    else:
                        print("Encuesta no encontrada.")
                except ValueError as error:
                    print(f"Error: {error}")
                except Exception as error:
                    print(f"Error inesperado: {error}")

        case "4":
            print("Saliendo...")
            break

        case _:
            print("Opción no válida")
