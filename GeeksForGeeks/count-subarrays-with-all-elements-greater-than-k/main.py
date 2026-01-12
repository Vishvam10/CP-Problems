def subarrays_with_elements_greater_than_k(arr, n, k):
    c, ans = 0, 0

    for i in range(n):
        if arr[i] > k:
            c += 1
        else:
            ans += (c) * (c + 1) / 2
            c = 0

    if c != 0:
        ans += (c) * (c + 1) / 2

    return int(ans)


a = [3, 4, 5, 6, 7, 2, 10, 11]
n = len(a)
k = 5
print(subarrays_with_elements_greater_than_k(a, n, k))
