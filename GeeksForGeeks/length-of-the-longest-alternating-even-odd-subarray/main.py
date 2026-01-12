def longest_alternating_even_odd_subarray(arr, n):
    # Check the parity of sum. Increase if odd, reset if even
    c = 1
    ans = 1

    for i in range(n - 1):
        if (arr[i] + arr[i + 1]) % 2 == 1:
            c += 1
        else:
            ans = max(ans, c)
            c = 1

    # Can never be 1 as even-odd elements must occur in pairs
    if ans == 1:
        return 0

    return max(ans, c)


arr = [1, 2, 3, 4, 5, 7, 8]
n = len(arr)

print(longest_alternating_even_odd_subarray(arr, n))
