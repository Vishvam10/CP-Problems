"""
DIFFICULTY : medium
TAGS : string, math, bit manipulation, simulation
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        s = ""

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            s += str(carry %2)
            carry //= 2

        return s[::-1]
                
                
        