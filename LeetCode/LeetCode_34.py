"""
DIFFICULTY : medium
TAGS : array, binary search
"""
class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        
        if(len(arr) == 0) :
            return [-1, -1]
        
        def FIRST(arr, low, high, target) :
            res = -1
            while low <= high:
                mid = low + (high- low) // 2
                if(arr[mid] == target) :
                    res = mid
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else :
                    high = mid - 1
            return res
        
        def LAST(arr, low, high, target) :
            res = -1
            while(low <= high) :
                mid = low + (high - low) // 2
                if(arr[mid] == target) :
                    res = mid
                    low = mid + 1
                elif(arr[mid] < target) :
                    low = mid + 1
                else :
                    high = mid - 1
            return res
        
        return [FIRST(arr, 0, len(arr)-1, target), LAST(arr, 0, len(arr)-1, target)]