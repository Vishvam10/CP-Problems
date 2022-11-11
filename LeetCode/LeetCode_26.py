"""
DIFFICULTY : easy
TAGS : array, two pointers
"""
class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        # Leave the first element as it will be unique anyway
        left = 1
        for i in range(1, len(arr)) :
            if(arr[i- 1] != arr[i]) :
                arr[left] = arr[i]
                left +=note 1
        return left