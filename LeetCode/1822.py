"""
DIFFICULTY : easy
TAGS : array, math
"""
class Solution:
    # Converting +ves to 1 and -ves to -1 to 
    # avoid overflows
    def arraySign(self, arr: List[int]) -> int:
        prod = 1
        for i in range(len(arr)) :
            if(arr[i] == 0) :
                return 0
            elif(arr[i] > 0) :
                arr[i] = 1
            else :
                arr[i] = -1
        
        for i in range(len(arr)) :
            prod *= arr[i]
            
        if(prod == 1) :
            return 1
        return -1