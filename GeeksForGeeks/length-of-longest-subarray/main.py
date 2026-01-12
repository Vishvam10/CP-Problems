def longestSubarry(arr, n):
    if n == 1:
        return 1 if arr[0] >= 0 else 0

    if n == 2:
        if arr[0] >= 0 and arr[1] >= 0:
            return 2
        if arr[0] >= 0 or arr[1] >= 0:
            return 1
        return 0

    left, right, ans = 0, 0, -1

    while right < n and left <= right:
        if arr[right] < 0:
            ans = max(ans, right - left)
            while right < n and arr[right] < 0:
                right += 1
            left = right
        right += 1

    ans = max(ans, right - left)

    return ans if ans != -1 else 0
