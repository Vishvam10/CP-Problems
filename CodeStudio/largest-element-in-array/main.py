def largestElement(arr: [], n: int) -> int:
    ans = float("-inf")
    for i in range(n):
        if arr[i] > ans:
            ans = arr[i]
    return ans
