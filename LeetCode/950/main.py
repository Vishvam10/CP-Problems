"""
DIFFICULTY : medium
TAGS : array, queue, sorting, simulation
"""


class Solution:
    def deckRevealedIncreasing(self, arr: List[int]) -> List[int]:
        ans = []
        for x in sorted(arr)[::-1]:
            ans = [x] + ans[-1:] + ans[:-1]
        return ans
