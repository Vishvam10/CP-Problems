def findMin(arr: [int]):
    n = len(arr)
    low, high, ans = 0, n - 1, float("inf")
    while (low <= high):
        mid = low + (high - low) // 2
        ans = min(ans, arr[mid])

        if (arr[mid] < arr[high]):
            high = mid - 1
        else:
            low = mid + 1

    return ans
