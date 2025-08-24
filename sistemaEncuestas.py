print("commit inicial")

questionList = []

class CreateSurvey:
    def __init__(self, question):
        self.question = question
        super().__init__()
        questionList.append(self)

x = input("Ingrese la pregunta: ")
y = CreateSurvey(x)
print(y)
print(y.question)
print(questionList)