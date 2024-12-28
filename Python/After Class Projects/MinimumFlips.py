def count_flips(arr):
    if not arr:
        return []

    
    flips_to_0 = 0
    flips_to_1 = 0
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  
            if arr[i] == 0:
                flips_to_1 += 1  
            else:
                flips_to_0 += 1  

    
    if arr[0] == 1:
        flips_to_0 += 1
    else:
        flips_to_1 += 1

    
    if flips_to_0 < flips_to_1:
        result = []
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                if arr[i] == 0:
                    result.append(f"From {i} to {i+1}")
        return result
    else:
        result = []
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                if arr[i] == 1:
                    result.append(f"From {i} to {i+1}")
        return result



arr = [0, 1, 1, 0, 0, 0, 1, 1]
result = count_flips(arr)
print(result)  
