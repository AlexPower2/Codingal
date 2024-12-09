def maxSubArraySum(a,size):
    max= -99999999999
    cmax=0

    for i in range(0,size):
        cmax= cmax+a[i]
        if(max <cmax):
            max = cmax

        if cmax < 0:
            cmax=0
    return max

a=[1,2,3,4,-5,-25,3,-9]
print(maxSubArraySum(a,len(a)))