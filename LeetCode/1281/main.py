class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        s = 0

        while n:
            n, remainder = divmod(n, 10)
            prod *= remainder
            s += remainder

        return prod - s
