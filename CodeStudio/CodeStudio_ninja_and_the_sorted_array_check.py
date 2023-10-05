def isSorted(n: int,  a: [int]) -> int:
    n = len(a)
    for i in range(1, n, 1) :
        if(a[i-1] <= a[i]) :
            continue
        else :
            return 0

    return 1
