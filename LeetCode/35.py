class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr)
        if(target > arr[len(arr)-1]) :
            return len(arr)
        while(low <= high) :
            mid = low + (high - low)//2
            if(arr[mid] == target) :
                return mid
            elif(arr[mid] < target) :
                low = mid + 1
            else :
                high = mid - 1
        return low