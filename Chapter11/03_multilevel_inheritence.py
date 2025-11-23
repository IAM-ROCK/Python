class Employee:
    a=1

class Progarmmer(Employee):
    b=2

class Manager(Progarmmer):
    c=3

o=Employee()
print(o.a) # Prints the a attribute
#print(o.b) #shows an error as there is no b attributes in employee class

o=Progarmmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
