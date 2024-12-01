def findWater(a, size):
    leftTallest= [0]*size

    rightTallest=[0]*size

    water=0

    leftTallest[0]= a[0]
    for i in range(1, size):
        leftTallest[i]=max(leftTallest[i-1], a[i])

    rightTallest[size- 1] = a[size-1]
    for i in range(size-2, -1 , -1):
        rightTallest[i] = max(rightTallest[i +1], a[i])
    
    for i in range(size):
        water+= min(leftTallest[i], rightTallest[i]) - a[i]

    return water

a=[0, 1, 0, 2, 1, 0, 1, 3 ,2 ,1,2,1 ]
bars= len(a)
print("water: ", findWater(a, bars))
