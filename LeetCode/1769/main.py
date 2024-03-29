"""
DIFFICULTY : medium
TAGS : array, string
"""


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        ans = []
        for i in range(len(boxes)):
            if (boxes[i] == "1"):
                ones.append(i)

        for i in range(len(boxes)):
            s = 0
            for j in range(len(ones)):
                ind = ones[j]
                s += abs(i - ind)
            ans.append(s)

        return ans
