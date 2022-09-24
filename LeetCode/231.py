class Solution:
    # IDEA : Bit pattern of powers of 2 and powers of 2 - 1
    
    # NOTE : n & (n-1) removes the last bit of a number 
    
    # For powers of 2, n is of the form 10000... and n-1 is 
    # of the form 1111... with 1 bit less (obviously). So, 
    # n & (n-1) would give us all 0s 
    
    # This is not the case for numbers that are not a power 
    # of 2. (They will leave behind atleast one 1)
    
    # So, the answer is : return n > 0 and n & (n-1) == 0
    # This can be further simplified as :
    # return n > 0 and not n&(n-1)
    
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and math.log2(n) == math.trunc(log2(n))
        return n > 0 and not n&(n-1)