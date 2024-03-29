'''
    UPPER BOUND : The smallest index i where arr[i] > x.

    The upper bound in a sorted array is the index of the first value that is greater than a given value. 
    
    IMP : If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
'''


def upperBound(arr: [int], x: int, n: int) -> int:

    left = 0
    right = n - 1
    ans = 0

    while (left <= right):

        mid = left + (right - left) // 2

        if (arr[mid] == x):
            ans = mid + 1
            left = mid + 1
        elif (arr[mid] < x):
            ans = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    return ans
