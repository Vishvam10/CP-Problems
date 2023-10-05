class Solution:
    def search(self, arr, n):
        left = 0
        right = len(arr)-1
        mid = 0
     
        if (n == 1):
            return arr[0]
     
        if (arr[left] != arr[left + 1]): 
            return arr[left]
     
        if (arr[right] != arr[right - 1]): 
            return arr[right]
        
        while (left <= right):
            mid = left + (right - left) // 2
            if (arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]):
                return arr[mid]
            elif((arr[mid] == arr[mid + 1] and mid % 2 == 0) or (arr[mid] == arr[mid - 1] and mid % 2 != 0)):
                left = mid + 1
            else:
                right = mid - 1
         
        return -1
            