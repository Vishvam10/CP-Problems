class Solution:
    def nthUglyNumber(self, n: int) -> int:

        res = [0] * n
        res[0] = 1

        p1, p2, p3 = 0, 0, 0

        for i in range(1, n, 1):

            t1, t2, t3 = 2 * res[p1], 3 * res[p2], 5 * res[p3]
            t4 = min(t1, t2, t3)

            if (t4 == t1):
                p1 += 1
            if (t4 == t2):
                p2 += 1
            if (t4 == t3):
                p3 += 1

            res[i] = t4

        return res[n - 1]
