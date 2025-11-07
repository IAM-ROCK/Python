a=int(input("Enter your age: "))

if(a>=18):
    print("You can drive car")
elif(a<0):
    print("You entered an invalid age negative") 
elif(a==0):
    print("You entered an invalid age Zero")
       
else:
    print("You can't drive car")    
    
   
   # and , or , not
   
b=int(input("Enter your age: "))

if(b>=18):
    print("You can drive car")
elif(b<0 or b==0):
    print("You entered an invalid age negative") 
       
else:
    print("You can't drive car")        
    
    
