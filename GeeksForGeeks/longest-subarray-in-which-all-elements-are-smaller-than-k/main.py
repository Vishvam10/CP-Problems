

def largest_subarray_with_all_elements_smaller_than_k(arr, n, k):

    c = 0
    start = 0
    end = 0
    max_len = -1

    for i in range(n):
        if (arr[i] < k):
            c += 1
            end += 1
        else:
            if c > max_len:
                max_len = c
                start = i - c
            c = 0
            end = i-1

    if (c != 0):
        if c > max_len:
            max_len = c
            start = n - c
        end = n-1

    return [max_len, start, end]


arr = [1, 8, 3, 5, 2, 2, 1, 13, 3, 5, 2, 2, 1, 1, 0, 12]
N = len(arr)
K = 6

print(largest_subarray_with_all_elements_smaller_than_k(arr, N, K))
