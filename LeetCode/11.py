class Solution:
    # Use 2 pointers and the fact that the 
    # smaller of the 2 heights can be safely
    # removed from further consideration because 
    # it can not contribute more than what it 
    # already has
    def maxArea(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1
        total = 0
        while(i < j) :
            total = max(total, min(arr[i], arr[j]) * (j - i))
            if(arr[i] < arr[j]) :
                i += 1
            else :
                j -= 1
        return total
        