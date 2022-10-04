class Solution:
    def tribonacci(self, n: int) -> int:
        if (n < 2) :
            return n;
        fi, se, th = 0, 1, 1
        x = 0
        while (n > 2) :
            x = fi + se + th
            fi = se
            se = th
            th = x
            n -= 1
        return th