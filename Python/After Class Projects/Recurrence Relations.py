def myfunction(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction(n/2)
    myfunction(n/3)
def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)