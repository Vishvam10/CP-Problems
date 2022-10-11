"""
DIFFICULTY : medium
TAGS : array, dp
"""
class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        prod = 1
        ans = float("-inf")
        
        for i in range(len(arr)) :
            prod *= arr[i]
            ans = max(ans, prod)
            if(prod == 0) :
                prod = 1
                
        prod = 1
        
        for i in range(len(arr) - 1, -1, -1) :
            prod *= arr[i]
            ans = max(ans, prod)
            if(prod == 0) :
                prod = 1
                
        return ans