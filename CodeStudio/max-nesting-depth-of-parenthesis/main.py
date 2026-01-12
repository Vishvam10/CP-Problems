def maxDepth(s: str) -> int:
    n = len(s)
    c = 0
    ans = 0
    for i in range(n):
        if s[i] == "(":
            c += 1
        elif s[i] == ")":
            c -= 1
            if c != 0:
                ans = max(ans, c)
    return ans + 1
