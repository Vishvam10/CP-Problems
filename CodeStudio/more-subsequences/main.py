from collections import defaultdict


def moreSubsequence(n: int, m: int, a: str, b: str) -> str:
    if (len(set(a)) > len(set(b))):
        return a
    elif (len(set(a)) == len(set(b))):
        if (n > m):
            return a
        elif (n == m):
            mp1, mp2 = defaultdict(int), defaultdict(int)
            for ch in a:
                mp1[ch] += 1
            for ch in b:
                mp2[ch] += 1
            s = 0
            for v1, v2 in zip(mp1.values(), mp2.values()):
                diff = v1 - v2
                s += diff
            if (s > 0):
                return b
            else:
                return a

        else:
            return b
    else:
        return b
