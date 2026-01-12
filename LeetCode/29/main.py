class Solution:
    # IDEA : Repeated subtraction but instead of subtracting
    # the divided once every time, we take the biggest
    # power of 2 * dividend every time, then decrease the
    # power pf 2
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        a, b, res = abs(dividend), abs(divisor), 0

        for i in range(32, -1, -1):
            if (a >> i) >= b:
                a -= b << i
                res += 1 << i

        return res if (dividend > 0) == (divisor > 0) else -res
