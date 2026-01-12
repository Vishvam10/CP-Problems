def linearSearch(n: int, num: int, arr: [int]) -> int:
    for ind, x in enumerate(arr):
        if x == num:
            return ind
    return -1
