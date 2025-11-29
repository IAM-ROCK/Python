from functools import reduce

a=[1,2,111,65,345,34567]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))