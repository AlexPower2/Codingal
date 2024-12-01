def calculateProfit(arr,arr_size):
    profit=0
    for i in range(1, arr_size):

        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]

    return profit

prices=[356,782,479,290,274,432,657]

profit= calculateProfit(prices,len(prices))
print("Max profit : ", profit)