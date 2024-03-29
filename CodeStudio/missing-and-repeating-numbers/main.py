from collections import defaultdict


def findMissingRepeatingNumbers(a: [int]) -> [int]:
    n = len(a)
    p = q = 0
    mp = [0 for _ in range(n+1)]
    for x in a:
        mp[x] += 1

    for i in range(1, n+1, 1):
        if (mp[i] == 0):
            q = i
        if (mp[i] > 1):
            p = i

    return [p, q]
