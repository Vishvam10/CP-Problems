class Solution:
    def search(self, arr: List[int], x: int) -> int:
        n = len(arr)
        if(n == 0) : 
            return -1
        low, high = 0, n - 1
        while(low <= high) :
            mid = low + (high - low) // 2
            # print(low, high, mid, arr[mid], x)
            if(arr[mid] == x) :
                return mid
            
            # If left-part is sorted
            if(arr[low] <= arr[mid]) :
                if(arr[low] <= x and x <= arr[mid]) :
                    high = mid - 1
                else :
                    low = mid + 1
            # If right-part is sorted
            else :
                if(arr[mid] <= x and x <= arr[high]) :
                    low = mid + 1
                else :
                    high = mid - 1
            

        return -1