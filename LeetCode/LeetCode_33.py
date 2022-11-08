"""
DIFFICULTY : medium
TAGS : array, binary search
"""
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        def find_pivot(arr) :
            l = 0
            r = len(arr) - 1
            while(l < r) :
                mid = l + (r - l) // 2
                if(arr[0] <= arr[mid]) :
                    l = mid + 1
                else :
                    r = mid
            return l
        
        def bs(arr, l, r, target) :
            while(l <= r) :
                mid = l + (r - l) // 2
                if(arr[mid] < target) :
                    l = mid + 1
                elif(arr[mid] > target) :
                    r = mid - 1
                else :
                    return mid
            return -1
        
        pivot = find_pivot(arr)
        
        if(target >= arr[pivot] and target <= arr[len(arr) - 1]) :
            return bs(arr, pivot, len(arr)-1, target)
        else :
            return bs(arr, 0, pivot-1, target)