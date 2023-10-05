"""
DIFFICULTY : easy
TAGS : array, hash table, two pointers, binary search, sorting
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)) :
            if(nums1[i] in nums2) :
                ans.append(nums1[i])
        return set(ans)