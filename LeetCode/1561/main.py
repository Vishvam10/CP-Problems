"""
DIFFICULTY : medium
TAGS : array, math, greedy, sorting, game theory
"""


class Solution:
    # Eg. 2, 4, 1, 2, 7, 8, 9, 1, 10, 11, 4, 5
    # 11, 10, 9, 8, 7, 5, 4, 4, -2-, -2-, -1-, -1-
    # (11, 10, 1), (9, 8, 1), (7, 5, 2), (4, 4, 2)

    # Or the reverse. So the final arrangement will be :
    # S S S S ... M L M L M L (S : Small, M : Medium, L : Large)

    # So, start from n//3 elements and add every second element

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        ans = 0
        for i in range(n // 3, n, 2):
            ans += piles[i]
        return ans
