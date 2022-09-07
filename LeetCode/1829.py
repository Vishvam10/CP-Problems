class Solution:
    # Inverse of XOR is XOR. So, instead of calculating
    # cumulative XOR every time we remove an element, we 
    # can just reuse the total XOR. So, if s = total_XOR, then :
    
    # s = s XOR arr.pop()
    
    # Similar to the case when s = total_sum and we remove 
    # the last element, we don't need to find the sum all over
    # again, instead we could just subtract the last element
    
    def getMaximumXor(self, arr: List[int], k: int) -> List[int]:
        m = 2**k - 1
        ans = []
        s = reduce(lambda x, y : x ^ y, arr)
        while len(arr) > 0 :
            ans.append(s ^ m)
            s ^= arr.pop()
        return ans