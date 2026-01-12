def removeDuplicates(arr, n):
    j = 0
    for i in range(1, n, 1):
        if arr[i] == arr[j]:
            continue
        else:
            j += 1
            arr[j] = arr[i]

    return j + 1
