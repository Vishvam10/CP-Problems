def two_equal_sum_subarray(arr, n) :

    s = sum(arr)
    temp = 0
    ind = -1
    for i in range(n) :
        temp += arr[i]
        print(temp, s - temp)
        if(temp == s - temp) :
            ind = i+1
            break
    
    if(ind == -1) :
        print("not possible")
        return -1

    print("subarrays : ", arr[:ind], arr[ind:n])

    return [arr[:ind], arr[ind:n]]


arr = [1 , 2 , 3 , 4 , 5 , 5]
n = len(arr)
two_equal_sum_subarray(arr, n)












