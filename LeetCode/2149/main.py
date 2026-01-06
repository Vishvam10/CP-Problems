"""
DIFFICULTY : medium
TAGS : array, two pointers, simulation
"""


class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for i in range(len(arr)):
            if (arr[i] > 0):
                pos.append(arr[i])
            else:
                neg.append(arr[i])

        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans