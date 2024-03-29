def getLongestSubarray(arr: [int], k: int) -> int:
    n = len(arr)
    mp = {}
    temp = s = ans = 0
    for i in range(n):
        temp += arr[i]
        if (temp not in mp):
            # Not considering all occurences of a prefix sum
            # since we want the longest subarray
            mp[temp] = i
    for i in range(n):
        s += arr[i]
        if (s == k):
            ans = max(ans, i+1)
        elif (s-k in mp):
            ans = max(ans, i-mp[(s-k)])
    return ans
