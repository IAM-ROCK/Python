'''

def rem(l,word):
    for item in l:
        l.remove(word)
        return l

l=["deekshith","Deepak","Sandeep"]    

print(rem(l,"deekshith"))

'''


def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["deekshith","deepak","Sandeep"]    

print(rem(l,"deep"))