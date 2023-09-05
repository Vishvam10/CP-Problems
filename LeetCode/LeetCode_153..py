class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        low, high = 0, n - 1
        while(low < high) :
            mid = low + (high - low) // 2
            if(arr[mid] > arr[high]) :
                low = mid + 1
            else :
                high = mid
        return arr[low]