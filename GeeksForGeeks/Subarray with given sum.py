

def subarray_of_with_given_sum(arr, n, s) :

    # pre[L..R] = pre[R] - pre[L-1]
    # Need the index of : pre[R] - k
    
    start, end, curSum = 0, -1, 0
    mp = {}

    for i in range(n) :
        curSum += arr[i]
        if(curSum == s) :
            start = 0
            end = i
            break

        if((curSum - s) in mp) :
            # print("present : ", curSum-s)
            start = mp.get(curSum - s) + 1
            end = i
            break

        mp[curSum] = i

    print("mp : ", mp)

    if(end == -1) :
        return -1

    return [start, end]




arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
n = len(arr)
k = 4
s = 10


print(subarray_of_with_given_sum(arr, n, k, s))
