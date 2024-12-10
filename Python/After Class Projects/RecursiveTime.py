def fac(n):
    if(n==1 or n==0):
        return 1
    return n* fac(n-1)

def print1to10(n):
    if(n>10):
        return
    print(n)
    print1to10(n+1)

a=int(input("Enter a number: "))
print("Factorial of the number enterd: ",fac(a))

print("Factorial of the number enterd: ",print1to10(a))