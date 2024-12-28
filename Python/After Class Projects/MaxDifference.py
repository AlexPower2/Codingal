def max_difference(arr):
    if len(arr) < 2:
        return 0  
    
    min_value = float('inf')  # Initialize to a very large number
    max_value = float('-inf') # Initialize to a very small number

    
    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return max_value - min_value


arr = [4, 5, 234, 2, 6, 82, 234, 5234]
print(max_difference(arr))
