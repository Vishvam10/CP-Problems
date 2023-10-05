"""
DIFFICULTY : medium
TAGS : array, sorting
"""
class Solution:        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            temp = True
            arr.sort()
            for i in range(len(arr)-1):
                if (arr[i+1] - arr[i] != arr[1] - arr[0]):
                    temp = False
                    break
            ans.append(temp)
        return ans