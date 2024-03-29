class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(x):
            s = 0
            while (x > 0):
                digit = x % 10
                x //= 10
                s += digit ** 2
            return s

        seen = set()

        while (n != 1 and n not in seen):
            seen.add(n)
            n = get_next(n)
        return n == 1
