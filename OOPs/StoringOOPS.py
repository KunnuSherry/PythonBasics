# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
    def getInfo(self):
        print(f'Name is: {self.name}')

Kunal = Programmer('kunal', 'python', 100000000)
Kunal.getInfo()