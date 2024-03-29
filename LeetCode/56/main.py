"""
DIFFICULTY : medium
TAGS : array
"""


class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr = sorted(arr, key=lambda x: x[0])
        ans = []
        for ele in arr:
            if (not ans or ans[-1][1] < ele[0]):
                ans.append(ele)
            else:
                ans[-1][1] = max(ans[-1][1], ele[1])

        return ans
