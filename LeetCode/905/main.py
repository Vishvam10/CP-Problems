class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        # arr.sort(key=lambda x: x & 1)
        left, right = 0, len(arr) - 1

        while(left <= right) :
            
            if(arr[left] % 2 > arr[right] % 2) :
                arr[left], arr[right] = arr[right], arr[left]
            
            if(arr[left] % 2 == 0) :
                left += 1
            
            if(arr[right] % 2 == 1) :
                right -= 1
        
        return arr