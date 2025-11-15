class Employee:   
    language="Py" # This is a class attribute
    salary=120000
    
harry=Employee()
harry.name="Harry" #object attribute(instance attribute)
print(harry.name,harry.salary,harry.language)

deekshith=Employee()
deekshith.name="Deekshith"
print(deekshith.name,deekshith.salary,deekshith.language)


# Here name is object attribute and salry and language are class
# attribute as they dicrectly belong to the class