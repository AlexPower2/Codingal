def way(stairs):

    if stairs < 0:
        return 0
    
    if stairs == 0:
        return 1
    
    TwoSteps= 0
    OneStep= 0

    if (stairs >= 2):

        TwoSteps= way(stairs -2)

    OneStep=way(stairs-1)
    return TwoSteps+OneStep

stairs=int(input("Enter number of steps: "))

print("Number of way to climb: ", way(stairs))