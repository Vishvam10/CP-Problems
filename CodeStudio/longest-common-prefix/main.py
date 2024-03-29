from typing import List


def commonPrefix(arr: List[str], n: int) -> str:
    n = len(arr)
    arr.sort(key=lambda x: len(x))
    check = arr[0]
    m = len(check)
    c = m
    for word in arr:
        for i in range(m):
            if (check[i] != word[i]):
                c = min(c, i)
                break
    if (c == 0):
        return -1
    return check[:c]
