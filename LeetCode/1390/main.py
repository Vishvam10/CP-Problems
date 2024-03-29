class Solution:
    def sumFourDivisors(self, arr: List[int]) -> int:

        def check(n):
            c, s = 0, 0
            for i in range(1, int(n**0.5) + 1, 1):
                if (n % i == 0):
                    if (i * i == n):
                        return 0

                    c += 2
                    s += (i + (n // i))

            return s if c == 4 else 0

        ans = 0

        for x in arr:
            ans += check(x)

        return ans
