from typing import List


def generateSubsequences(s: str) -> List[str]:
    def generate(s, start, n, pref, acc):
        if len(pref) == n:
            acc.append(pref)
            return

        for i in range(start, len(s)):
            temp = pref + s[i]
            generate(s, i + 1, n, temp, acc)

        return acc

    ans = [""]
    for i in range(1, len(s) + 1):
        temp = generate(s, 0, i, "", [])
        ans.extend(temp)

    return ans
