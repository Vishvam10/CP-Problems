from typing import List


def immediateSmaller(arr: List[int]) -> None:

    n = len(arr)

    for i in range(1, n):
        arr[i-1] = arr[i] if (arr[i] < arr[i-1]) else -1
