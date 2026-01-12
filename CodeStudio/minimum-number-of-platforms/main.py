from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def calculateMinPatforms(arr, dep, n):
    """
    900 940 950 1100 1500 1800
    910 1200 1120 1130 1900 2000

    --
       ----------
         -----
            ---
                    -------
                            -----
    """
    arr.sort()
    dep.sort()
    i, j, platforms, ans = 1, 0, 1, 1
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        ans = max(ans, platforms)

    # print('ans : ', ans)
    return ans
