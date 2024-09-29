from math import sqrt
number=int(input("Enter your number :"))
print("\n")
c=0
if number > 1:
    for i  in range(2, int(sqrt(number))+1):
        if (number % i) == 0:
            print(number, "is not a prime number")
            c=1
            break
        
if c==0:
    print(number, "is a prime number")
        