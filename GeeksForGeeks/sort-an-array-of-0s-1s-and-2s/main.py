class Solution:
    def sort012(self, arr, n):
        low = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if (arr[mid] == 0):
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif (arr[mid] == 1):
                mid += 1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        return arr
