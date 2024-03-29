def moveZeros(n: int,  a: [int]) -> [int]:
    n = len(a)
    left = 0
    for i in range(n):
        if (a[i] != 0):
            a[i], a[left] = a[left], a[i]
            left += 1
    return a
