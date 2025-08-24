print("commit inicial")

class CreateSurvey:
    def __init__(self, question):
        self.question = question
        super().__init__()

x = input("Ingrese la pregunta: ")
y = CreateSurvey(x)
print(y)
print(y.question)