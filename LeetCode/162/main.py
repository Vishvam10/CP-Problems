class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        
        n = len(arr)

        if(n == 1) : 
            return 0
        
        if(arr[0] > arr[1]) :
            return 0
        
        if(arr[-1] > arr[-2]) :
            return n-1

        '''
            3 cases :
                - mid is the peak
                - mid is in left of peak
                - mid is in right of peak
        '''

        low, high = 1, n-2
        
        while(low <= high) :
            
            mid = low + (high - low) // 2
            
            # mid is peak
            if(arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]) :
                return mid
            
            # mid is left of peak => go right
            elif(arr[mid] < arr[mid+1]) :
                low = mid + 1

            # mid is right of peak
            elif(arr[mid] < arr[mid-1]) :
                high = mid - 1
            
        return -1




        