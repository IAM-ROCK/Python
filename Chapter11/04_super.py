class Employee:
    def __init__(self):
        print("Constructor of  Employee")
    a=1

class Progarmmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of  Programmer")
    b=2

class Manager(Progarmmer):
    def __init__(self):
        super().__init__()
        print("Constructor of  Manager")
    c=3

#o=Employee()
#print(o.a) # Prints the a attribute
#print(o.b) #shows an error as there is no b attributes in employee class

#o=Progarmmer()
#print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
