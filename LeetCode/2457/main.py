"""
DIFFICULTY : medium
TAGS : math, greedy
"""


class Solution:
    # IDEA : Go from right (say n-1 == i),
    # for every iteration, increase the next (i+1 == n-2)
    # digit by 1 and set everything before it to 0

    # In other words, turn the rightmost non-zero digit
    # to zero until the digit sum is greater than target.
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def ds(n):
            s = 0
            while (n):
                s += n % 10
                n //= 10
            return s
        temp = n
        i = 0
        while ds(n) > target:
            # Not just n // 10. For example, 123456 -> 12346. To do so,
            # we need n // 10 = 12345 then +1 to give us 12346
            n = n // 10 + 1
            i += 1
        return n * (10 ** i) - temp
