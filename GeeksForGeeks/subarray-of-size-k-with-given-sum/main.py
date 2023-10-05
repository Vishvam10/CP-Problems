

def subarray_of_size_k_with_given_sum(arr, n, k, s) :

    # pre[L..R] = pre[R] - pre[L-1]
    # Need the index of : pre[R] - k
    
    start, end, curSum = 0, -1, 0
    mp = {}

    for i in range(n) :
        curSum += arr[i]
        if(curSum == s) :
            start = 0
            end = i
            if(end - start + 1 == k) :
                break

        if((curSum - s) in mp) :
            start = mp.get(curSum - s) + 1
            end = i
            if(end - start + 1 == k) :
                break

        mp[curSum] = i

    if(end == -1) :
        return -1

    return [start, end]




arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
n = len(arr)
k = 4
s = 24


print(subarray_of_size_k_with_given_sum(arr, n, k, s))
