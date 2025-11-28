l=[3,56,67,88,980]

'''index=0
for item in l:
    index +=1
    print(f"The item number at index {index} is {item}")'''


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")