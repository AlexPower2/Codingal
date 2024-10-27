def indec(n,num):
    if(n<1 or n>num):
        return
    print(n) #For decreasing order
    indec(n-1,num)
    print(n) #For increasing order

n=int(input("Enter any number n: "))
indec(n,n)