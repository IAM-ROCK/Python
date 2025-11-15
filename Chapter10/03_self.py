class Employee:   
    language="Py" # This is a class attribute
    salary=120000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    

deekshith=Employee()
deekshith.language="JavaScript"  #Instance attribute 


Employee.getInfo(deekshith)
#or
deekshith.getInfo()
