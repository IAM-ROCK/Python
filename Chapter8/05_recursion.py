'''
factorial(1)=1
factorial(2)=2X1
factorial(3)=3X2X1
factorial(4)=4X3X2X1
factorial(5)=5X4X3X2X1


factorial(n)=nXn-1X........3X2X1

factorial(n)=n*factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)


n=int(input("Enter the number: "))
print(f"Factorial of this number is:{factorial(n)}")
print("Factorial of this number is:",factorial(n))