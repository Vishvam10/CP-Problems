"""
DIFFICULTY : medium
TAGS : array, math, dp, game theory
"""
class Solution:
    # In the description, we know that sum(piles) is odd.
#     If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
#     If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.
#     So, Alex always defeats Lee in this game.
    def stoneGame(self, arr: List[int]) -> bool:
        return True
        
        