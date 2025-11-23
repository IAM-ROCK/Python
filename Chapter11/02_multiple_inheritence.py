class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class Coder:
    language="Python"
    def printLanguages(self):
        print(f"Out of all languahes here is your language: {self.language}")


class Programmer(Employee,Coder):
    company="ITC Infotech"
    def showLangauage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")




a=Employee()
b=Programmer()


print(a.company , b.company)
b.show()
b.printLanguages()
b.showLangauage()

print(b.language)