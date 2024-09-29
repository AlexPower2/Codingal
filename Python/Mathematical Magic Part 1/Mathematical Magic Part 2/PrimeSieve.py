def SieveOfEratosthenes(num):
    prime =[True for i in range(num+1)]

    p = 2
    while (p * p <= num):


        if (prime[p] == True):

            for i in range(p*p, num+1, p):
                prime[i]=False
        p += 1

    for p in range(2, num+1):
        if prime[p]:
            print(p)

number = int(input("Enter the last number of the range: "))

print("Prime number in the range of 2 to ", number, "are: ")
SieveOfEratosthenes(number)