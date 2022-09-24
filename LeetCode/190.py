"""
DIFFICULTY : medium
TAGS : divide and conquer, bit manipulation
"""
class Solution:
    # Same as reverse integer but instead of base 10 we 
    # have base 2. So, instead of x 10**i, etc. we can 
    # bit manipulation
    
    # IN DECIMAL
    # rev = (rev * 10) + (num % 10) 
    # num //= 10
    
    # IN BINARY
    # rev = (rev * 2) + (num % 2)
    # num //= 2
    
    # USING BIT MANIPULATION
    # rev = (rev << 1) + (num & 1)
    # num >>= 1
    
    # &1 gives us the last digit ( here, last bit )
    # + can also be substituted with boolean OR since
    # we are dealing with bits, they are the same
    
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32) :
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev