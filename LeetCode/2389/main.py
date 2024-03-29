"""
DIFFICULTY : easy
TAGS : array, binary search, greedy, sorting, prefix sum
"""


class Solution:
    def answerQueries(self, arr: List[int], queries: List[int]) -> List[int]:
        arr.sort()
        ans = []
        for target in queries:
            temp = 0
            count = 0
            for val in arr:
                if (temp + val <= target):
                    temp += val
                    count += 1
                else:
                    break
            ans.append(count)

        return ans
