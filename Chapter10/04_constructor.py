class Employee:   
    language="Py" # This is a class attribute
    salary=120000
    
    def __init__(self):
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

deekshith=Employee()
deekshith.name="Deekshith"
print(deekshith.name,deekshith.salary)

