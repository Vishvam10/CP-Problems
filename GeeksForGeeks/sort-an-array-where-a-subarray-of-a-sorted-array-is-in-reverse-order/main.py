
def sort_where_subarray_is_sorted_in_reverse_order(arr, n):

    left, right = -1, -1

    for i in range(1, n):
        if (arr[i] < arr[i-1]):
            left = i-1
            break

    for i in range(n-2, -1, -1):
        if (arr[i] < arr[i+1]):
            right = i
            break

    if (left == -1 and right == -1):
        return arr

    while (left <= right):

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    print(arr)

    return arr


# Given that the subarray is sorted in descending order
# and the array is sorted in ascending order
# a = [2, 5, 65, 55, 50, 70, 90]
a = [1, 7, 6, 5, 4, 3, 2, 8]
n = len(a)
sort_where_subarray_is_sorted_in_reverse_order(a, n)
