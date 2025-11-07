student = {"name": "Deekshith", "course": "ISE", "score": 90}

print(student.get("name"))          # Deekshith
print(student.keys())               # dict_keys(['name','course','score'])
print(student.values())             # dict_values(['Deekshith','ISE',90])
print(student.items())              # dict_items([('name','course','score')])

student.update({"score": 95})
print(student)                      # {'name':'Deekshith','course':'ISE','score':95}

student.pop("course")
print(student)                      # {'name':'Deekshith','score':95}
