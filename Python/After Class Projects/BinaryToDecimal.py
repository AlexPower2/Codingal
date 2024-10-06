def binaryTodecimal(n):
    decimal = 0
    power = 1
    while n>0:
# Find the remainder of the given binary number.
        rem = n%10
        n = n//10
        decimal += rem*power
# For every remainder multiply it with the power of 2.
        power = power*2
        
    return decimal
print( binaryTodecimal(1111) )