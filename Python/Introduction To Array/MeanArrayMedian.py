def arrayMean(arr,array_size):
    total_sum=0
    for i in range(0,array_size):
        total_sum += arr[i]

    return float(total_sum/array_size)

def arrayMedian(arr,array_size):
    sorted(arr)

    if array_size % 2 == 0:

        return int(arr[int((array_size-1)/2)]+arr[int(array_size/2)]/2)
        
    return arr[array_size/2]
    

arr=[1,4,5,2,5,8,5,2,6,8]
array_size=len(arr)

print("Mean =", arrayMean(arr, array_size))
print("Median =", arrayMedian(arr,array_size))
    
