def search(arr, n, x):

    low, high = 0, n - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if (arr[mid] == x):
            return mid
        if (arr[low] <= arr[mid]):
            if (arr[low] <= x and x <= arr[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (arr[mid] <= x and x <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1
    return -1
