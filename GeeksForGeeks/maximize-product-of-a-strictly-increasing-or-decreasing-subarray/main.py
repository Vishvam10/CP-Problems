def kadane_product(arr):
    curMin, curMax, ans = 1, 1, arr[0]

    for x in arr:
        v = (x, curMin * x, curMax * x)
        curMin, curMax = min(v), max(v)
        ans = max(ans, curMax)

    return ans


def maxSubarrayProduct(arr, n):
    i = 0
    maxProd = float("-inf")

    while i < n:
        temp = []
        temp.append(arr[i])

        # Increasing subarray
        if i < n - 1 and arr[i] < arr[i + 1]:
            while i < n - 1 and arr[i] < arr[i + 1]:
                temp.append(arr[i + 1])
                i += 1

        # Decreasing subarray
        else:
            while i < n - 1 and arr[i] > arr[i + 1]:
                temp.append(arr[i + 1])
                i += 1

        curProd = kadane_product(temp)
        maxProd = max(maxProd, curProd)

        i += 1

    return maxProd


arr = [1, 2, 10, 8, 1, 0, 0, 2, -8, -10, 100, 101]
n = len(arr)

print(kadane_product(arr))
maxSubarrayProduct(arr, n)
