def summ(n):
    if(n<=0):
        return 0
    return n+summ(n-1)
print(summ(4))
def sumarray(n):
    if(n<=2):
        return 0
    return n+sumarray(n-2)
print (sumarray(8))