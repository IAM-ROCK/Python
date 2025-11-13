f=open("poem.txt")
c=f.read()
if("Twinkle" in c):
    print("The word Twinkle is present in the content")
    
else:
    print("The word twinkle is not present in the content")    
    
f.close()
