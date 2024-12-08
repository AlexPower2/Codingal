def getMaxLength(a, size):
    counter=0
    maxOnes=0

    for i in range(0, size):

        if (a[i]==0):
            counter=0

        else:
            counter+=1
            maxOnes=max(maxOnes, counter)

    return maxOnes

a=[0,1,1,0,1,0,0,1,0,1,1]
size=len(a)

print("Max 1's: ",getMaxLength(a, size))