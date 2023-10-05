def longestSubarrayWithSumK(a: [int], k: int) -> int:

    # Prefix sums

    n = len(a)
    ans = 0
    pre = [0] * (n+1)
    pre[0] = a[0]
    
    for i in range(1, n, 1) :
        pre[i] = pre[i-1] + a[i]

    for i in range(n) :
        for j in range(i, n) :
            temp = pre[j] - pre[i]
            if(temp == k) :
                ans = max(ans, j-i)
    return ans

    # Sliding window
   
    # n = len(a)
    # ans = 0
    # left = right = 0
    # s = 0
    # while(right < n) :
    #     s += a[right]
    #     while(s > k) :
    #         s -= a[left]
    #         left += 1
    #     if(s == k) :
    #         ans = max(ans, right-left+1)
    #     right += 1
    # return ans