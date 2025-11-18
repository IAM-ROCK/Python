class Employee:   
    language="Py" # This is a class attribute
    salary=120000
    
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

deekshith=Employee( "Deekshith",130000,"JavaScript")
#deekshith.name="Deekshith"
print(deekshith.name,deekshith.salary,deekshith.language)

#rohan=Employee() 

