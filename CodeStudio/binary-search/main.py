def search(arr: [int], target: int):
    n = len(arr)
    left = 0
    right = n-1
    while (left <= right):
        mid = left + (right - left) // 2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return -1
