def sum_of_all_subarrays(arr, n, size):
    ans = []
    s = sum(arr[:k])

    ans.append(s)

    for i in range(k, n):
        # arr[end] - arr[start]
        s += arr[i] - arr[i - k]
        ans.append(s)

    return ans


arr = [1, -2, 3, -4, 5, 6]
n = len(arr)
k = 2

assert [-1, 1, -1, 1, 11] == sum_of_all_subarrays(arr, n, k)
