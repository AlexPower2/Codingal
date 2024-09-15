def prints(n):
    if(n<=0):
        return
    print("hello")
    prints(n//2)
prints(10)