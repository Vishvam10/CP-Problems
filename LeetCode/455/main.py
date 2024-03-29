class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        a, b, n, m = 0, 0, len(g), len(s)
        while (a < n and b < m):
            if (s[b] >= g[a]):
                a += 1
            b += 1
        return a
