"""
DIFFICULTY : medium
TAGS : array, greedy
"""
class Solution:
    def maximumTop(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        if(k == 0) :
            if(n >= 1) :
                return arr[0]
            return -1
        
        if(k == 1) :
            if(n == 1) :
                return -1
            return arr[1]
        
        if(n == 1) :
            if(k % 2 == 0) :
                return arr[0]
            return -1
        
        max_ele = max(arr[0:min(k-1, n)])
        
        if(k < n) :
            max_ele = max(max_ele, arr[k])
            
        return max_ele
        